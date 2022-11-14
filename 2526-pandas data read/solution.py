# coding: utf-8
from pandas import DataFrame
import pandas as pd


def file_reading(input_path: str) -> DataFrame:
    """
    :param input_path: the source data path
    :return: return a DataFrame
    """
    # -- write your code here --
    return pd.read_csv(filepath_or_buffer=input_path, nrows=5)
