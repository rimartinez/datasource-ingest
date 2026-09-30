from __future__ import annotations

from datasource_ingest.core import DataIngestor


def main() -> None:
    sample_records = [
        {"id": "A-001", "name": "Alice Johnson", "email": "alice@example.com"},
        {"id": "A-002", "name": "Bob Smith", "email": "bob@example.com"},
    ]

    ingestor = DataIngestor()
    result = ingestor.run("demo_source", "csv", sample_records)
    print(result)


if __name__ == "__main__":
    main()
