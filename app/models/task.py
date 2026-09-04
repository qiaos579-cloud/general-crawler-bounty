from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, HttpUrl


class TaskStatus(StrEnum):
    pending = "pending"
    running = "running"
    success = "success"
    failed = "failed"


class CrawlTaskCreate(BaseModel):
    url: HttpUrl
    collector: str = Field(default="html")


class CrawlTask(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    url: HttpUrl
    collector: str
    status: TaskStatus = TaskStatus.pending
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    error: str | None = None
