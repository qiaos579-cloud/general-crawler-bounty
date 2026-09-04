from app.collectors.base import BaseCollector


class CollectorRegistry:
    def __init__(self) -> None:
        self._collectors: dict[str, type[BaseCollector]] = {}

    def register(self, collector_cls: type[BaseCollector]) -> None:
        self._collectors[collector_cls.name] = collector_cls

    def create(self, name: str) -> BaseCollector:
        try:
            return self._collectors[name]()
        except KeyError as exc:
            available = ", ".join(sorted(self._collectors)) or "none"
            raise ValueError(f"Unknown collector: {name}. Available: {available}") from exc

    def names(self) -> list[str]:
        return sorted(self._collectors)


registry = CollectorRegistry()
