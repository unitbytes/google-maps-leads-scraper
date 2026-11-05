#!/usr/bin/env python3
"""
Google Maps Email & Leads Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-maps-leads-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-maps-leads-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/google-maps-leads-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_maps_leads_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "searchQueries": ["dentists in Austin TX"],
    "maxPlacesPerQuery": 20,
    "reviewHookType": "most_relevant",
    "language": "en",
    "region": "us"
}

run = client.actor("unitbytes/google-maps-leads-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("business_name"), item.get("primary_email"), item.get("phone"), item.get("website"), item.get("rating"))
