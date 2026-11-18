import type { DashboardSummary, WaterBody } from "./types";
const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api/v1";
async function getJson<T>(path:string):Promise<T>{
  const response=await fetch(`${API_BASE}${path}`);
  if(!response.ok) throw new Error(`API request failed (${response.status})`);
  return response.json() as Promise<T>;
}
export const api={
  summary:()=>getJson<DashboardSummary>("/dashboard/summary"),
  waterBodies:()=>getJson<{items:WaterBody[];count:number;data_status:string}>("/water-bodies"),
  health:()=>getJson<{status:string}>("/health"),
};
