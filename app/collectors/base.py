from abc import ABC, abstractmethod

from app.models.item import CrawlItem


class BaseCollector(ABC):
    name = "base"

    @abstractmethod
    async def collect(self, url: str) -> CrawlItem:
        raise NotImplementedError
