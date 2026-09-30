from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import AppConfig, OutputEnvelope


class DataIngestor:
    def __init__(self, config: AppConfig | None = None):
        self.config = config or AppConfig()

    def normalize_record(
        self, record: dict[str, Any], source_name: str, source_type: str
    ) -> dict[str, Any]:
        return {
            "source_name": source_name,
            "source_type": source_type,
            "record": record,
            "metadata": {
                "normalized": True,
            },
        }

    def export_json(
        self,
        records: list[dict[str, Any]],
        source_name: str,
        source_type: str,
        output_path: str | Path | None = None,
    ) -> dict[str, Any]:
        payload = OutputEnvelope(
            source_name=source_name,
            source_type=source_type,
            record_count=len(records),
            records=records,
        )

        file_path = (
            Path(output_path)
            if output_path
            else self.config.output_dir / f"{source_name}.json"
        )
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(
            json.dumps(payload.model_dump(mode="json"), indent=2), encoding="utf-8"
        )

        return payload.model_dump(mode="json")

    def run(
        self,
        source_name: str,
        source_type: str,
        raw_records: list[dict[str, Any]],
        output_path: str | Path | None = None,
    ) -> dict[str, Any]:
        normalized = [
            self.normalize_record(record, source_name, source_type)
            for record in raw_records
        ]
        return self.export_json(normalized, source_name, source_type, output_path)
