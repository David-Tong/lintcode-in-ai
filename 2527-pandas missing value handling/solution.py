# coding: utf-8
from pandas import DataFrame


def miss_value_handling(data: DataFrame) -> DataFrame:
    """
    :param data: the source data
    :return: return a DataFrame
    """
    # -- write your code here --
    return data.dropna()