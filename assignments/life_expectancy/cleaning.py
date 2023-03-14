import argparse
import pathlib
import pandas as pd

read_file_name = "eu_life_expectancy_raw.tsv"
file_path = pathlib.Path(__file__).parent/"data"/ read_file_name

def load_data(path:pathlib.Path):
    with open(path, encoding="utf8") as file:
        read_file=pd.read_csv(file,sep='\t')
        df = pd.DataFrame(read_file)
    return df

def unpivot(df):
    #keep unit, sex, age and geo time as columns and unpivot years
    df = df.melt(id_vars=[r"unit,sex,age,geo\time"],
                        value_vars=['2021 ','2020 ', '2019 ', '2018 ', '2017 ',
        '2016 ', '2015 ', '2014 ', '2013 ', '2012 ', '2011 ', '2010 ', '2009 ',
        '2008 ', '2007 ', '2006 ', '2005 ', '2004 ', '2003 ', '2002 ', '2001 ',
        '2000 ', '1999 ', '1998 ', '1997 ', '1996 ', '1995 ', '1994 ', '1993 ',
        '1992 ', '1991 ', '1990 ', '1989 ', '1988 ', '1987 ', '1986 ', '1985 ',
        '1984 ', '1983 ', '1982 ', '1981 ', '1980 ', '1979 ', '1978 ', '1977 ',
        '1976 ', '1975 ', '1974 ', '1973 ', '1972 ', '1971 ', '1970 ', '1969 ',
        '1968 ', '1967 ', '1966 ', '1965 ', '1964 ', '1963 ', '1962 ', '1961 ',
        '1960 '], value_name="value")
    #split columns by comma in order to have 4 columns instead of 1
    df[['unit', 'sex', 'age', 'geo\time']] = df[r"unit,sex,age,geo\time"].str.split(",", expand = True)
    #drop the column thant we split before
    df=df.drop([r'unit,sex,age,geo\time'], axis=1)
    #rename variables
    df=df.rename(columns={"variable": "year", "geo\time": "region"})
    df = df[['unit', 'sex', 'age', 'region', 'year', 'value']]
    return df

def date_format(df):
    df = df.astype({'year':'int'})
    #remove all values that are equal to ":"
    df = df[df.value != ': ']
    #remove space from colum value, because it should be a number
    df[['value', 'delete']] = df["value"].str.split(" ", expand = True)
    #drop second column with the space
    df=df.drop(["delete"], axis=1)
    #define value as float
    df = df.astype({'value':'float'})
    return df

def filter_region(df, country):
    df = df[df.region == country]
    return df

def save_data(df):
    df.to_csv(pathlib.Path(__file__).parent/"data"/ "pt_life_expectancy.csv",index=False)

def clean_data(df,country):
    return filter_region(date_format(unpivot(df)), country)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("country")
    args = parser.parse_args()

    save_data(clean_data(load_data(file_path), args.country))
