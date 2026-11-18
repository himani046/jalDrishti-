"""Transparent illustrative score; replace with trained, evaluated models."""
from app.services.demo_data import WATER_BODIES
def assess_demo_vulnerability(location_id: str) -> dict:
    row=next(r for r in WATER_BODIES if r["id"]==location_id)
    change=row["water_extent_change_pct"] or 0.0
    quantity=min(100.0,max(0.0,50.0+abs(min(change,0.0))*2.0))
    level="high" if quantity>=75 else "moderate" if quantity>=50 else "low"
    return {"location_id":location_id,"quantity_score":round(quantity,1),"quality_concern_score":None,"overall_score":round(quantity,1),"risk_level":level,"confidence":"low","evidence":[f"Synthetic water extent change fixture: {change}%.","No field groundwater measurement is included.","Water quality has not been assessed; no safety inference is possible."],"recommended_actions":["Collect a field water-level observation before groundwater conclusions.","Arrange laboratory/field water-quality testing before use decisions.","Verify satellite water-extent change using cloud-masked imagery and season-matched dates."],"data_status":"illustrative_demo"}
