"""Transparent illustrative score. Replace with trained, evaluated models."""

from app.services.demo_data import WATER_BODIES


def assess_demo_vulnerability(location_id: str) -> dict:
    water_body = next(row for row in WATER_BODIES if row["id"] == location_id)
    change = water_body["water_extent_change_pct"] or 0.0

    # This is only a toy demonstration of score plumbing, not a scientific index.
    quantity_score = min(100.0, max(0.0, 50.0 + abs(min(change, 0.0)) * 2.0))
    quality_score = 0.0  # No laboratory/field measurements are present.
    overall = quantity_score  # Quality is unassessed, not assumed safe.

    if overall >= 75:
        level = "high"
    elif overall >= 50:
        level = "moderate"
    else:
        level = "low"

    return {
        "location_id": location_id,
        "quantity_score": round(quantity_score, 1),
        "quality_concern_score": None,
        "overall_score": round(overall, 1),
        "risk_level": level,
        "confidence": "low",
        "evidence": [
            f"Synthetic water extent change fixture: {change}%.",
            "No field groundwater measurement is included.",
            "Water quality has not been assessed; no safety inference is possible.",
        ],
        "recommended_actions": [
            "Collect a field water-level observation before groundwater conclusions.",
            "Arrange laboratory/field water-quality testing before use decisions.",
            "Verify satellite water-extent change using cloud-masked imagery and season-matched dates.",
        ],
        "data_status": "illustrative_demo",
    }
