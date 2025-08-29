# Revenue–Risk Predictive Model

## Project Summary
The Revenue–Risk Predictive Model investigates the relationship between bank revenues and market risk indicators.  
It was built as part of an Applied Financial Engineering Bootcamp, covering the entire lifecycle (Stages 1–16): from data acquisition and storage to modeling, evaluation, deployment, and lifecycle review.  



## Objectives
- Build a reproducible pipeline for financial data ingestion, cleaning, and storage.  
- Detect and analyze outliers and their impact on model assumptions.  
- Explore revenue vs risk dynamics using statistical summaries and visualizations.  
- Engineer lagged and rolling features to capture time-series structure.  
- Fit baseline Linear Regression and Time-Series Classification models.  
- Quantify uncertainty using bootstrap confidence intervals and scenario analysis.  
- Deliver stakeholder-ready insights with clear communication of risks and assumptions.  



## Methodology
1. **Data Acquisition:** Pulled quarterly revenue via APIs (Yahoo Finance, FMP) and scraped financial tables.  
2. **Data Processing:** Stored as CSV + Parquet, applied cleaning, imputation, and normalization.  
3. **Outlier Analysis:** Used IQR and Z-score methods; compared sensitivity of models with and without outliers.  
4. **EDA:** Generated histograms, scatterplots, and correlation heatmaps to identify key relationships.  
5. **Feature Engineering:** Created lag features, rolling averages, and ratios.  
6. **Modeling:**  
   - Linear Regression — explained variance (R² ≈ 0.92).  
   - Time-Series Classification — predicted up/down movement in risk index.  
7. **Evaluation:** Bootstrap resampling (500 runs), scenario comparisons, and subgroup diagnostics.  
8. **Reporting:** Stakeholder summary with polished charts and a clear “what this means for you.”  
9. **Deployment & Monitoring:** Reflection on data, model, system, and business risks; metrics for monitoring (e.g., null <2%, rolling AUC >0.6).  
10. **Orchestration & Review:** Documented pipeline dependencies (DAG), logging strategy, and lifecycle reflections.  


## Key Results
- Revenue and risk are strongly correlated (R² ≈ 0.92).  
- Model RMSE remained stable under bootstrap resampling.  
- Sensitivity analysis showed the model is robust under IQR outlier filtering but weaker under strict Z-score thresholds.  
- Forecasts are most reliable when communicated as ranges rather than exact point predictions.  


## Risks and Assumptions
- **Data Risks:** Missing or delayed quarterly financials; schema drift.  
- **Model Risks:** Market regime shifts (e.g., crises) that break linear assumptions.  
- **System Risks:** API downtime, latency beyond acceptable thresholds, spikes in null values.  
- **Business Risks:** Misinterpretation of forecasts; overconfidence in a single model.  



## Conclusion
This project successfully demonstrates an end-to-end predictive modeling workflow in financial engineering.  
From ingestion and preprocessing to modeling, evaluation, and reporting, the pipeline is reproducible, documented, and stakeholder-ready.  
It highlights both the potential and the limitations of using linear and time-series models to connect revenue with market risk, emphasizing the importance of uncertainty quantification and assumption-aware communication.  



Author: Khushi Khanna, MFE
