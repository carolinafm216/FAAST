import pathlib
from life_expectancy.data_cleaning import clean_data, file_path
from life_expectancy.loading_saving_data import load_data, save_data

LIFE_EXPECTANCY_FILE_PATH = (
    pathlib.Path(__file__).parent / "data" / "eu_life_expectancy_raw.tsv"
)

if __name__ == "__main__":  # pragma: no cover
    save_data(clean_data(load_data(LIFE_EXPECTANCY_FILE_PATH), "PT"))
