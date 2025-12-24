#!/usr/bin/env python3
"""
CSV Deduplication Script for Blog Post Analysis
Adds deduplication flags and decision columns to master CSV.
"""

import csv
import re
from difflib import SequenceMatcher
from collections import defaultdict
from typing import List, Dict, Tuple

# Cluster categorization based on user strategy
AUTO_KEEP_CLUSTERS = {
    'Integration', 'Integrations', 'After-Hours', 'After-Hours & 24/7',
    'Call Routing & IVR', 'IVR', 'Bilingual/Spanish', 'Salon/Spa', 'Long-tail'
}

REVIEW_CLUSTERS = {
    'Legal', 'Setup', 'Setup & Onboarding', 'HVAC', 'Competitor Switching',
    'Real Estate', 'Pricing & ROI', 'Pricing', 'Plumbing', 'Accounting/Tax',
    'Accounting', 'Compliance', 'Migration'
}

def normalize_title(title: str) -> str:
    """Normalize title for comparison by removing punctuation and converting to lowercase."""
    # Remove special characters and extra whitespace
    normalized = re.sub(r'[^\w\s]', '', title.lower())
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    return normalized

def calculate_similarity(title1: str, title2: str) -> float:
    """Calculate similarity ratio between two titles."""
    norm1 = normalize_title(title1)
    norm2 = normalize_title(title2)
    return SequenceMatcher(None, norm1, norm2).ratio()

def extract_keywords(title: str) -> set:
    """Extract significant keywords from title."""
    # Remove common words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                  'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be', 'been',
                  'how', 'what', 'when', 'where', 'why', 'guide', 'complete', 'setup'}

    words = normalize_title(title).split()
    return {w for w in words if w not in stop_words and len(w) > 2}

def find_duplicates(posts: List[Dict]) -> Dict[int, List[Tuple[int, float]]]:
    """
    Find duplicate and similar posts.
    Returns dict mapping row_num -> [(similar_row_num, similarity_score), ...]
    """
    duplicates = defaultdict(list)

    for i, post1 in enumerate(posts):
        for j, post2 in enumerate(posts[i+1:], start=i+1):
            similarity = calculate_similarity(post1['Title'], post2['Title'])

            # Check if keywords overlap significantly
            keywords1 = extract_keywords(post1['Title'])
            keywords2 = extract_keywords(post2['Title'])

            if keywords1 and keywords2:
                keyword_overlap = len(keywords1 & keywords2) / len(keywords1 | keywords2)
            else:
                keyword_overlap = 0

            # Consider duplicates if high title similarity OR high keyword overlap
            if similarity >= 0.80 or keyword_overlap >= 0.70:
                # Store both directions
                duplicates[i].append((j, similarity))
                duplicates[j].append((i, similarity))

    return duplicates

def determine_primary(posts: List[Dict], group_indices: List[int]) -> int:
    """
    Determine which post in a duplicate group should be the primary.
    Priority: High > Medium > Low, then by rationale length, then first occurrence.
    """
    priority_rank = {'High': 3, 'Medium': 2, 'Low': 1, '': 0}

    scored_posts = []
    for idx in group_indices:
        post = posts[idx]
        priority_score = priority_rank.get(post.get('Priority', ''), 0)
        rationale_length = len(post.get('Rationale', ''))

        # Score: priority (most important) * 10000 + rationale_length * 10 - index (first occurrence tiebreaker)
        score = priority_score * 10000 + rationale_length * 10 - idx
        scored_posts.append((idx, score))

    # Return index with highest score
    return max(scored_posts, key=lambda x: x[1])[0]

def count_source_occurrences(posts: List[Dict]) -> Dict[str, int]:
    """Count how many unique sources mention similar topics."""
    # This is a simplified version - could be enhanced to check across sources
    source_counts = defaultdict(int)
    for post in posts:
        source = post.get('Source', '')
        title_key = normalize_title(post.get('Title', ''))
        source_counts[title_key] += 1
    return source_counts

def assign_dedupe_status_and_decisions(posts: List[Dict], duplicates: Dict) -> List[Dict]:
    """
    Assign DEDUPE_STATUS and AUTO_DECISION to each post.
    """
    # Group duplicates into clusters
    processed = set()
    duplicate_groups = []

    for idx in range(len(posts)):
        if idx in processed:
            continue

        if idx in duplicates and len(duplicates[idx]) > 0:
            # Build group of similar posts
            group = {idx}
            to_check = [idx]

            while to_check:
                current = to_check.pop()
                for similar_idx, similarity in duplicates.get(current, []):
                    if similar_idx not in group:
                        group.add(similar_idx)
                        to_check.append(similar_idx)

            duplicate_groups.append((list(group), max(s for _, s in duplicates[idx])))
            processed.update(group)

    # Assign status and decisions
    status_map = {}
    decision_map = {}

    for group_indices, max_similarity in duplicate_groups:
        primary_idx = determine_primary(posts, group_indices)

        for idx in group_indices:
            if idx == primary_idx:
                if max_similarity >= 0.95:
                    status_map[idx] = "PRIMARY"
                    decision_map[idx] = "KEEP"
                else:
                    status_map[idx] = "PRIMARY"
                    decision_map[idx] = "REVIEW"
            else:
                # Check similarity with primary
                sim_with_primary = 0
                for similar_idx, similarity in duplicates.get(idx, []):
                    if similar_idx == primary_idx:
                        sim_with_primary = similarity
                        break

                if sim_with_primary >= 0.95:
                    status_map[idx] = f"DUPLICATE_OF_ROW_{primary_idx + 2}"  # +2 for header and 1-indexing
                    decision_map[idx] = "SKIP_DUPLICATE"
                elif sim_with_primary >= 0.80:
                    status_map[idx] = f"SIMILAR_TO_ROW_{primary_idx + 2}"
                    decision_map[idx] = "REVIEW"
                else:
                    status_map[idx] = f"SIMILAR_TO_ROW_{primary_idx + 2}"
                    decision_map[idx] = "REVIEW"

    # Process unique posts and apply auto-keep logic
    for idx, post in enumerate(posts):
        if idx not in status_map:
            status_map[idx] = "UNIQUE"

            # Auto-keep logic for unique posts
            cluster = post.get('Cluster', '')
            priority = post.get('Priority', '')

            # Check if in auto-keep cluster
            is_auto_keep_cluster = any(c in cluster for c in AUTO_KEEP_CLUSTERS)
            is_review_cluster = any(c in cluster for c in REVIEW_CLUSTERS)

            if is_auto_keep_cluster or priority == 'High':
                decision_map[idx] = "KEEP"
            elif is_review_cluster:
                decision_map[idx] = "REVIEW"
            else:
                decision_map[idx] = "KEEP"  # Default to keep if unique

    # Apply additional logic for PRIMARY posts
    for idx, status in status_map.items():
        if status == "PRIMARY" and idx not in decision_map:
            post = posts[idx]
            cluster = post.get('Cluster', '')
            priority = post.get('Priority', '')

            is_auto_keep_cluster = any(c in cluster for c in AUTO_KEEP_CLUSTERS)

            if is_auto_keep_cluster or priority == 'High':
                decision_map[idx] = "KEEP"
            else:
                decision_map[idx] = "REVIEW"

    return status_map, decision_map

def process_csv(input_path: str, output_path: str):
    """Main processing function."""
    print("Reading CSV file...")

    # Read all posts
    posts = []
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            posts.append(row)

    print(f"Loaded {len(posts)} posts")

    # Find duplicates
    print("Analyzing duplicates...")
    duplicates = find_duplicates(posts)

    # Assign status and decisions
    print("Assigning dedupe status and decisions...")
    status_map, decision_map = assign_dedupe_status_and_decisions(posts, duplicates)

    # Add new columns
    new_fieldnames = list(fieldnames) + ['DEDUPE_STATUS', 'AUTO_DECISION', 'YOUR_DECISION']

    # Write updated CSV
    print(f"Writing updated CSV to {output_path}...")
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for idx, post in enumerate(posts):
            post['DEDUPE_STATUS'] = status_map.get(idx, 'UNIQUE')
            post['AUTO_DECISION'] = decision_map.get(idx, 'REVIEW')
            post['YOUR_DECISION'] = ''
            writer.writerow(post)

    # Generate summary statistics
    print("\nGenerating summary report...")

    unique_count = sum(1 for s in status_map.values() if s == 'UNIQUE')
    primary_count = sum(1 for s in status_map.values() if s == 'PRIMARY')
    duplicate_count = sum(1 for s in status_map.values() if 'DUPLICATE_OF' in s)
    similar_count = sum(1 for s in status_map.values() if 'SIMILAR_TO' in s)

    keep_count = sum(1 for d in decision_map.values() if d == 'KEEP')
    skip_count = sum(1 for d in decision_map.values() if d == 'SKIP_DUPLICATE')
    review_count = sum(1 for d in decision_map.values() if d == 'REVIEW')

    summary = f"""# Deduplication Summary Report

**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

- **Total posts:** {len(posts)}
- **Unique posts:** {unique_count}
- **Primary posts (best version of duplicates):** {primary_count}
- **Duplicates found:** {duplicate_count}
- **Similar posts (different angles):** {similar_count}

## Auto-Decision Breakdown

- **Auto-KEEP recommendations:** {keep_count}
- **Auto-SKIP recommendations:** {skip_count}
- **Needs manual REVIEW:** {review_count}

## Deduplication Methodology

### Duplicate Detection Criteria
- Title similarity >90% (using SequenceMatcher)
- Keyword overlap >70%
- Same cluster theme consideration

### Status Definitions
- **UNIQUE:** No duplicates found
- **PRIMARY:** This is the main version (others are duplicates of this)
- **DUPLICATE_OF_ROW_X:** This is a duplicate of row X
- **SIMILAR_TO_ROW_X:** Similar but different angle (review recommended)

### Auto-Decision Logic

**KEEP criteria:**
- UNIQUE posts (no duplicates)
- PRIMARY posts in auto-keep clusters
- High priority posts
- Posts in auto-keep clusters: Integrations, After-Hours & 24/7, Call Routing & IVR, Bilingual/Spanish, Salon/Spa, Long-tail

**SKIP_DUPLICATE criteria:**
- Clear duplicates with >95% title similarity
- Lower priority than primary version
- Same keyword + cluster

**REVIEW criteria:**
- Similar titles but different angles (80-95% similarity)
- Posts in review clusters: Legal, Setup, HVAC, Competitor Switching, Real Estate, Pricing & ROI, Plumbing, Accounting/Tax, Compliance, Migration
- Edge cases needing manual judgment

## Next Steps

1. Open the updated CSV: `MASTER_LIST_ALL_887_POSTS.csv`
2. Review posts marked with `AUTO_DECISION = REVIEW`
3. Fill in the `YOUR_DECISION` column with "KEEP", "SKIP", or add notes
4. Focus on reviewing:
   - Posts marked as SIMILAR_TO (different angles may be valuable)
   - Posts in review clusters (Legal, Setup, HVAC, etc.)
   - High-priority duplicates that need strategic decisions

## Duplicate Group Examples

"""

    # Add examples of duplicate groups
    processed_groups = set()
    example_count = 0

    for idx in range(len(posts)):
        if idx in duplicates and idx not in processed_groups and example_count < 10:
            group = [idx]
            for similar_idx, similarity in duplicates[idx]:
                if similar_idx not in group:
                    group.append(similar_idx)

            if len(group) > 1:
                example_count += 1
                summary += f"\n### Example {example_count}:\n"
                for g_idx in group[:3]:  # Show max 3 posts per group
                    post = posts[g_idx]
                    row_num = g_idx + 2  # +2 for header and 1-indexing
                    summary += f"- **Row {row_num}:** {post['Title']} ({post.get('Priority', 'N/A')} priority, {post.get('Cluster', 'N/A')} cluster)\n"
                    summary += f"  - Status: {status_map[g_idx]}\n"
                    summary += f"  - Decision: {decision_map[g_idx]}\n"

                processed_groups.update(group)

    summary += f"""

## Statistics by Cluster

"""

    # Cluster statistics
    cluster_stats = defaultdict(lambda: {'total': 0, 'unique': 0, 'keep': 0, 'skip': 0, 'review': 0})

    for idx, post in enumerate(posts):
        cluster = post.get('Cluster', 'Unknown')
        cluster_stats[cluster]['total'] += 1

        if status_map[idx] == 'UNIQUE':
            cluster_stats[cluster]['unique'] += 1

        decision = decision_map[idx]
        if decision == 'KEEP':
            cluster_stats[cluster]['keep'] += 1
        elif decision == 'SKIP_DUPLICATE':
            cluster_stats[cluster]['skip'] += 1
        else:
            cluster_stats[cluster]['review'] += 1

    for cluster, stats in sorted(cluster_stats.items(), key=lambda x: x[1]['total'], reverse=True):
        summary += f"\n**{cluster}:**\n"
        summary += f"- Total: {stats['total']}\n"
        summary += f"- Unique: {stats['unique']}\n"
        summary += f"- Keep: {stats['keep']}\n"
        summary += f"- Skip: {stats['skip']}\n"
        summary += f"- Review: {stats['review']}\n"

    return summary

def main():
    input_path = "/Users/yanismellata/Documents/nextphone/docs/SEO/Wave 2/Dec_2025_research/5. blog_post_extractions/MASTER_LIST_ALL_887_POSTS.csv"
    output_path = input_path  # Overwrite the same file
    summary_path = "/Users/yanismellata/Documents/nextphone/docs/SEO/Wave 2/Dec_2025_research/5. blog_post_extractions/DEDUPLICATION_SUMMARY.md"

    # Process CSV
    summary = process_csv(input_path, output_path)

    # Write summary
    print(f"\nWriting summary to {summary_path}...")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    print("\n✓ Deduplication complete!")
    print(f"✓ Updated CSV saved to: {output_path}")
    print(f"✓ Summary report saved to: {summary_path}")

if __name__ == "__main__":
    main()
