import logging
from uuid import UUID

from app.collectors.html import HtmlCollector
from app.collectors.json_api import JsonCollector
from app.core.config import settings
from app.core.registry import registry
from app.models.item import CrawlItem
from app.models.task import CrawlTask, CrawlTaskCreate, TaskStatus
from app.services.deduplicator import fingerprint
from app.storage.jsonl import JsonlStorage

logger = logging.getLogger(__name__)

registry.register(HtmlCollector)
registry.register(JsonCollector)


class TaskService:
    def __init__(self) -> None:
        self.tasks: dict[UUID, CrawlTask] = {}
        self.storage = JsonlStorage(settings.output_path)
        self.seen_hashes: set[str] = set()

    async def run(self, request: CrawlTaskCreate) -> tuple[CrawlTask, CrawlItem | None]:
        task = CrawlTask(url=request.url, collector=request.collector)
        self.tasks[task.id] = task
        task.status = TaskStatus.running

        try:
            collector = registry.create(request.collector)
            item = await collector.collect(str(request.url))
            item.content_hash = fingerprint(item)

            if item.content_hash not in self.seen_hashes:
                self.storage.append(item)
                self.seen_hashes.add(item.content_hash)

            task.status = TaskStatus.success
            return task, item
        except Exception as exc:
            task.status = TaskStatus.failed
            task.error = str(exc)
            logger.exception("Task failed: %s", task.id)
            return task, None

    def get(self, task_id: UUID) -> CrawlTask | None:
        return self.tasks.get(task_id)


service = TaskService()
