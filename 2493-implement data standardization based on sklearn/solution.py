# coding: utf-8
from sklearn.preprocessing import StandardScaler
from numpy import ndarray


class data_standardize(object):

    def __init__(self) -> None:
        """
        In this function you need to initialize standardization function from sklearn
        """
        # write your code here
        self.scaler = StandardScaler()

    def fit_data(self, data: ndarray) -> None:
        """
        In this function you need to fit data to the standardization function.
        :param data: Input data which type is ndarray.
        """
        # write your code here
        self.scaler.fit(data)

    def std_data(self, data: ndarray) -> ndarray:
        """
        In this function you need to transform data using standardization function.
        :param data: Input data which type is ndarray.
        :return: Data after standardization which type should be ndarray.
        """
        # write your code here
        return self.scaler.transform(data)