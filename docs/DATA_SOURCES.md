# Data source register

This is a research checklist, not a claim that data has already been downloaded or integrated. Confirm current availability, terms of use, schema, units, coverage and update frequency from the provider before use.

| Domain | Candidate source | Intended use | Validation required |
|---|---|---|---|
| Groundwater quantity | Central Ground Water Board (CGWB) | Observation-well depth and seasonal trends | Station metadata, dates, depth units, aquifer and missingness |
| Water resources | India-WRIS | Water-resource assets and monitoring context | Access method, licensing and spatial identifiers |
| Surface-water quality | CPCB / MPPCB / NWMP | Lab/field measurements such as pH, DO, BOD, COD, TDS and metals | Parameter units, method, station/date and detection limits |
| Satellite | Sentinel-2 Level-2A | Water extent and spectral indicators | Cloud masking, season matching and spatial resolution |
| Rainfall | IMD gridded rainfall / CHIRPS | Precipitation history and anomalies | Resolution, bias and time aggregation |
| Terrain | SRTM or Copernicus DEM | Elevation, slope and terrain covariates | Resolution and datum |
| Administrative boundaries | Authoritative government boundary products | District/block/village joins | Boundary vintage and licensing |

## Important rules
1. Never replace a missing measured value with a synthetic value in the training target.
2. Retain provenance: provider, dataset/product, station or pixel, date, units, processing version and retrieval date.
3. Keep raw data immutable and out of Git when large or restricted.
4. Distinguish measured field/lab data, satellite-derived proxies, model estimates and demo fixtures.
5. Check data licensing and attribution requirements before redistributing.
6. Groundwater depth is not directly observed by Sentinel-2; satellite products are indirect covariates only.
7. Satellite reflectance cannot certify potable water or reliably detect all dissolved contaminants/pathogens.
