# JalDrishti AI

**Seeing Water Clearly. Protecting Every Drop.**

JalDrishti AI is a geospatial environmental decision-support platform combining water-quantity intelligence, water-quality monitoring, satellite-derived indicators, forecasting and explainable action recommendations.

> **Scientific guardrail:** satellite observations are proxies for surface-water/environmental conditions. They do not directly measure groundwater depth or establish drinking-water safety. Groundwater forecasts must be trained and validated against monitoring-well observations; water-safety decisions require laboratory/field measurements.

## Current project status

This repository contains the initial application scaffold:
- FastAPI backend with health, dashboard, water-body and risk endpoints.
- React + TypeScript + Vite frontend scaffold.
- A transparent, rule-based vulnerability scoring baseline, clearly labelled as illustrative until real data is connected.
- Data contracts, source register and notebooks roadmap.

No real measurements or model performance are fabricated. The dashboard starts with clearly labelled demo records.

## Architecture

```text
JalDrishti-AI/
├── backend/                 FastAPI API and baseline risk service
├── frontend/                React + TypeScript + Vite UI
├── data/
│   ├── raw/                 Keep downloaded source data out of Git
│   ├── processed/
│   └── sample/              Small, explicitly synthetic demo fixtures
├── docs/                    Data dictionary, sources and methodology
├── ml/                      Future model training and evaluation
├── notebooks/               Analysis workflow
└── .gitignore
```

## Quick start

### Backend

Python 3.11+ recommended.

```bash
cd backend
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000  
Swagger: http://127.0.0.1:8000/docs

### Frontend

Use Node.js 20+.

```bash
cd frontend
npm install
npm run dev
```

Vite normally serves the UI at http://localhost:5173. The frontend uses `VITE_API_BASE_URL` (defaults to `http://localhost:8000/api/v1`).

## Environment variables

Backend:
- `CORS_ORIGINS`: comma-separated allowed browser origins; defaults to localhost Vite ports.
- `JALDRISHTI_ENV`: `development` or `production`.

Frontend:
- Copy `.env.example` to `.env` and set `VITE_API_BASE_URL` if needed.

Never commit credentials, API keys, private datasets or personally identifiable information.

## Data plan

See [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) and [docs/METHODOLOGY.md](docs/METHODOLOGY.md). Prioritize official observations from CGWB/India-WRIS for groundwater and CPCB/MPPCB for water quality, supplemented by satellite-derived indicators (e.g. Sentinel-2) and rainfall products (e.g. CHIRPS/IMD). Check licensing, temporal coverage, spatial resolution, units and missingness before model training.

## Planned development sequence

1. Pilot district selection and source/data audit.
2. Geospatial normalization and exploratory analysis.
3. Baseline groundwater and water-quality models using measured labels.
4. Satellite water extent/vegetation change analysis.
5. Time-aware validation, uncertainty and explainability.
6. Connect verified outputs to the dashboard and build intervention workflows.

## License

No license has been selected yet. Until a license is added, reuse permissions are not granted by default.
