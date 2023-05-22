from argparse import PARSER
import argparse
import pathlib
from life_expectancy.Country import Country
from life_expectancy.data_cleaning import clean_data, unpivot
from life_expectancy.file_processor import (
    CSVReadingStrategy,
    JSONReadingStrategy,
    file_processor,
)
from life_expectancy.loading_saving_data import save_data


if __name__ == "__main__":  # pragma: no cover
    file = "eu_life_expectancy_raw.tsv"
    file_path = pathlib.Path(__file__).parent / "data" / file

    if file.split(".")[1] == "json":
        File_processor = file_processor(file_path, JSONReadingStrategy())
    else:
        File_processor = file_processor(file_path, CSVReadingStrategy())

    parser = argparse.ArgumentParser()
    parser.add_argument("region")
    args = parser.parse_args()
    # Process the file using the current strategy
    save_data(clean_data(File_processor.load_data(), args.region))

    print(Country.list_all_countries(unpivot(File_processor.load_data())))
