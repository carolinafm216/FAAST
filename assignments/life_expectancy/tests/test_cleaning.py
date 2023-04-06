"""Tests for the cleaning module"""
from unittest.mock import patch
import pandas as pd
from life_expectancy.loading_saving_data import save_data, load_data, file_path
from life_expectancy.data_cleaning import clean_data
from . import OUTPUT_DIR


@patch("life_expectancy.loading_saving_data.save_data")
@patch("life_expectancy.loading_saving_data.load_data")
def test_clean_data(
    mock_load, mock_save, life_expectancy_original, pt_life_expectancy_expected
):
    """Run the `clean_data` function and compare the output to the expected output"""
    mock_load.return_value = life_expectancy_original
    mock_save.side_effect = print()

    save_data(clean_data(load_data(file_path), "PT"))
    pt_life_expectancy_actual = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
