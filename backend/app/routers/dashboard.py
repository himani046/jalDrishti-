from fastapi import APIRouter
from app.services.demo_data import DASHBOARD_SUMMARY

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def summary() -> dict:
    """Return clearly labelled demo summary until verified datasets are ingested."""
    return DASHBOARD_SUMMARY
