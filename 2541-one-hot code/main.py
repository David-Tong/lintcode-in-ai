# coding: utf-8
from pandas import DataFrame
from numpy import ndarray
from sklearn.preprocessing import OneHotEncoder


class OneHot(object):
    def __init__(self) -> None:
        """
        In this function you need to initialize the OneHotEncoder classifier from sklearn.
        :return None
        """
        # write your code here
        self.enc = OneHotEncoder()

    def fit_transform_data(self, data: DataFrame) -> ndarray:
        """
        In this function you need to fit_transform the input data.
        :param data: Input data which format is DataFrame
        :return Returns a data of type ndarray
        """
        # write your code here
        return self.enc.fit_transform(data).toarray()