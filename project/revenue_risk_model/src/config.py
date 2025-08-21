# src/config.py
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Project root = the folder that CONTAINS src/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_env(dotenv_path: str | None = None) -> None:
    path = dotenv_path or find_dotenv(usecwd=True)
    load_dotenv(path, override=False)

def get_key(name: str, default: str | None = None, required: bool = False) -> str | None:
    val = os.getenv(name, default)
    if required and val is None:
        raise KeyError(f"Missing required environment variable: {name}")
    return val

def _resolve_from_root(rel: str) -> Path:
    p = Path(rel)
    return p if p.is_absolute() else (PROJECT_ROOT / p)

def data_dir(kind: str = "root") -> str:
    load_env()
    base = _resolve_from_root(get_key("DATA_DIR", "data"))
    if kind == "raw":
        raw = get_key("DATA_DIR_RAW", None)
        return str(_resolve_from_root(raw) if raw else (base / "raw"))
    if kind == "processed":
        proc = get_key("DATA_DIR_PROCESSED", None)
        return str(_resolve_from_root(proc) if proc else (base / "processed"))
    return str(base)

