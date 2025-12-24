#!/usr/bin/env python3
"""
Analyze all 23 blog post extraction files to find natural clusters
"""
import os
import re
from collections import defaultdict, Counter
import json

# File data
files_data = {
    "01_GAP_ANALYSIS": 42,
    "02_NextPhone_100_Posts": 78,
    "03_ruby": 30,
    "04_smith_ai": 32,
    "05_abby": 32,
    "06_goodcall": 28,
    "07_upfirst": 32,
    "08_emitrr": 30,
    "09_heyrosie": 32,
    "10_integration_keywords": 16,
    "11_hvac_keywords": 32,
    "12_competitor_switching": 32,
    "13_problem_solution": 32,
    "14_legal_keywords": 35,
    "15_setup_implementation": 33,
    "16_jtbd_keywords": 35,
    "17_paa_keywords": 32,
    "18_seasonal_keywords": 32,
    "19_budget_pricing": 28,
    "20_micro_niches": 30,
    "21_feature_capability": 28,
    "22_objection_concern": 33,
    "23_semrush_consolidated": 153
}

total_posts = sum(files_data.values())

# Keywords to track for clustering
cluster_keywords = {
    # Industries
    "Legal": ["legal", "law firm", "attorney", "lawyer", "solo attorney"],
    "HVAC": ["hvac", "heating", "cooling", "air conditioning", "ac", "furnace"],
    "Real Estate": ["real estate", "realtor", "property", "showing", "listing"],
    "Plumbing": ["plumbing", "plumber", "pipe", "leak", "water heater"],
    "Electrical": ["electrical", "electrician", "wiring", "power outage"],
    "Contractors": ["contractor", "construction", "general contractor", "builder"],
    "Accounting": ["accounting", "accountant", "cpa", "tax season", "bookkeeping"],
    "Salon/Spa": ["salon", "spa", "massage", "stylist", "therapist"],
    "Restaurant": ["restaurant", "dining", "reservation", "takeout"],

    # Integrations
    "HubSpot Integration": ["hubspot"],
    "Salesforce": ["salesforce"],
    "Pipedrive": ["pipedrive"],
    "Calendly": ["calendly"],
    "Google Calendar": ["google calendar"],
    "Zapier": ["zapier"],
    "Clio": ["clio"],
    "Follow Up Boss": ["follow up boss"],

    # Features
    "Bilingual/Spanish": ["bilingual", "spanish", "multilingual"],
    "Emergency Routing": ["emergency", "urgent", "priority"],
    "24/7/After-Hours": ["24/7", "after-hours", "after hours", "overnight"],
    "IVR": ["ivr", "phone menu", "auto attendant"],
    "Call Routing": ["call routing", "routing", "forwarding"],

    # Use Cases
    "Setup/Migration": ["setup", "configuration", "onboarding", "porting", "migration"],
    "Appointment Scheduling": ["appointment", "scheduling", "booking", "calendar"],

    # Comparisons
    "AI vs Human": ["ai vs", "vs virtual", "vs traditional"],
    "Competitor Switching": ["ruby", "smith.ai", "alternative to", "switch from"],

    # Pricing/ROI
    "Pricing/ROI": ["pricing", "cost", "roi", "savings", "affordable"],

    # Objections
    "Objections": ["concern", "worry", "problem", "fix", "troubleshoot"]
}

# This would scan actual files, but for now we'll create summary
print("=" * 80)
print("BLOG POST CONSOLIDATION ANALYSIS")
print("=" * 80)
print()
print(f"Total Posts Loaded: {total_posts}")
print(f"Total Sources: {len(files_data)} extraction files")
print()
print("Posts per source:")
print("-" * 80)
for source, count in sorted(files_data.items(), key=lambda x: -x[1]):
    print(f"{source:40} {count:>4} posts")
print()
print(f"Average posts per source: {total_posts / len(files_data):.1f}")
print()
