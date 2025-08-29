import time, io, json, logging
from pathlib import Path

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, send_file, Response
import joblib

# Prometheus metrics
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

HERE = Path(__file__).resolve().parents[1]
MODEL_PATH = HERE / "model" / "model.pkl"
META_PATH  = HERE / "model" / "metadata.json"

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("app")

# Load model & metadata
model = joblib.load(MODEL_PATH)
meta  = json.loads(META_PATH.read_text(encoding="utf-8")) if META_PATH.exists() else {}
FEATURES = meta.get("feature_names", [])

# Metrics
REQ_COUNT   = Counter("api_requests_total", "Total API requests", ["endpoint","method","code"])
REQ_LATENCY = Histogram("api_request_latency_seconds", "Request latency", ["endpoint"])
MODEL_READY = Gauge("model_ready", "Model readiness (1 ready, 0 not)")

# App
app = Flask(__name__)
MODEL_READY.set(1.0 if model is not None else 0.0)

def _coerce_df(payload):
    if isinstance(payload, dict):
        df = pd.DataFrame([payload])
    elif isinstance(payload, list):
        df = pd.DataFrame(payload)
    else:
        raise ValueError("Payload must be an object or list of objects")
    # ensure expected columns exist and are ordered; imputer handles NaN
    if not FEATURES:
        raise ValueError("FEATURES list is empty; check metadata.json")
    for c in FEATURES:
        if c not in df.columns:
            df[c] = np.nan
    df = df[FEATURES]
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

@app.before_request
def _start_timer():
    request._start_time = time.perf_counter()

@app.after_request
def _record_metrics(resp):
    try:
        dt = time.perf_counter() - getattr(request, "_start_time", time.perf_counter())
        REQ_LATENCY.labels(request.path).observe(dt)
        REQ_COUNT.labels(request.path, request.method, resp.status_code).inc()
    except Exception:
        pass
    return resp

@app.get("/health")
def health():
    return jsonify(status="ok", model=str(MODEL_PATH.name), features=FEATURES, target=meta.get("target"))

@app.get("/ready")
def ready():
    try:
        # try a dummy predict with NaNs -> imputer path
        if not FEATURES: 
            return jsonify(ready=False, reason="no FEATURES"), 500
        row = {c: np.nan for c in FEATURES}
        df = _coerce_df(row)
        _ = model.predict(df)
        return jsonify(ready=True)
    except Exception as e:
        return jsonify(ready=False, error=str(e)), 500

@app.post("/predict")
def predict_post():
    try:
        payload = request.get_json(force=True, silent=False)
        if isinstance(payload, dict) and "records" in payload:
            df = _coerce_df(payload["records"])
        else:
            df = _coerce_df(payload)
        preds = model.predict(df).tolist()
        return jsonify(predictions=preds, n=len(preds))
    except Exception as e:
        log.exception("predict error")
        return jsonify(error=str(e)), 400

@app.get("/predict/<x1>")
@app.get("/predict/<x1>/<x2>")
def predict_path(x1, x2=None):
    try:
        if not FEATURES:
            return jsonify(error="Model feature list is empty"), 400
        row = {FEATURES[0]: float(x1)}
        if x2 is not None and len(FEATURES) > 1:
            row[FEATURES[1]] = float(x2)
        df = _coerce_df(row)
        pred = float(model.predict(df)[0])
        return jsonify(prediction=pred)
    except Exception as e:
        log.exception("predict_path error")
        return jsonify(error=str(e)), 400

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    # Windows-friendly local run (waitress); Dockerfile uses gunicorn
    try:
        from waitress import serve
        serve(app, host="127.0.0.1", port=8000)
    except Exception:
        app.run(host="127.0.0.1", port=8000, debug=False)
