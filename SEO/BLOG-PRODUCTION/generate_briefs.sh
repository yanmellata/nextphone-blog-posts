#!/bin/bash

# Base path
BASE="/Users/yanismellata/Documents/nextphone/docs/SEO/BLOG-PRODUCTION"
CSV="/Users/yanismellata/Documents/nextphone/docs/SEO/Wave 2/Dec_2025_research/0_RESULTS/Wave_2_Focused_Blog_List_Dec2025.csv"

# Phase mapping (POST ranges to phase folders)
declare -A PHASE_MAP
PHASE_MAP=(
  ["120-195"]="phase-9-integrations"
  ["196-218"]="phase-10-features"
  ["219-232"]="phase-11-competitors"
  ["233-247"]="phase-12-workflows"
  ["248-259"]="phase-13-setup"
  ["260-276"]="phase-14-trust-optimization"
)

# Function to determine phase folder for a POST number
get_phase_folder() {
  local post_num=$1
  for range in "${!PHASE_MAP[@]}"; do
    IFS='-' read -r start end <<< "$range"
    if [ "$post_num" -ge "$start" ] && [ "$post_num" -le "$end" ]; then
      echo "${PHASE_MAP[$range]}"
      return
    fi
  done
}

# Read CSV and generate briefs (skip header row 1)
tail -n +2 "$CSV" | while IFS=',' read -r category subcategory title keyword angle priority validation wordcount decision; do
  # Calculate POST number (CSV row 2 = POST-120, row 3 = POST-121, etc.)
  POST_NUM=$((118 + NR))
  
  # Increment for next iteration
  ((NR++))
  
  # Get phase folder
  PHASE=$(get_phase_folder $POST_NUM)
  
  # Skip if phase not found
  if [ -z "$PHASE" ]; then
    continue
  fi
  
  # Brief file path
  BRIEF_FILE="$BASE/$PHASE/POST-$POST_NUM/0-brief.md"
  
  # Create brief content
  cat > "$BRIEF_FILE" << EOF
# POST-$POST_NUM: $category

**Category:** $category
**Subcategory:** $subcategory
**CSV Row:** $((POST_NUM - 118))

## Title
$title

## Primary Keyword
$keyword

## Angle (Unique Positioning)
$angle

## Priority
$priority

## Target Word Count
$wordcount words

## Validation
$validation mentions in Wave 2 research

## Next Steps
1. Phase 1: Research (use PHASE_1_RESEARCH_PROMPT.md)
2. Phase 2: Outline (use PHASE_2_OUTLINE_PROMPT.md)
3. Phase 3: Draft (use PHASE_3_WRITING_PROMPT.md)
4. Phase 4: QA Review (use formatting-test-comprehensive.mdx as reference)

## References
- Wave_2_Focused_Blog_List_Dec2025.csv (Row $((POST_NUM - 118)))
- BLOG_PRODUCTION_TRACKER.md (POST-$POST_NUM)
- NEXTPHONE_FACTBASE.md (data source)
- CONTENT_PRODUCTION_GUIDELINES.md (style guide)
EOF

  echo "Created brief for POST-$POST_NUM in $PHASE"
done
