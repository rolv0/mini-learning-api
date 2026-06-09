from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app, store


client = TestClient(app)


def setup_function() -> None:
    store.clear()


def test_root_points_to_docs_and_health() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "name": "Mini Learning API",
        "docs": "/docs",
        "health": "/health",
    }


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_notes() -> None:
    create_response = client.post(
        "/notes",
        json={"title": "Learn FastAPI", "topic": "backend"},
    )

    assert create_response.status_code == 201
    created = create_response.json()
    assert created["title"] == "Learn FastAPI"
    assert created["topic"] == "backend"
    assert created["status"] == "todo"
    assert datetime.fromisoformat(created["created_at"])

    list_response = client.get("/notes")

    assert list_response.status_code == 200
    assert list_response.json() == [created]


def test_list_notes_can_filter_by_topic() -> None:
    backend_note = client.post(
        "/notes",
        json={"title": "Learn FastAPI", "topic": "backend"},
    ).json()
    client.post(
        "/notes",
        json={"title": "Practice pytest", "topic": "testing"},
    )

    response = client.get("/notes?topic=backend")

    assert response.status_code == 200
    assert response.json() == [backend_note]


def test_list_notes_can_filter_by_status() -> None:
    done_note = client.post(
        "/notes",
        json={"title": "Write tests", "topic": "testing"},
    ).json()
    client.patch(f"/notes/{done_note['id']}", json={"status": "done"})
    client.post(
        "/notes",
        json={"title": "Learn FastAPI", "topic": "backend"},
    )

    response = client.get("/notes?status=done")

    assert response.status_code == 200
    assert response.json()[0]["id"] == done_note["id"]


def test_update_note_status() -> None:
    note = client.post(
        "/notes",
        json={"title": "Write tests", "topic": "testing"},
    ).json()

    response = client.patch(
        f"/notes/{note['id']}",
        json={"status": "done"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "done"


def test_delete_note() -> None:
    note = client.post(
        "/notes",
        json={"title": "Read docs", "topic": "fastapi"},
    ).json()

    delete_response = client.delete(f"/notes/{note['id']}")

    assert delete_response.status_code == 204
    assert client.get("/notes").json() == []


def test_missing_note_returns_404() -> None:
    response = client.patch(
        "/notes/00000000-0000-0000-0000-000000000000",
        json={"status": "done"},
    )

    assert response.status_code == 404
