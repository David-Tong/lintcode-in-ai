# coding: utf-8
from pandas import DataFrame
import pandas as pd


def loc_split(data: DataFrame) -> DataFrame:
    """
    :param data: the source data
    :return: return a DataFrame
    """
    # -- write your code here --
    start = "2013-01-02"
    end = "2013-01-05"
    index = pd.date_range(start=start, end=end, closed="left")
    columns = ["B", "D"]
    df = pd.DataFrame(columns=columns, index=index)
    return df
