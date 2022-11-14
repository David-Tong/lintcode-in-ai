# coding: utf-8
from pandas import DataFrame
import pandas as pd


def create_dataframe() -> DataFrame:
    """
    :return: return a DataFrame, create_series() -> DataFrame:
    """
    data = {"name": ["Tom", "Jack", "Mike"], "age": [28, 34, 29]}
    index = ["a", "b", "c"]

    df = pd.DataFrame(data=data, index=index)
    return df


df = create_dataframe()
print(df)