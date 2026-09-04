from datetime import datetime, timezone

from pydantic import BaseModel, Field


class CrawlItem(BaseModel):
    url: str
    title: str | None = None
    text: str | None = None
    raw: dict | list | str | None = None
    content_hash: str | None = None
    collected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
