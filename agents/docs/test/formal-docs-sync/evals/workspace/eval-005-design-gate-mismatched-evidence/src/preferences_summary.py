FIELD_ORDER = ("language", "timezone", "theme")


def build_summary(preferences):
    return [(field, preferences[field]) for field in FIELD_ORDER if preferences.get(field)]
