import argparse
import pathlib
import pandas as pd

read_file_name = "eu_life_expectancy_raw.tsv"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def load_data(path: pathlib.Path) -> pd.DataFrame:
    # with open(path, encoding="utf8") as file:
    read_file = pd.read_csv(path, sep="\t")
    df = pd.DataFrame(read_file)
    return df


def _unpivot(df: pd.DataFrame) -> pd.DataFrame:
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


def _convert_date_format(df: pd.DataFrame) -> pd.DataFrame:
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


def _filter_region(df: pd.DataFrame, country: str) -> pd.DataFrame:
    df = df[df.region == country]
    return df


def save_data(df: pd.DataFrame):
    df.to_csv(
        pathlib.Path(__file__).parent / "data" / "pt_life_expectancy.csv", index=False
    )


def clean_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    # return filter_region(date_format(unpivot(df)), country)
    return df.pipe(_unpivot).pipe(_convert_date_format).pipe(_filter_region, country)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("country")
    args = parser.parse_args()

    save_data(clean_data(load_data(file_path), args.country))
