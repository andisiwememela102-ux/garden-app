"""Garden advice starter for the Git Workflows practical."""

month = int(input("Enter a month number (1-12): "))

if month in (12, 1, 2):
    season = "Winter"
elif month in (3, 4, 5):
    season = "Spring"
elif month in (6, 7, 8):
    season = "Summer"
else:
    season = "Autumn"

# TODO: Extract the season lookup into a reusable function.
# TODO: Move seasonal advice into a data structure instead of hardcoding it.
# TODO: Validate the month so invalid input does not produce incorrect advice.

if season == "Spring":
    advice = "Sow hardy vegetables and prepare your beds."
elif season == "Summer":
    advice = "Water plants regularly and harvest ripe produce."
elif season == "Autumn":
    advice = "Collect seeds and plant cool-weather crops."
else:
    advice = "Protect tender plants from frost and plan next season's beds."

print(f"Season: {season}")
print(advice)
