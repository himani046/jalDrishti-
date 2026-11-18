# Data source register

This is a research checklist, not a claim that data has been downloaded or integrated. Confirm availability, terms, schema, units, coverage and update frequency before use.

| Domain | Candidate source | Intended use | Validation required |
|---|---|---|---|
| Groundwater | Central Ground Water Board (CGWB) | Observation-well depth and seasonal trends | Station metadata, dates, units, aquifer, missingness |
| Water resources | India-WRIS | Water assets and monitoring context | Access method, licensing, spatial identifiers |
| Surface-water quality | CPCB / MPPCB / NWMP | Lab/field pH, DO, BOD, COD, TDS, metals | Units, method, station/date, detection limits |
| Satellite | Sentinel-2 Level-2A | Water extent and spectral indicators | Cloud masking, season matching, resolution |
| Rainfall | IMD gridded rainfall / CHIRPS | Precipitation history and anomalies | Resolution, bias, aggregation |
| Terrain | SRTM / Copernicus DEM | Elevation, slope and terrain covariates | Resolution and datum |
| Boundaries | Authoritative government products | District/block/village joins | Boundary vintage and licensing |

## Rules
1. Never replace missing measured targets with synthetic values.
2. Retain provenance: provider, product, station/pixel, date, units, processing version and retrieval date.
3. Keep raw data immutable and out of Git when large or restricted.
4. Distinguish measured data, satellite proxies, model estimates and demo fixtures.
5. Check licensing and attribution before redistribution.
6. Sentinel-2 does not directly observe groundwater depth.
7. Satellite reflectance cannot certify potable water or reliably detect all dissolved contaminants/pathogens.
