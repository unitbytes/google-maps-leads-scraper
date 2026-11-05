#!/usr/bin/env python3
"""
Google Maps B2B Leads, Website Contacts, Tech Stack & Reviews — Real-Time Synchronous REST API Quickstart (RapidAPI Hub & Zyla API Hub)
RapidAPI Hub: https://rapidapi.com/unitbytes/api/google-maps-b2b-leads-email-tech-stack-reviews-data-api
Zyla API Hub: https://zylalabs.com/api-marketplace/location+%26+mapping/maps+business+places+leads+and+reviews+api/14553
Docs & Schema: https://unitbytes.com/actors/google-maps-leads-scraper/

Usage:
    pip install requests
    export RAPIDAPI_KEY="your_rapidapi_key"
    python examples/run_gmaps_rapidapi.py
"""

import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
if not RAPIDAPI_KEY or RAPIDAPI_KEY.startswith("YOUR_"):
    raise SystemExit("Please set your RapidAPI key: export RAPIDAPI_KEY='your_rapidapi_key'")

BASE_URL = "https://google-maps-b2b-leads-email-tech-stack-reviews-data-api.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-host": "google-maps-b2b-leads-email-tech-stack-reviews-data-api.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
}

# 1. Search B2B Local Business Leads with Website Email & Tech Stack Enrichment
resp = requests.get(
    f"{BASE_URL}/v1/gmaps/search",
    headers=HEADERS,
    params={"query": "dentists in Austin TX", "page_size": 3, "enrich_contacts": "true"},
    timeout=30,
)
resp.raise_for_status()
items = resp.json().get("data", {}).get("items", [])
print(f"Found {len(items)} enriched Google Maps B2B leads:")
for lead in items[:3]:
    print(f" - {lead.get('title')} | Phone: {lead.get('phone')} | Email: {lead.get('primaryEmail')} | Score: {lead.get('leadScore')}")
