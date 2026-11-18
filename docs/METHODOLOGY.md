# Methodology and scientific safeguards

## 1. Separate quantity from quality
- **Quantity:** monitored groundwater levels, rainfall, surface-water extent, land cover, terrain and defensible demand proxies.
- **Quality:** laboratory/field parameters linked to sampling station and date.
Do not interpret unassessed quality as safe or clean.

## 2. Satellite processing
1. Filter Sentinel-2 Level-2A by region and time.
2. Mask clouds and shadows using scene classification/cloud probability.
3. Calculate NDWI/MNDWI for surface-water mapping, with documented formulas.
4. Aggregate extent over seasonally comparable windows.
5. Validate masks against reference labels or inventories.
6. Store product ID, acquisition date, mask and processing metadata.
Spectral indices are indicators, not direct groundwater or complete pollution measurements.

## 3. Groundwater model
- Target: observed well depth with documented units and convention.
- Features: historical well observations, rainfall lags, season, terrain/geology where available, land cover and satellite covariates.
- Split by time and, where possible, by well to avoid leakage.
- Baselines: persistence/seasonal baseline and regularized regression; compare Random Forest and gradient boosting.
- Report MAE/RMSE, bias, uncertainty and season/region-specific performance.
- Avoid confident extrapolation outside training coverage.

## 4. Water-quality model
- Train on measured samples with parameter units and station/time metadata.
- Handle each parameter separately where standards and units differ.
- Report calibration, class balance, confusion matrix and temporal/spatial validation.
- Avoid leakage from repeated station samples across random splits.
- Source current regulatory thresholds and show parameter, unit and intended use.

## 5. Vulnerability index
Keep distinct quantity stress, quality concern and evidence coverage/confidence outputs. Combine only when both dimensions have sufficient evidence and weights are justified. Missing values must remain missing, not silently become zero risk.

## 6. Recommendations
Outputs are triage suggestions, not regulatory or public-health decisions. High-consequence actions require field verification and authority review.
