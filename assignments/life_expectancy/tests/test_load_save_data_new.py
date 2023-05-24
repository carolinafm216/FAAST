import pathlib
from unittest.mock import patch
import pandas as pd
from life_expectancy import file_processor
from life_expectancy.loading_saving_data import *


File_Path = pathlib.Path(__file__).parent / "data" / read_file_name


def test_load_data(Life_Expectancy_Filter_Region):
    # test if load data function is calling the right arguments
    with patch("life_expectancy.loading_saving_data.pd.read_csv") as mock_read_csv:
        mock_read_csv.return_value = Life_Expectancy_Filter_Region  # imput fixture

        strategy = file_processor.CSVReadingStrategy()
        Raw_Actual = strategy.read_file(File_Path)

        pd.testing.assert_frame_equal(Raw_Actual, Life_Expectancy_Filter_Region)
        mock_read_csv.assert_called_once_with(File_Path, sep="\t")



def test_save_data(capfd):
    msg = "I was saved"

    with patch("life_expectancy.loading_saving_data.save_data") as mock_save:
        mock_save.side_effect = print(msg, end="")

        out, _ = capfd.readouterr()
        assert out == msg
