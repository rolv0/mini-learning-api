# Mini Learning API

A small FastAPI project for learning backend development, testing, GitHub workflows, and open source contribution.

The API lets you create and manage learning notes. It is intentionally small, but structured like a real project.

## What You Will Learn

- How a Python API project is structured
- How FastAPI routes and Pydantic models work
- How to run automated tests with pytest
- How GitHub Actions can test pull requests
- How to prepare a repository for contributors

## Features

- Health check endpoint
- List learning notes
- Filter notes by topic or status
- Create a learning note
- Update a note status
- Delete a note
- In-memory storage, so it is easy to understand

## Requirements

- Python 3.11 or newer
- Git

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements-dev.txt
```

On macOS/Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Run The API

```bash
uvicorn app.main:app --reload
```

Open:

- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Run Tests

```bash
pytest
```

## API Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/health` | Check if the API is running |
| `GET` | `/notes` | List all notes, optionally filtered by `topic` or `status` |
| `POST` | `/notes` | Create a note |
| `PATCH` | `/notes/{note_id}` | Update a note |
| `DELETE` | `/notes/{note_id}` | Delete a note |

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/notes ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"Learn FastAPI\",\"topic\":\"backend\"}"
```

On macOS/Linux:

```bash
curl -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","topic":"backend"}'
```

Filter notes by topic:

```bash
curl "http://127.0.0.1:8000/notes?topic=backend"
```

Filter notes by status:

```bash
curl "http://127.0.0.1:8000/notes?status=done"
```

## Good First Issues

These are good contribution ideas:

- Add a `priority` field to notes
- Add file-based persistence
- Add more tests for invalid input
- Improve the API documentation examples

## Deploy Ideas

This repo includes `render.yaml`, so Render is the easiest first deploy target.

1. Push this repository to GitHub.
2. Create a new Render account or log in.
3. Choose "New Web Service".
4. Connect your GitHub repository.
5. Render should detect `render.yaml`.
6. Deploy.

For learning, start locally first. Deploy once you understand the routes, tests, and GitHub workflow.
