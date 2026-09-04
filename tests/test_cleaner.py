from app.services.cleaner import normalize_text


def test_normalize_text() -> None:
    assert normalize_text("a   b\n c") == "a b c"
