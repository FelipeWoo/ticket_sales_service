# Sales & Consumption Ticket

## Overview

Handles point-of-sale logic, invoice generation, and customer receipts.  
Implements immutable, auditable ticket storage using SQLite and generates PDF exports with only public-facing fields.  
Supports raw SQL filtering, structured field validation, and an append-only logic.

---

## Category

Sales & Consumption

---

## Running the Project

```bash
make run
````

This command will execute the main program. Make sure your `.env` file and SQLite schema are initialized.

---

## Testing

```bash
make test
make cov
```

* `make test`: Runs all unit tests using `pytest`
* `make cov`: Runs tests with coverage report

---

## Linting and Formatting

```bash
make lint
make ty
make check
```

* `make lint`: Lint using `ruff`
* `make ty`: Static typing check using `pyright` or `mypy`
* `make check`: Runs all code quality checks

---

## Project Structure

```text
ticket_sales_service/
├── .private/             # Internal credentials, secrets (excluded from Git)
├── .venv/                # Virtual environment
├── docs/                 # Project documentation (logic, specs, stages)
├── exports/              # PDF exports (public-only ticket representations)
├── logs/                 # Application log files
│
├── src/                  # Main source code
│   ├── db/               # Database connection and schema
│   ├── models/           # Ticket data models
│   ├── services/         # Business logic (create, read, export)
│   └── utils/            # Shared utilities (logging, boot, validators)
│
├── tests/                # All test cases with pytest
├── scripts/              # Notebooks, importers, and helper scripts
├── Makefile              # Project commands and automation
├── .env                  # Environment configuration
├── .gitignore            # Git ignore rules
├── pyproject.toml        # Build and tool configuration
├── requirements.txt      # Python dependencies (for pip)
├── uv.lock               # Dependency lock for uv
└── README.md             # Project overview and usage
```

---

## Development Roadmap

The project follows a staged development plan outlined in:

```
docs/stages.md
```

Each stage includes testing activities, features, and commit messages. For full system design and logic, see:

* `docs/specs.md`
* `docs/logic.md`
* `docs/workflow.md`

---

## License

This project is licensed under the terms of the LICENSE file.
