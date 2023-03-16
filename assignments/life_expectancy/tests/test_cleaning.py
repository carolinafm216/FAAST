"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import clean_data, save_data, load_data, file_path
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    save_data(clean_data(load_data(file_path), "PT"))
    pt_life_expectancy_actual = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


if __name__ == "__main__":  # pragma: no cover
    test_clean_data(file_path)
