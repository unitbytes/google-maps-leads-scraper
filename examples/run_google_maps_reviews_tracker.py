#!/usr/bin/env python3
"""
Google Maps Review Monitor & Change Tracker (Alerts & ORM) — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/google-maps-reviews-tracker?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/google-maps-reviews-tracker/
n8n Template: https://unitbytes.com/n8n/workflows/google-maps-reviews-tracker-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_google_maps_reviews_tracker.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "reviewsToCheck": [
        "https://www.google.com/maps/place/Katz's+Delicatessen/@40.722233,-73.987429,17z/"
    ],
    "trackChanges": True,
    "verifyDisappearedReviews": True,
    "reviewsSort": "newest",
    "language": "en",
    "region": "us"
}

run = client.actor("unitbytes/google-maps-reviews-tracker").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("place_name"), item.get("change_type"), item.get("review_stars"), item.get("review_text"))
