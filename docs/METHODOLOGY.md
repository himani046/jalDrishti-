# Methodology and scientific safeguards

## 1. Separate quantity from quality
Maintain two independent evidence streams:
- **Quantity:** monitored groundwater levels, rainfall, surface-water extent, land cover, terrain and defensible demand proxies.
- **Quality:** laboratory/field parameters linked to sampling station and date.

Do not interpret an unassessed quality dimension as safe or clean.

## 2. Satellite processing
Candidate Sentinel-2 Level-2A workflow:
1. Filter by region and time window.
2. Mask clouds and cloud shadows using scene classification / cloud probability.
3. Calculate NDWI and MNDWI for surface-water mapping; calculate vegetation/moisture indicators with documented formulas.
4. Aggregate water extent over seasonally comparable windows.
5. Validate water masks against reference labels or authoritative inventories.
6. Store product ID, acquisition date, cloud mask and processing details.

Index values are indicators, not direct measurements of groundwater level or all pollution parameters.

## 3. Groundwater model
- Target: observed groundwater depth from a monitoring well, with units and measurement convention documented.
- Features: historical well observations, rainfall lags, season, terrain/geology where available, land cover and satellite covariates.
- Split by time and, where possible, by well/location to avoid leakage.
- Baselines: persistence/seasonal baseline and regularized regression; compare with Random Forest and gradient boosting.
- Report MAE/RMSE, bias, uncertainty intervals and performance by season/region.
- Do not extrapolate confidently outside training coverage.

## 4. Water-quality model
- Train only on measured samples with parameter units and station/time metadata.
- Handle each parameter separately where standards and units differ.
- Report calibration, class balance, confusion matrix and temporal/spatial validation.
- Avoid leakage from repeated samples at the same station across random train/test splits.
- Regulatory thresholds must be sourced from current applicable standards and shown with parameter, unit and intended use.

## 5. Vulnerability index
Keep at least three outputs: quantity stress score, quality concern score, and evidence coverage/confidence.
Only combine into a composite when both dimensions have adequate evidence and weights are justified. Missing values must remain missing, not be silently treated as zero risk.

## 6. Recommendations
Recommendations are triage suggestions, not automated regulatory or public-health decisions. High-consequence actions require field verification and appropriate authority review.
