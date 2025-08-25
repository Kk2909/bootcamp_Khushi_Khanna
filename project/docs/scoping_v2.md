# Revenue Prediction vs Risk — v2

**Problem.** Predict quarterly IB revenues for a 5‑bank peer set using VaR as the baseline driver, extending with finance‑relevant features. Use 5 years of history; normalize across peers for comparability.

**Stakeholder & Use.** Finance leadership & risk: plans, what‑ifs, variance tracking vs actuals.

**Useful Answer.** Predictive regression (start OLS). y = revenue_total. Baseline x = var. Iterate features. Report MAE/MAPE/R² and error‑by‑bank. Provide normalized comparisons & residuals.

**Assumptions.** Comparable VaR/proxies available; quarterly frequency; per‑bank normalization; limited regime breaks.

**Risks.** Data gaps/definitions, non‑linearity, structural shifts. We’ll monitor via backtests, error‑by‑bank, sensitivity.

**Deliverables.** Clean dataset, EDA, feature set, baseline + variants, evaluation, write‑up.
