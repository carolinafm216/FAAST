import pathlib
import pandas as pd

read_file_name = "eu_life_expectancy_raw.tsv"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def load_data(path: pathlib.Path) -> pd.DataFrame:
    # with open(path, encoding="utf8") as file:
    read_file = pd.read_csv(path, sep="\t")
    df = pd.DataFrame(read_file)
    return df


def save_data(df: pd.DataFrame):
    df.to_csv(
        pathlib.Path(__file__).parent / "data" / "pt_life_expectancy.csv", index=False
    )
    return df
