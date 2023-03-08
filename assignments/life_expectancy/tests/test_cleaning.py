"""Tests for the cleaning module"""
import pandas as pd
import argparse

from life_expectancy.cleaning import clean_data
from . import OUTPUT_DIR, LIFE_EXPECTANCY_FILE_PATH, SAVE_FILE_PATH


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    #clean_data()
    clean_data(LIFE_EXPECTANCY_FILE_PATH,'PT')
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
