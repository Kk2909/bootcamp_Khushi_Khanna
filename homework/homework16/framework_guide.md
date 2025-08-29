\# Framework guide 



| Lifecycle Stage | What You Did | Challenges | Decisions / Solutions | Future Improvements |

|---|---|---|---|---|

| 1. Problem Framing | Framed a revenue ↔ risk relationship; goal: explain/forecast with uncertainty. | Causality vs correlation; quarterly small-N. | Treat as decision support; keep scope simple. | Add macro \& credit spread factors; define action thresholds. |

| 2. Tooling Setup | Python + pandas/sklearn; Git repo with folders. | Env/.env path confusion. | Standardized layout; .gitignore for secrets. | Pin requirements; add pre-commit (format/lint). |

| 3. Python Fundamentals | Modular helpers for IO/plots; seeded randomness. | Dtype/date parsing edge cases. | Assert checks and converters. | Unit tests for IO contracts. |

| 4. Data Ingestion | Pulled API + scraped table; saved to `data/raw/` with timestamps. | Missing quarters; schema drift. | Validate required cols/NA counts; raw snapshots. | Retries, schema hash, source notes. |

| 5. Data Storage | CSV in raw; Parquet in processed; simple read/write utils. | Format consistency. | Env-driven paths; suffix-routed IO. | Data catalog; `.env.example`. |

| 6. Preprocessing | Imputation/normalization; saved cleaned file. | Impute vs signal distortion. | Compare before/after; document rules. | Robust scalers; missingness sensitivity. |

| 7. Outliers | IQR/Z-score flags; sensitivity with/without outliers. | Shock vs bad data. | Keep plausible shocks; cap obvious errors. | Try winsorizing; robust models. |

| 8. EDA | Distributions, relationships, seasonal checks. | Low power (quarterly). | Focus on effect sizes \& trends. | Add macro overlays. |

| 9. Feature Eng. | Lags, rolling stats, simple ratios/momentum. | Leakage \& alignment. | Past-only windows; index checks. | Regime/interaction features. |

| 10. Modeling | Baseline Linear Regression; optional TS/classifier. | Heteroskedastic residuals; regime shifts. | Keep simple baseline; diagnose residuals. | Regularization; ARIMAX/GB as next step. |

| 11. Evaluation \& Risk | RMSE/R²; bootstrap CI; scenario compare. | Communicating uncertainty. | Plain-language “holds if / sensitive to” notes. | PSI/drift checks; subgroup error. |

| 12. Reporting | 2–3 key charts + takeaways; sensitivity summary. | Avoid overclaiming. | Decision-oriented bullets; assumptions called out. | Reusable one-pager template. |

| 13. Productization | Repo clean-up; persisted `model.pkl`; minimal API sketch. | Reuse vs speed. | Move reusable code to `src/`; run notes. | CLI entry points; `requirements.txt`. |

| 14. Deployment \& Mon. | Reflection on risks + Data/Model/System/Business metrics. | Choosing pragmatic metrics. | Freshness, null rate, rolling error, p95 latency, 1–2 KPIs. | Drift alerts; retrain triggers. |

| 15. Orchestration | DAG plan: ingest → clean → fe → model → evaluate; logs \& `.ok` checkpoints. | Idempotency/paths. | Timestamped outputs; `--force/--recompute`. | Add `run\_all` and (later) a scheduler. |

| 16. Lifecycle Review | This guide + repo polish; linked decisions across stages. | Summarizing succinctly. | Keep emphasis on uncertainty \& scope. | Add more data \& risk factors; regularized models with monitoring. |



\*\*Short reflections\*\*

\- Hardest: small quarterly sample → solved by focusing on uncertainty \& sensitivity.  

\- Most rewarding: clean, reproducible pipeline with clear stakeholder notes.  

\- Connections: storage/cleaning choices constrained features; orchestration made later steps repeatable.

