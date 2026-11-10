"""Seasonal gardening advice for the month and hemisphere."""

SEASONS_BY_MONTH = {
    1: "Winter", 2: "Winter", 3: "Spring",
    4: "Spring", 5: "Spring", 6: "Summer",
    7: "Summer", 8: "Summer", 9: "Autumn",
    10: "Autumn", 11: "Autumn", 12: "Winter",
}

ADVICE_BY_SEASON = {
    "Spring": "Sow hardy vegetables and prepare your beds.",
    "Summer": "Water plants regularly and harvest ripe produce.",
    "Autumn": "Collect seeds and plant cool-weather crops.",
    "Winter": "Protect tender plants from frost and plan next season's beds.",
}

OPPOSITE_SEASON = {
    "Spring": "Autumn",
    "Summer": "Winter",
    "Autumn": "Spring",
    "Winter": "Summer",
}


def validate_month(month):
    """Return a valid integer month or raise ValueError with a friendly message."""
    if isinstance(month, bool):
        raise ValueError("Month must be a whole number from 1 to 12.")
    try:
        month = int(month)
    except (TypeError, ValueError):
        raise ValueError("Month must be a whole number from 1 to 12.") from None
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")
    return month


def get_season(month, hemisphere="north"):
    """Return a season for a month in the north or south hemisphere."""
    month = validate_month(month)
    hemisphere = hemisphere.strip().lower()
    if hemisphere not in {"north", "south"}:
        raise ValueError("Hemisphere must be 'north' or 'south'.")
    season = SEASONS_BY_MONTH[month]
    return season if hemisphere == "north" else OPPOSITE_SEASON[season]


def get_gardening_advice(month, hemisphere="north"):
    """Look up gardening advice for a month and hemisphere."""
    return ADVICE_BY_SEASON[get_season(month, hemisphere)]


def main():
    """Prompt for input and print advice without exposing tracebacks."""
    try:
        month = input("Enter a month number (1-12): ")
        hemisphere = input("Hemisphere (north/south, default north): ").strip().lower()
        hemisphere = hemisphere or "north"
        season = get_season(month, hemisphere)
        print(f"Season: {season}")
        print(get_gardening_advice(month, hemisphere))
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
