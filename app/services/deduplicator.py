import hashlib

from app.models.item import CrawlItem


def fingerprint(item: CrawlItem) -> str:
    basis = f"{item.url}\n{item.text or ''}"
    return hashlib.sha256(basis.encode("utf-8")).hexdigest()
