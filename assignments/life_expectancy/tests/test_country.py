import pathlib
import unittest
from unittest.mock import patch
import numpy as np
from life_expectancy.Country import Country
from life_expectancy.data_cleaning import unpivot
from life_expectancy.file_processor import CSVReadingStrategy, file_processor
import pandas as pd
from pandas import testing as tm

from life_expectancy.tests.conftest import (
    coutry_list_expected,
    life_expectancy_original,
    life_expectancy_unpivot,
)

read_file_name = "mock_file_path.tsv"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def test_list_country(coutry_list_expected, life_expectancy_unpivot):
    response = Country.list_all_countries(life_expectancy_unpivot)
    assert response == coutry_list_expected
