from uuid import UUID

from fastapi import FastAPI, HTTPException

from app.core.logging import configure_logging
from app.core.registry import registry
from app.models.task import CrawlTaskCreate
from app.services.task_service import service

configure_logging()
app = FastAPI(title="通用爬虫（揭榜挂帅）", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/collectors")
def collectors() -> dict:
    return {"collectors": registry.names()}


@app.post("/tasks")
async def create_task(request: CrawlTaskCreate) -> dict:
    task, item = await service.run(request)
    return {
        "task": task.model_dump(mode="json"),
        "item": item.model_dump(mode="json") if item else None,
    }


@app.get("/tasks/{task_id}")
def get_task(task_id: UUID) -> dict:
    task = service.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.model_dump(mode="json")
