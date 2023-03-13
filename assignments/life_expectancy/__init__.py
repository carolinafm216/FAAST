from pathlib import Path
from life_expectancy.cleaning import clean_data, file_path

LIFE_EXPECTANCY_FILE_PATH=Path('eu_life_expectancy_raw.tsv')


if __name__ == "__main__":  # pragma: no cover
    clean_data(LIFE_EXPECTANCY_FILE_PATH,'PT')
