# Analysis notebook sequence

1. `01_data_inventory.ipynb` — source inventory, schema, coverage, missingness, units, provenance.
2. `02_groundwater_eda.ipynb` — well trends, seasonality, quality checks.
3. `03_water_quality_eda.ipynb` — station/sample cleaning and parameter distributions.
4. `04_satellite_water_extent.ipynb` — cloud-masked Sentinel-2 water masks, season-matched change.
5. `05_model_training.ipynb` — leakage-safe baselines and spatiotemporal evaluation.
6. `06_explainability_and_uncertainty.ipynb` — feature attributions, calibration and uncertainty.

Do not train models until targets, units, observation dates and data provenance have been audited.
