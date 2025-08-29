\# Homework 10  Modeling



This homework combines \*\*Stage 10a (Linear Regression)\*\* and \*\*Stage 10b (Time Series / Classification)\*\* in one notebook.



---



\## Folder Structure

\- `data/raw/` → synthetic datasets created for homework  

\- `data/processed/` → any cleaned/derived outputs  

\- `notebooks/` → main notebook: `stage10\_modeling\_homework.ipynb`  

\- `src/` → reusable functions if needed  

\- `README.md` → this summary  



---



\## Stage 10a: Linear Regression

\- \*\*Dataset:\*\* Synthetic, 400 rows, predictors `x1`, `x2`, target `y`.  

\- \*\*Results:\*\*  

&nbsp; - R² ≈ 0.978  

&nbsp; - RMSE ≈ 1.8  

\- \*\*Residuals Check:\*\*  

&nbsp; - Linearity → good (no curve)  

&nbsp; - Independence → no visible pattern  

&nbsp; - Homoscedasticity → spread roughly constant  

&nbsp; - Normality → histogram bell-shaped, QQ plot ~ straight line  



\*\*Conclusion:\*\* Model fits the synthetic data well.





\## Risks \& Assumptions

\- Synthetic data = idealized; real-world may not satisfy assumptions.  

\- Random seed fixed for reproducibility.  



