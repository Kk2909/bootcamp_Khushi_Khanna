# Stage 13 — Productization

**Included**
- Pickled model: `model/model.pkl` (+ `model/metadata.json`)
- Flask API: `src/app.py` with `/health`, `POST /predict`, `GET /predict/<x1>[/<x2>]`, `/plot`
- `requirements.txt`
- Pred vs Actual image: `artifacts/images/pred_vs_actual.png`

**Run**
1. `pip install -r requirements.txt`
2. `python src/app.py` → http://127.0.0.1:8000
