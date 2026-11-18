# API overview

Base path: `/api/v1`

| Method | Route | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/dashboard/summary` | Prototype summary counters |
| GET | `/water-bodies` | List current fixtures; optional `district` filter |
| GET | `/water-bodies/{id}` | Get one water-body record |
| GET | `/risk/{location_id}` | Transparent demo risk assessment |

FastAPI OpenAPI docs: `/docs`.
