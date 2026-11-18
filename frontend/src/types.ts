export interface WaterBody {
  id: string;
  name: string;
  district: string;
  latitude: number;
  longitude: number;
  observation_date: string;
  source_type: "demo" | "measured" | "satellite_proxy";
  water_extent_change_pct: number | null;
  ndwi: number | null;
  quality_status: string;
  notes: string;
}

export interface DashboardSummary {
  data_status: string;
  message: string;
  monitored_locations: number;
  water_bodies: number;
  locations_requiring_review: number;
  last_updated: string | null;
}
