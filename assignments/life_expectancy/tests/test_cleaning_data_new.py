import pandas as pd
from life_expectancy.data_cleaning import unpivot, convert_date_format, filter_region

def test_unipivot(life_expectancy_unpivot, life_expectancy_original):
    response_df = unpivot(life_expectancy_original)
    # in order to force json file columns to be str
    life_expectancy_unpivot = life_expectancy_unpivot.astype({"year": "str"})
    life_expectancy_unpivot = life_expectancy_unpivot.astype({"value": "str"})
    response_df = response_df.astype({"value": "str"})

    pd.testing.assert_frame_equal(response_df, life_expectancy_unpivot)


def test_convert_date_format(
    life_expectancy_convert_date_format, life_expectancy_unpivot
):
    response_df = convert_date_format(life_expectancy_unpivot)
    # because it assumes int32 instead of int64
    life_expectancy_convert_date_format = life_expectancy_convert_date_format.astype(
        {"year": "int"}
    )
    pd.testing.assert_frame_equal(
        response_df.reset_index(drop=True),
        life_expectancy_convert_date_format.reset_index(drop=True),
        check_names=False,
    )


def test_filter_region(
    life_expectancy_filter_region, life_expectancy_convert_date_format
):
    response_df = filter_region(life_expectancy_convert_date_format, "PT")
    # because it assumes int32 instead of int64
    pd.testing.assert_frame_equal(
        response_df.reset_index(drop=True),
        life_expectancy_filter_region.reset_index(drop=True),
        check_names=False,
    )
