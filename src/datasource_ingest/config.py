from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


@dataclass
class AppConfig:
    project_root: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2])
    input_dir: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2] / "data")
    output_dir: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2] / "output")
    source_config_path: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2] / "config" / "sources.yaml")


class SourceRecord(BaseModel):
    source_name: str
    record_id: str | None = None
    source_type: str
    raw_data: dict[str, Any] = Field(default_factory=dict)
    normalized_data: dict[str, Any] = Field(default_factory=dict)


class OutputEnvelope(BaseModel):
    source_name: str
    source_type: str
    record_count: int = 0
    records: list[dict[str, Any]] = Field(default_factory=list)
