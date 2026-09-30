from __future__ import annotations

from pathlib import Path


def ensure_directories() -> None:
    root = Path(__file__).resolve().parents[1]
    for directory in [
        root / "data",
        root / "output",
        root / "config",
        root / "logs",
    ]:
        directory.mkdir(exist_ok=True, parents=True)


if __name__ == "__main__":
    ensure_directories()
    print("Project directories created successfully.")
