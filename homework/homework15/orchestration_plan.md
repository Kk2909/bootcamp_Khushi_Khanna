\# Stage 15 — Orchestration \& System Design (Revenue–Risk)



\## 1) Jobs / Tasks

\- ingest\_api

\- scrape\_aux

\- clean\_preprocess

\- feature\_engineer

\- model\_fit

\- evaluate\_report



\## 2) Dependencies (DAG)

ingest\_api ─┐

&nbsp;           ├─> clean\_preprocess → feature\_engineer → model\_fit → evaluate\_report

scrape\_aux ─┘



\## 3) For each task: Inputs / Outputs / Idempotency / Logging / Checkpoints

| Task | Inputs | Outputs | Idempotent? | Logging | Checkpoint |

|---|---|---|---|---|---|

| ingest\_api | .env (if used), params | data/raw/api\_<src>\_<ticker>\_<ts>.csv | Yes | logs/ingest.log | checkpoints/ingest\_<ts>.ok |

| scrape\_aux | URL | data/raw/scrape\_<site>\_<table>\_<ts>.csv | Yes | logs/scrape.log | checkpoints/scrape\_<ts>.ok |

| clean\_preprocess | raw CSVs | data/processed/cleaned\_<ts>.parquet | Yes | logs/clean.log | checkpoints/cleaned\_<ts>.ok |

| feature\_engineer | cleaned | data/processed/fe\_<ts>.parquet | Yes | logs/fe.log | checkpoints/fe\_<ts>.ok |

| model\_fit | engineered | model/model.pkl; reports/metrics.json | Yes\* (`--force` to overwrite) | logs/model.log | checkpoints/model\_<ts>.ok |

| evaluate\_report | model + data | reports/figures/\*; deliverables/\* | Yes | logs/eval.log | checkpoints/eval\_<ts>.ok |



\## 4) Reliability (Logging • Retries • Failure Modes)

\- Logging: Python `logging` INFO to console + per-task log file.

\- Retries: network/API 3× (1s, 3s, 9s); scrape 2× with User-Agent.

\- Fail fast: missing ENV key, schema drift (col diff), empty file ⇒ fix upstream and re-run.



\## 5) What to automate now vs keep manual (with rationale)

\- Automate now: ingest\_api, clean\_preprocess, model\_fit (simple CLI wrappers).

\- Keep manual: full scheduler/Airflow/Prefect (out of scope for homework right now).



\## 6) Runbook (local examples)

python -m src.orch.ingest\_step --ticker JPM --source yf

python -m src.orch.clean\_step  --input data/raw/<latest>.csv

python -m src.orch.fe\_step     --input data/processed/cleaned\_\*.parquet

python -m src.orch.model\_step  --data  data/processed/fe\_\*.parquet

python -m src.orch.eval\_step   --model model/model.pkl




