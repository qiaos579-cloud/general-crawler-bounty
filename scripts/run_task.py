import argparse
import asyncio
import json

from app.models.task import CrawlTaskCreate
from app.services.task_service import service


async def main() -> None:
    parser = argparse.ArgumentParser(description="Run one crawl task")
    parser.add_argument("--url", required=True)
    parser.add_argument("--collector", default="html", choices=["html", "json"])
    args = parser.parse_args()

    task, item = await service.run(CrawlTaskCreate(url=args.url, collector=args.collector))
    print(json.dumps({
        "task": task.model_dump(mode="json"),
        "item": item.model_dump(mode="json") if item else None,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
