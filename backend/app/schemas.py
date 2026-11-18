from typing import Literal
from pydantic import BaseModel, Field


RiskLevel = Literal["low", "moderate", "high", "critical"]


class WaterBody(BaseModel):
    id: str
    name: str
    district: str
    latitude: float
    longitude: float
    observation_date: str
    source_type: Literal["demo", "measured", "satellite_proxy"]
    water_extent_change_pct: float | None = None
    ndwi: float | None = None
    quality_status: str = "not_assessed"
    notes: str


class VulnerabilityAssessment(BaseModel):
    location_id: str
    quantity_score: float = Field(ge=0, le=100)
    quality_concern_score: float = Field(ge=0, le=100)
    overall_score: float = Field(ge=0, le=100)
    risk_level: RiskLevel
    confidence: Literal["low", "medium", "high"]
    evidence: list[str]
    recommended_actions: list[str]
    data_status: Literal["illustrative_demo", "observed_and_modelled"]
