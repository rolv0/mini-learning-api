from uuid import UUID

from fastapi import FastAPI, HTTPException, Response, status

from app.models import Note, NoteCreate, NoteUpdate
from app.store import NoteStore

app = FastAPI(
    title="Mini Learning API",
    description="A small API for learning FastAPI, testing, and GitHub contributions.",
    version="0.1.0",
)

store = NoteStore()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/notes", response_model=list[Note])
def list_notes() -> list[Note]:
    return store.list_notes()


@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate) -> Note:
    return store.create_note(payload)


@app.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: UUID, payload: NoteUpdate) -> Note:
    note = store.update_note(note_id, payload)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: UUID) -> Response:
    deleted = store.delete_note(note_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
