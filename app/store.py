from uuid import UUID, uuid4

from app.models import Note, NoteCreate, NoteStatus, NoteUpdate


class NoteStore:
    def __init__(self) -> None:
        self._notes: dict[UUID, Note] = {}

    def list_notes(self) -> list[Note]:
        return list(self._notes.values())

    def create_note(self, payload: NoteCreate) -> Note:
        note = Note(
            id=uuid4(),
            title=payload.title,
            topic=payload.topic,
            status=NoteStatus.TODO,
        )
        self._notes[note.id] = note
        return note

    def get_note(self, note_id: UUID) -> Note | None:
        return self._notes.get(note_id)

    def update_note(self, note_id: UUID, payload: NoteUpdate) -> Note | None:
        current = self.get_note(note_id)
        if current is None:
            return None

        updated = current.model_copy(update=payload.model_dump(exclude_unset=True))
        self._notes[note_id] = updated
        return updated

    def delete_note(self, note_id: UUID) -> bool:
        if note_id not in self._notes:
            return False

        del self._notes[note_id]
        return True

    def clear(self) -> None:
        self._notes.clear()
