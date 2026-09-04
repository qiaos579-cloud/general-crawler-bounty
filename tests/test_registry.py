from app.collectors.base import BaseCollector
from app.core.registry import CollectorRegistry
from app.models.item import CrawlItem


class DemoCollector(BaseCollector):
    name = "demo"

    async def collect(self, url: str) -> CrawlItem:
        return CrawlItem(url=url, text="demo")


def test_registry() -> None:
    registry = CollectorRegistry()
    registry.register(DemoCollector)
    assert registry.names() == ["demo"]
    assert isinstance(registry.create("demo"), DemoCollector)
