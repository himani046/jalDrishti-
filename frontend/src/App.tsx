import { useEffect, useState } from "react";
import { Activity, AlertTriangle, ArrowUpRight, Droplets, FlaskConical, Leaf, MapPinned, Satellite, Waves } from "lucide-react";
import { api } from "./api";
import type { DashboardSummary, WaterBody } from "./types";

const fallbackSummary: DashboardSummary = {
  data_status: "illustrative_demo",
  message: "Showing synthetic interface fixtures. Connect verified datasets before operational use.",
  monitored_locations: 2,
  water_bodies: 2,
  locations_requiring_review: 1,
  last_updated: null,
};
const fallbackWater: WaterBody[] = [
  { id:"rewa-demo-01", name:"Demo Reservoir A", district:"Rewa", latitude:24.53, longitude:81.30, observation_date:"2026-11-01", source_type:"demo", water_extent_change_pct:-12, ndwi:0.24, quality_status:"not_assessed", notes:"Synthetic UI fixture only." },
  { id:"rewa-demo-02", name:"Demo Pond B", district:"Rewa", latitude:24.58, longitude:81.34, observation_date:"2026-11-01", source_type:"demo", water_extent_change_pct:3.5, ndwi:0.31, quality_status:"not_assessed", notes:"Synthetic UI fixture only." },
];
function Metric({label,value,detail,icon:Icon}:{label:string;value:string|number;detail:string;icon:typeof Droplets}) {
  return <article className="metric-card"><div className="metric-head"><span>{label}</span><Icon size={19}/></div><div className="metric-value">{value}</div><p>{detail}</p></article>;
}
export default function App() {
  const [summary,setSummary]=useState(fallbackSummary);
  const [waterBodies,setWaterBodies]=useState(fallbackWater);
  const [apiState,setApiState]=useState<"connecting"|"connected"|"offline">("connecting");
  useEffect(()=>{ Promise.all([api.summary(),api.waterBodies(),api.health()]).then(([s,w])=>{setSummary(s);setWaterBodies(w.items);setApiState("connected");}).catch(()=>setApiState("offline")); },[]);
  return <main className="app-shell">
    <aside className="sidebar">
      <a className="brand" href="#"><span className="brand-mark"><Waves size={23}/></span><span>JalDrishti<small>WATER INTELLIGENCE</small></span></a>
      <div className="nav-label">WORKSPACE</div>
      <a className="nav-item active" href="#overview"><Activity size={17}/> Overview</a>
      <a className="nav-item" href="#quantity"><Droplets size={17}/> Water quantity</a>
      <a className="nav-item" href="#quality"><FlaskConical size={17}/> Water quality</a>
      <a className="nav-item" href="#satellite"><Satellite size={17}/> Satellite insights</a>
      <a className="nav-item" href="#actions"><AlertTriangle size={17}/> Risk & actions</a>
      <div className="sidebar-bottom"><span className={`status-dot ${apiState}`}/> API {apiState}</div>
    </aside>
    <section className="main-content" id="overview">
      <header className="topbar"><div><div className="eyebrow">ENVIRONMENTAL MONITORING / MADHYA PRADESH</div><h1>Water intelligence overview</h1></div><div className="location-pill"><MapPinned size={16}/> Rewa pilot <span>⌄</span></div></header>
      <section className="hero-panel"><div className="hero-copy"><div className="hero-kicker"><span className="live-dot"/> INTEGRATED WATER MONITORING</div><h2>See the water.<br/><em>Understand the risk.</em></h2><p>One view of water availability, environmental change and quality evidence to help prioritize local action.</p><a href="#water-bodies" className="hero-link">Explore monitoring locations <ArrowUpRight size={16}/></a></div><div className="hero-art" aria-hidden="true"><div className="orbit orbit-one"/><div className="orbit orbit-two"/><div className="globe"><div className="globe-line"/><div className="globe-shine"/><Waves size={66}/></div><span className="art-label label-top">SURFACE WATER</span><span className="art-label label-bottom">FIELD + SATELLITE DATA</span></div></section>
      <div className="data-notice"><AlertTriangle size={17}/><span><strong>Prototype data notice:</strong> {summary.message}</span><span className="notice-tag">DEMO MODE</span></div>
      <section className="metrics-grid"><Metric label="Monitored locations" value={summary.monitored_locations} detail="Locations in current dataset" icon={MapPinned}/><Metric label="Water bodies" value={summary.water_bodies} detail="Demo records available" icon={Waves}/><Metric label="Needs review" value={summary.locations_requiring_review} detail="Illustrative triage count" icon={AlertTriangle}/><Metric label="Water quality" value="Not assessed" detail="Laboratory data not connected" icon={FlaskConical}/></section>
      <div className="section-heading" id="water-bodies"><div><div className="eyebrow">GEOSPATIAL MONITORING</div><h3>Water-body watchlist</h3></div><span className="muted-count">{waterBodies.length} locations</span></div>
      <section className="water-grid">{waterBodies.map(body=><article className="water-card" key={body.id}><div className="water-visual"><div className="contour contour-a"/><div className="contour contour-b"/><div className="water-pin"><Waves size={22}/></div><span className="visual-caption">SATELLITE / FIELD RECORD</span></div><div className="water-card-body"><div className="water-title"><div><h4>{body.name}</h4><p>{body.district} district · {body.observation_date}</p></div><span className="demo-chip">DEMO</span></div><div className="water-stats"><div><small>Extent change</small><strong>{body.water_extent_change_pct===null?"—":`${body.water_extent_change_pct>0?"+":""}${body.water_extent_change_pct}%`}</strong></div><div><small>NDWI proxy</small><strong>{body.ndwi??"—"}</strong></div><div><small>Quality</small><strong>Unassessed</strong></div></div><p className="water-note">{body.notes}</p></div></article>)}</section>
      <section className="insight-grid" id="quantity">
        <article className="insight-card"><div className="insight-icon blue"><Droplets size={20}/></div><div><h3>Water quantity intelligence</h3><p>Next: ingest observation-well data, rainfall, terrain and satellite indicators. Validate groundwater forecasts against held-out monitoring wells.</p><span className="coming-label">DATA PIPELINE PENDING</span></div></article>
        <article className="insight-card" id="quality"><div className="insight-icon green"><FlaskConical size={20}/></div><div><h3>Water quality intelligence</h3><p>Next: connect laboratory measurements for pH, TDS, DO, BOD, nitrate and metals. Remote sensing alone cannot certify water safety.</p><span className="coming-label">LAB DATA PENDING</span></div></article>
        <article className="insight-card" id="satellite"><div className="insight-icon gold"><Satellite size={20}/></div><div><h3>Satellite change detection</h3><p>Next: cloud-mask Sentinel-2 imagery and compare season-matched water extent and vegetation indices.</p><span className="coming-label">EARTH ENGINE INTEGRATION PENDING</span></div></article>
        <article className="insight-card" id="actions"><div className="insight-icon purple"><Leaf size={20}/></div><div><h3>Explainable action center</h3><p>Every future alert will include source observations, date, confidence, limitations and recommended field verification.</p><span className="coming-label">BASELINE RULES ONLY</span></div></article>
      </section>
      <footer>JalDrishti AI · Prototype v0.1 · Not an official water-quality certification or emergency advisory.</footer>
    </section>
  </main>;
}
