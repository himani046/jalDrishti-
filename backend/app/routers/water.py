from fastapi import APIRouter, HTTPException, Query

from app.services.demo_data import WATER_BODIES
from app.services.risk import assess_demo_vulnerability

router = APIRouter(tags=["water"])


@router.get("/water-bodies")
def list_water_bodies(district: str | None = Query(default=None)) -> dict:
    rows = WATER_BODIES
    if district:
        rows = [row for row in rows if row["district"].lower() == district.lower()]
    return {"items": rows, "count": len(rows), "data_status": "illustrative_demo"}


@router.get("/water-bodies/{water_body_id}")
def get_water_body(water_body_id: str) -> dict:
    for row in WATER_BODIES:
        if row["id"] == water_body_id:
            return row
    raise HTTPException(status_code=404, detail="Water body not found")


@router.get("/risk/{location_id}")
def get_risk(location_id: str) -> dict:
    if location_id not in {"rewa-demo-01", "rewa-demo-02"}:
        raise HTTPException(status_code=404, detail="Location not found")
    return assess_demo_vulnerability(location_id)
