from fastapi import APIRouter
from app.services.demo_data import DASHBOARD_SUMMARY
router = APIRouter(prefix="/dashboard",tags=["dashboard"])
@router.get("/summary")
def summary() -> dict:
    return DASHBOARD_SUMMARY
