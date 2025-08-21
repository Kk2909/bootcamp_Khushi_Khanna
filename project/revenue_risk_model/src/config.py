import os
from dotenv import load_dotenv, find_dotenv

def load_env(dotenv_path: str | None = None) -> None:
    path = dotenv_path or find_dotenv(usecwd=True)
    load_dotenv(path, override=False)

def get_key(name: str, default: str | None = None, required: bool = False) -> str | None:
    val = os.getenv(name, default)
    if required and val is None:
        raise KeyError(f"Missing required environment variable: {name}")
    return val

def data_dir(kind: str = "root") -> str:
    load_env()
    if kind == "raw":
        return get_key("DATA_DIR_RAW", "./data/raw", False)
    if kind == "processed":
        return get_key("DATA_DIR_PROCESSED", "./data/processed", False)
    return get_key("DATA_DIR", "./data", False)
