"""Synthetic fixtures for UI development only. Never present these as observations."""

DASHBOARD_SUMMARY = {
    "data_status": "illustrative_demo",
    "message": "Demo values only. Connect validated official datasets before making decisions.",
    "monitored_locations": 2,
    "water_bodies": 2,
    "locations_requiring_review": 1,
    "last_updated": None,
}

WATER_BODIES = [
    {
        "id": "rewa-demo-01",
        "name": "Demo Reservoir A",
        "district": "Rewa",
        "latitude": 24.53,
        "longitude": 81.30,
        "observation_date": "2026-11-01",
        "source_type": "demo",
        "water_extent_change_pct": -12.0,
        "ndwi": 0.24,
        "quality_status": "not_assessed",
        "notes": "Synthetic example for interface testing; not a real reservoir assessment.",
    },
    {
        "id": "rewa-demo-02",
        "name": "Demo Pond B",
        "district": "Rewa",
        "latitude": 24.58,
        "longitude": 81.34,
        "observation_date": "2026-11-01",
        "source_type": "demo",
        "water_extent_change_pct": 3.5,
        "ndwi": 0.31,
        "quality_status": "not_assessed",
        "notes": "Synthetic example for interface testing; not a real pond assessment.",
    },
]
