import io, json
from pathlib import Path

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, send_file
import joblib
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parents[1]
MODEL_PATH = HERE / "model" / "model.pkl"
META_PATH  = HERE / "model" / "metadata.json"
ART_IMG    = HERE / "artifacts" / "images" / "pred_vs_actual.png"

app = Flask(__name__)

# Load model & metadata once
model = joblib.load(MODEL_PATH)
meta  = json.loads(META_PATH.read_text(encoding="utf-8"))
FEATURES = meta.get("feature_names", [])

def _coerce_df(payload):
    """Accept dict or list-of-dicts; coerce to DataFrame with model feature columns."""
    if isinstance(payload, dict):
        df = pd.DataFrame([payload])
    elif isinstance(payload, list):
        df = pd.DataFrame(payload)
    else:
        raise ValueError("Payload must be an object or list of objects")
    # ensure expected columns exist and are ordered; imputer will handle NaN
    for c in FEATURES:
        if c not in df.columns:
            df[c] = np.nan
    df = df[FEATURES]
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

@app.get("/health")
def health():
    return jsonify(status="ok", model=str(MODEL_PATH.name), features=FEATURES, target=meta.get("target"))

@app.post("/predict")
def predict_post():
    try:
        payload = request.get_json(force=True, silent=False)
        if isinstance(payload, dict) and "records" in payload:
            df = _coerce_df(payload["records"])
        else:
            df = _coerce_df(payload)  # support single record or list
        preds = model.predict(df).tolist()
        return jsonify(predictions=preds, n=len(preds))
    except Exception as e:
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
        return jsonify(error=str(e)), 400

@app.get("/plot")
def plot_png():
    if ART_IMG.exists():
        return send_file(ART_IMG, mimetype="image/png")
    buf = io.BytesIO()
    xs = np.linspace(0, 10, 100); ys = xs + np.random.normal(0, 1, 100)
    plt.figure(); plt.scatter(xs, ys, s=16, alpha=0.7)
    plt.plot([0,10],[0,10], "--"); plt.tight_layout()
    plt.savefig(buf, format="png", dpi=144); plt.close(); buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
