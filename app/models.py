from datetime import datetime
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, Field


class NoteStatus(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class NotePriority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    topic: str = Field(min_length=1, max_length=60)
    priority: NotePriority = NotePriority.MEDIUM


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    topic: str | None = Field(default=None, min_length=1, max_length=60)
    status: NoteStatus | None = None
    priority: NotePriority | None = None


class Note(BaseModel):
    id: UUID
    title: str
    topic: str
    status: NoteStatus
    priority: NotePriority
    created_at: datetime
