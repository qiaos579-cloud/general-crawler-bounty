import json
from pathlib import Path

from app.models.item import CrawlItem


class JsonlStorage:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, item: CrawlItem) -> None:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(item.model_dump(mode="json"), ensure_ascii=False) + "\n")
