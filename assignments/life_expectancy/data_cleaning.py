import pathlib
import pandas as pd

read_file_name = "eu_life_expectancy_raw.tsv"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def unpivot(df: pd.DataFrame) -> pd.DataFrame:
    # keep unit, sex, age and geo time as columns and unpivot years
    value_vars = list(df.columns)[1:]
    df = df.melt(
        id_vars=[r"unit,sex,age,geo\time"], value_vars=value_vars, value_name="value"
    )
    # split columns by comma in order to have 4 columns instead of 1
    df[["unit", "sex", "age", "geo\time"]] = df[r"unit,sex,age,geo\time"].str.split(
        ",", expand=True
    )
    # drop the column thant we split before
    df = df.drop([r"unit,sex,age,geo\time"], axis=1)
    # rename variables
    df = df.rename(columns={"variable": "year", "geo\time": "region"})
    df = df[["unit", "sex", "age", "region", "year", "value"]]
    return df


def convert_date_format(df: pd.DataFrame) -> pd.DataFrame:
    df = df.astype({"year": "int"})
    # remove all values that are equal to ":"
    df = df[df.value != ": "]
    # remove space from colum value, because it should be a number
    df[["value", "delete"]] = df["value"].str.split(" ", expand=True)
    # drop second column with the space
    df = df.drop(["delete"], axis=1)
    # define value as float
    df = df.astype({"value": "float"})
    return df


def filter_region(df: pd.DataFrame, country: str) -> pd.DataFrame:
    df = df[df.region == country]
    return df


def clean_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    # return filter_region(date_format(unpivot(df)), country)
    return df.pipe(unpivot).pipe(convert_date_format).pipe(filter_region, country)
