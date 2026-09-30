# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

Pipeline that pulls records from different kinds of sources (CRM exports or APIs, SQL databases, CSV/Excel files, email dumps), normalizes them, and writes one standard JSON output for model training or downstream processing. The project is an early template. Most of the source adapters still need to be built.

The developer works on this repo from several machines. Keep project knowledge in this file, which is committed with the repo, rather than in machine-local memory.

## Commands

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows (PowerShell); on POSIX: source .venv/bin/activate
pip install -r requirements.txt
pip install -e ".[dev]"           # editable install + pytest and ruff

python -m datasource_ingest       # run the demo pipeline (writes output/demo_source.json)
python scripts/bootstrap.py       # create data/, output/, logs/ locally (all gitignored)

pytest -q                                          # all tests
pytest tests/test_core.py::test_run_generates_json_payload   # a single test
ruff check .                      # lint (line length 100)
```

CI (`.github/workflows/ci.yml`) runs `pytest -q` on Python 3.10, 3.11 and 3.12. It installs from `requirements.txt` and runs `pip install -e .`. It does not run ruff.

## Architecture

The code uses a `src/` layout, with the package at `src/datasource_ingest/`. Pytest puts `src` on the path through `pyproject.toml`.

Data flows as: raw records (`list[dict]`) → `DataIngestor.run()` → `normalize_record()` for each record → `export_json()`. `export_json()` wraps the records in an `OutputEnvelope` and writes `output/<source_name>.json`.

- `core.py`: `DataIngestor`. `normalize_record` currently only wraps each raw record as `{source_name, source_type, record, metadata}`. `run()` returns the envelope dict and also writes it to disk, and the tests write to the real `output/` folder too.
- `config.py`: `AppConfig` (a dataclass) builds its paths from the location of the package file (`parents[2]` is the repo root), so the paths assume a source checkout. The Pydantic models are `OutputEnvelope` (the output shape) and `SourceRecord`, which nothing uses yet.
- `connectors/base.py`: `BaseConnector` is an abstract class with `fetch()` and `normalize()`. New source types (`crm`, `sql`, `csv`, `email`) should subclass it. No concrete connectors exist yet, and `DataIngestor` doesn't call connectors yet. Today callers pass raw records directly.
- `config/sources.yaml`: lists the sources (`name`, `type`, `enabled`, plus `path` or `connection_string`). **Nothing loads this file yet**, and there is no YAML library among the dependencies, so wiring it up means adding `pyyaml`.
- `.env.example`: the environment variables for CRM, SQL and SMTP credentials. Copy it to `.env`, which is gitignored and loaded with `python-dotenv`.
- `examples/`: a sample input CSV and the expected output JSON shape.

## Gotchas

- `connectors/` has no `__init__.py`. It works as an implicit namespace package in editable or source runs, but `setuptools.packages.find` skips it in a regular (non-editable) install. Add `__init__.py` when you build out connectors.
- Keep dependencies in sync by hand. `requirements.txt` and `pyproject.toml` duplicate the runtime dependencies, and `ruff` appears only in the `dev` extra.
- `data/` and `output/` are gitignored, and `examples/` is the only committed sample data.
