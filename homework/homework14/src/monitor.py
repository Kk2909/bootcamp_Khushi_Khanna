import time, csv, requests, os
from datetime import datetime

BASE = os.environ.get("API_BASE","http://127.0.0.1:8000")
OUT  = os.environ.get("MONITOR_LOG","docs/monitor_log.csv")
INTERVAL = float(os.environ.get("MONITOR_INTERVAL","10"))

print(f"[monitor] polling {BASE}/health every {INTERVAL}s -> {OUT}")
with open(OUT, "a", newline="") as f:
    w = csv.writer(f)
    if f.tell() == 0:
        w.writerow(["ts","ok","latency_ms"])
    while True:
        t0 = time.perf_counter()
        ok = False
        try:
            r = requests.get(f"{BASE}/health", timeout=5)
            ok = (r.status_code == 200)
        except Exception:
            ok = False
        dt_ms = int((time.perf_counter()-t0)*1000)
        w.writerow([datetime.utcnow().isoformat()+"Z", int(ok), dt_ms]); f.flush()
        time.sleep(INTERVAL)
