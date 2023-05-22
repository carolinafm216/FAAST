from enum import Enum

import pandas as pd


# mudar nome do ficheiro para country - pap8
class Country(Enum):
    ES = "ES"
    IT = "IT"
    PT = "PT"

    @classmethod
    def list_all_countries(self, df: pd.DataFrame) -> pd.DataFrame:
        listCountries = df["region"].str[:2]
        listCountries = list(dict.fromkeys(listCountries.to_list()))
        return listCountries
