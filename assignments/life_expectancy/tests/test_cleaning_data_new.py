import pathlib
from life_expectancy.data_cleaning import unpivot, convert_date_format, filter_region
import pandas as pd

df_original = pd.read_json(
    pathlib.Path(__file__).parent / "fixtures" / "life_expectancy_original.json"
)
df_expected_unpivot = pd.read_json(
    pathlib.Path(__file__).parent / "fixtures" / "life_expectancy_unpivot.json"
)
df_expectancy_convert_date_format = pd.read_json(
    pathlib.Path(__file__).parent
    / "fixtures"
    / "life_expectancy_convert_date_format.json"
)


def test_unipivot(life_expectancy_unpivot):
    response_df = unpivot(df_original)
    # in order to force json file columns to be str
    life_expectancy_unpivot = life_expectancy_unpivot.astype({"year": "str"})
    life_expectancy_unpivot = life_expectancy_unpivot.astype({"value": "str"})
    response_df = response_df.astype({"value": "str"})

    pd.testing.assert_frame_equal(response_df, life_expectancy_unpivot)


def test_convert_date_format(life_expectancy_convert_date_format):
    response_df = convert_date_format(df_expected_unpivot)
    # because it assumes int32 instead of int64
    life_expectancy_convert_date_format = life_expectancy_convert_date_format.astype(
        {"year": "int"}
    )
    pd.testing.assert_frame_equal(
        response_df.reset_index(drop=True),
        life_expectancy_convert_date_format.reset_index(drop=True),
        check_names=False,
    )


def test_filter_region(life_expectancy_filter_region):
    response_df = filter_region(df_expectancy_convert_date_format, "PT")
    # because it assumes int32 instead of int64
    pd.testing.assert_frame_equal(
        response_df.reset_index(drop=True),
        life_expectancy_filter_region.reset_index(drop=True),
        check_names=False,
    )
