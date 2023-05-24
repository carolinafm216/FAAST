import pathlib
from life_expectancy.Country import Country

read_file_name = "mock_file_path.tsv"
file_path = pathlib.Path(__file__).parent / "data" / read_file_name


def test_list_country(coutry_list_expected, life_expectancy_unpivot):
    response = Country.list_all_countries(life_expectancy_unpivot)
    assert response == coutry_list_expected
