from collections.abc import Iterable


def export_catalog_v2(item_ids: Iterable[str]) -> dict[str, object]:
    return {"format": "v2", "items": list(item_ids)}
