# coding: utf-8
from pandas import DataFrame


def group_aggregation(data: DataFrame) -> DataFrame:
    """
    :param data: the source data
    :return: return a DataFrame
    """
    # -- write your code here --
    print(data.groupby("company").mean())