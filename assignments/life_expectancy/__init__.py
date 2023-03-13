import argparse
from life_expectancy.cleaning import clean_data

LIFE_EXPECTANCY_FILE_PATH=r"C:\Users\cfmarreiros\Documents\GitHub\FAAST\assignments\life_expectancy\data\eu_life_expectancy_raw.tsv"
SAVE_FILE_PATH=r"C:\Users\cfmarreiros\Documents\GitHub\FAAST\assignments\life_expectancy\data"

if __name__ == "__main__":  # pragma: no cover
    clean_data(LIFE_EXPECTANCY_FILE_PATH,'PT')
    