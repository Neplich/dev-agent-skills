FIELD_ORDER = ("language", "timezone", "theme")


def build_summary(preferences, compact=False):
    items = [(field, preferences[field]) for field in FIELD_ORDER if preferences.get(field)]
    if compact:
        return " | ".join(f"{field}: {value}" for field, value in items)
    return items
