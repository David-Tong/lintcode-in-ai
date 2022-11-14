# coding: utf-8
from pandas import DataFrame
from sklearn.impute import SimpleImputer


class ImputerClassifier(object):
    def __init__(self) -> None:
        """
        In this function you need to initialize the SimpleImputer classifier from sklearn.
        """
        # write your code here
        self.imp = SimpleImputer()

    def fit_transform_data(self, data: DataFrame) -> DataFrame:
        """
        In this function you need to fit the input data and label to the SimpleImputer classifier
        and returns the data after the missing value processing.
        :param data: Input data which format is DataFrame
        :return Returns a data of type DataFrame
        """
        # write your code here
        data["Age"] = self.imp.fit_transform(data["Age"].values.reshape(-1, 1))[:, 0]
        return data
