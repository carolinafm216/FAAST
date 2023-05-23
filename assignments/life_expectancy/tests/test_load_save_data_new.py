import pathlib
from unittest.mock import patch
import pandas as pd
from life_expectancy.loading_saving_data import load_data


read_file_name = "mock_file_path.tsv"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def test_load_data(life_expectancy_filter_region):
    # test if load data function is calling the right arguments
    with patch("life_expectancy.loading_saving_data.pd.read_csv") as mock_read_csv:
        mock_read_csv.return_value = life_expectancy_filter_region  # imput fixture

        raw_actual = load_data(file_path)

        pd.testing.assert_frame_equal(raw_actual, life_expectancy_filter_region)
        mock_read_csv.assert_called_once_with(file_path, sep="\t")


def test_save_data(capfd):
    msg = "I was saved"

    with patch("life_expectancy.loading_saving_data.save_data") as mock_save:
        mock_save.side_effect = print(msg, end="")

        out, _ = capfd.readouterr()
        assert out == msg
