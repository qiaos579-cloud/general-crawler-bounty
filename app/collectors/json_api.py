import json

import httpx

from app.collectors.base import BaseCollector
from app.core.config import settings
from app.models.item import CrawlItem


class JsonCollector(BaseCollector):
    name = "json"

    async def collect(self, url: str) -> CrawlItem:
        headers = {"User-Agent": settings.default_user_agent}
        async with httpx.AsyncClient(
            timeout=settings.request_timeout,
            follow_redirects=True,
            headers=headers,
        ) as client:
            response = await client.get(url)
            response.raise_for_status()
            payload = response.json()

        return CrawlItem(
            url=str(response.url),
            title=None,
            text=json.dumps(payload, ensure_ascii=False),
            raw=payload,
        )
