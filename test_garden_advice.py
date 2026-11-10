"""Tests for month validation and hemisphere-specific gardening advice."""
import unittest

from garden_advice import get_gardening_advice, get_season, validate_month


class GardenAdviceTests(unittest.TestCase):
    def test_northern_seasons(self):
        self.assertEqual(get_season(3), "Spring")
        self.assertEqual(get_season(7), "Summer")
        self.assertEqual(get_season(10), "Autumn")
        self.assertEqual(get_season(12), "Winter")

    def test_southern_hemisphere_reverses_seasons(self):
        self.assertEqual(get_season(3, "south"), "Autumn")
        self.assertEqual(get_season(7, "south"), "Winter")

    def test_default_hemisphere_is_north(self):
        self.assertEqual(get_season(3), get_season(3, "north"))

    def test_month_validation_accepts_numeric_input(self):
        self.assertEqual(validate_month("12"), 12)

    def test_month_validation_rejects_non_numeric_and_out_of_range(self):
        for value in ("spring", "", "0", "13", True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_month(value)

    def test_hemisphere_validation(self):
        with self.assertRaisesRegex(ValueError, "Hemisphere"):
            get_season(1, "east")

    def test_advice_matches_selected_season(self):
        self.assertEqual(
            get_gardening_advice(3, "south"),
            "Collect seeds and plant cool-weather crops.",
        )


if __name__ == "__main__":
    unittest.main()
