from datasource_ingest.core import DataIngestor


def test_run_generates_json_payload():
    ingestor = DataIngestor()
    result = ingestor.run(
        "demo_source",
        "csv",
        [{"id": "A-001", "name": "Alice Johnson"}],
    )

    assert result["source_name"] == "demo_source"
    assert result["source_type"] == "csv"
    assert result["record_count"] == 1
    assert result["records"][0]["record"]["name"] == "Alice Johnson"
