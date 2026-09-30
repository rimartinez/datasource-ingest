# Data Source Ingest

A Python project template for collecting information from multiple source types and normalizing it into JSON for model training or downstream processing.

## Included sources

- CRM-style APIs or exports
- SQL databases
- CSV and Excel files
- Email exports or message dumps

## Goals

- Standardize source-specific data into a single JSON schema
- Support local development and Git-based collaboration
- Keep the project easy to clone and continue on other machines

## Quick start

1. Create a virtual environment
2. Install dependencies
3. Run the sample pipeline

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m datasource_ingest
```

## Project structure

- `src/` - application source code
- `tests/` - test suite
- `examples/` - sample inputs and outputs
- `config/` - environment configuration and source definitions
- `scripts/` - operational helpers

## Notes

This is a starter project designed for future expansion. The core idea is to create adapters for each source, normalize their data, and emit a standardized JSON payload.
