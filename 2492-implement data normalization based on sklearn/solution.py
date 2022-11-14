# coding: utf-8
from sklearn.preprocessing import MinMaxScaler
from numpy import ndarray


class data_normalization(object):

    def __init__(self) -> None:
        """
        In this function you need to initialize normalization function from sklearn
        """
        # write your code here
        self.scaler = MinMaxScaler()

    def fit_data(self, data: ndarray) -> None:
        """
        In this function you need to fit data to the normalization function.
        :param data: Input data which type is ndarray.
        """
        # write your code here
        self.scaler.fit(data)

    def norm_data(self, data: ndarray) -> ndarray:
        """
        In this function you need to transform data using normalization function.
        :param data: Input data which type is ndarray.
        :return: Data after normalization which type should be ndarray.
        """
        # write your code here
        return self.scaler.transform(data)