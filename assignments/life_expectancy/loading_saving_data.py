import pathlib
import pandas as pd

read_file_name = "life_expectancy_original.json"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def save_data(df: pd.DataFrame):
    df.to_csv(
        pathlib.Path(__file__).parent / "data" / "pt_life_expectancy.csv", index=False
    )
    return df
