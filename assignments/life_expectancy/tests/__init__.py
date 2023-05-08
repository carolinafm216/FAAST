"""Test suite for the 1st assignment"""
from pathlib import Path
import pathlib
import pandas as pd

FIXTURES_DIR = Path(__file__).parent / "fixtures"
OUTPUT_DIR = Path(__file__).parent.parent / "data"

df_original = pd.read_json(
    pathlib.Path(__file__).parent / "fixtures" / "life_expectancy_original.json"
)
df_expected_unpivot = pd.read_json(
    pathlib.Path(__file__).parent / "fixtures" / "life_expectancy_unpivot.json"
)
