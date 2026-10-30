#!/usr/bin/env python3
"""
Google Maps Contributor Reviews Scraper (Local Guides) — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-maps-contributor-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-maps-contributor-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/google-maps-contributor-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_maps_contributor_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "contributors": ["https://www.google.com/maps/contrib/100000000000000000002"],
    "maxReviews": 50,
    "maxReviewersPerPlace": 20,
    "scrapeReviews": True,
    "placeSort": "negative_and_newest",
    "outputFormat": "flattened"
}

run = client.actor("unitbytes/google-maps-contributor-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("contributor_name"), item.get("place_name"), item.get("rating"), item.get("review_text"))
