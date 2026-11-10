"""Garden advice organized as reusable season and advice lookups."""

SEASONS_BY_MONTH = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn",
}

ADVICE_BY_SEASON = {
    "Spring": "Sow hardy vegetables and prepare your beds.",
    "Summer": "Water plants regularly and harvest ripe produce.",
    "Autumn": "Collect seeds and plant cool-weather crops.",
    "Winter": "Protect tender plants from frost and plan next season's beds.",
}


def get_season(month):
    """Return the northern-hemisphere season for a month number."""
    return SEASONS_BY_MONTH[month]


def get_gardening_advice(month):
    """Look up gardening advice for a month."""
    return ADVICE_BY_SEASON[get_season(month)]


def main():
    """Print the season and gardening suggestion for the requested month."""
    month = int(input("Enter a month number (1-12): "))
    season = get_season(month)
    print(f"Season: {season}")
    print(get_gardening_advice(month))


if __name__ == "__main__":
    main()
