# coding: utf-8
import pandas as pd
from pandas import DataFrame

def removing_duplicate_values(input_data: DataFrame) -> DataFrame:
    """
    In this function you need to initialize the KNN classifier from sklearn
    :param input_data: Input data which data type is DataFrame
    :return: Data after removing duplictae values which data type should be DataFrame
    """
    # write your code here
    subset = ["method", "year"]
    return input_data.drop_duplicates(subset=subset)
