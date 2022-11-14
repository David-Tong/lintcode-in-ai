# coding: utf-8
from pandas import DataFrame
from sklearn.model_selection import train_test_split


def data_split(data: DataFrame) -> tuple:
    """
    :param data: the source data
    :return: return a tuple
    """
    # -- write your code here --
    data_train, data_test = train_test_split(data, test_size=0.3)
    X_train, X_test, y_train, y_test = data_train.iloc[: , :-1], data_test.iloc[: , :-1], data_train.iloc[: , -1], data_test.iloc[: , -1]
    return (X_train, X_test, y_train, y_test)
