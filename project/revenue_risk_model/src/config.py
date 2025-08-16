import os
from dotenv import load_dotenv

def load_env(dotenv_path: str | None = None) -> None:
    load_dotenv(dotenv_path)

def get_key(name: str, default: str | None = None, required: bool = False) -> str | None:
    val = os.getenv(name, default)
    if required and val is None:
        raise KeyError(f"Missing required environment variable: {name}")
    return val
