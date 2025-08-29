# Homework 11 — Evaluation & Risk Communication

**Summary**
- RMSE = 3115.86, MAE = 2449.54, R² = 0.001
- Bootstrap RMSE 95% CI: [2550.71, 3653.39] (B=1200)
- Scenarios compared (mean vs median imputation). See: `artifacts/metrics/scenario_compare.csv`

**Diagnostics**
- See `artifacts/plots/`: `pred_vs_actual.png`, `residuals_vs_pred.png`, `residual_hist.png`
- If available: `rmse_by_risk_quintile.png`, `rmse_by_rev_size.png`
- (Optional) `backtest_rmse_over_time.png`

**Assumptions & Risks**
- Assumes data distribution similar to training; sensitive to extreme volatility/missing-rate > 10%.
- Misuse risk: treat predictions as ranges, not exact points.

**Go/No-Go (example)**
- RMSE ≤ target; 95% empirical PI coverage ≥ 90%;
- No subgroup RMSE > 1.5× overall; no sustained degradation in backtest.

**Artifacts**
- Metrics JSON: `artifacts/metrics/eval_summary.json`
- Scenario table: `artifacts/metrics/scenario_compare.csv`
- Plots: `artifacts/plots/*.png`
