import httpx
from bs4 import BeautifulSoup

from app.collectors.base import BaseCollector
from app.core.config import settings
from app.models.item import CrawlItem
from app.services.cleaner import normalize_text


class HtmlCollector(BaseCollector):
    name = "html"

    async def collect(self, url: str) -> CrawlItem:
        headers = {"User-Agent": settings.default_user_agent}
        async with httpx.AsyncClient(
            timeout=settings.request_timeout,
            follow_redirects=True,
            headers=headers,
        ) as client:
            response = await client.get(url)
            response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")
        title = soup.title.get_text(strip=True) if soup.title else None
        text = normalize_text(soup.get_text(" ", strip=True))
        return CrawlItem(url=str(response.url), title=title, text=text, raw=None)
