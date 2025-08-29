\# Stakeholder Summary — Revenue–Risk Predictive Model



\## Executive Summary

We built a predictive model to assess the relationship between bank revenues and market risk.  

Findings confirm a strong correlation (R² ≈ 0.92), but forecasts should be treated as \*\*ranges\*\* rather than exact predictions, given sensitivity to market conditions.





\## Key Insights

\- \*\*Strong Revenue–Risk Link:\*\* Revenues and market risk indices move closely together.

\- \*\*Stable Baseline Model:\*\* Regression achieved R² ≈ 0.92; bootstrap confirmed reliability.

\- \*\*Sensitivity to Outliers:\*\* Moderate outlier removal improves stability; excessive filtering reduces robustness.

\- \*\*Directional Prediction:\*\* Time-series classification provides useful signals on risk direction.





\## Assumptions and Risks

\- \*\*Assumptions:\*\* Data quality remains consistent; past patterns extend into near-term forecasts.  

\- \*\*Risks:\*\*  

&nbsp; - Data delays or schema drift (APIs, financials)  

&nbsp; - Model instability in crisis/regime shift periods  

&nbsp; - Misinterpretation of forecasts as precise values  





\## Implications for Decision Makers

\- Use outputs as \*\*scenario guidance\*\* (ranges, not single numbers).  

\- Model is best suited as a \*\*decision-support tool\*\*, not for standalone forecasting.  

\- Regular monitoring of data quality and model drift is critical before operational use.  



Khushi Khanna, MFE



