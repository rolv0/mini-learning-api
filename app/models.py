from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, Field


class NoteStatus(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    topic: str = Field(min_length=1, max_length=60)


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    topic: str | None = Field(default=None, min_length=1, max_length=60)
    status: NoteStatus | None = None


class Note(BaseModel):
    id: UUID
    title: str
    topic: str
    status: NoteStatus
