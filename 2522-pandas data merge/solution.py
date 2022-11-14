# coding: utf-8
from pandas import DataFrame
import pandas as pd


def data_merge(left_data: DataFrame, right_data: DataFrame) -> DataFrame:
    """
    :param left_data: the first source data
    :param right_data: the second source data
    :return: return a DataFrame
    """
    # -- write your code here --
    return left_data.merge(right_data, left_on=['key1', 'key2'], right_on=['key1', 'key2'])
