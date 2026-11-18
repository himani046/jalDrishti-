"""Transparent illustrative score. Replace with trained, evaluated models."""

from app.services.demo_data import WATER_BODIES

def assess_demo_vulnerability(location_id: str) -> dict:
    water_body = next(row for row in WATER_BODIES if row["id"] == location_id)
    change = water_body["water_extent_change_pct"] or 0.0
    # Toy demonstration of score plumbing, not a scientific index.
    quantity_score = min(100.0, max(0.0, 50.0 + abs(min(change, 0.0)) * 2.0))
    overall = quantity_score
    level = "high" if overall >= 75 else "moderate" if overall >= 50 else "low"
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
