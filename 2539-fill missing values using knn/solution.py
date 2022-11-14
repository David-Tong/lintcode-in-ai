# coding: utf-8
from pandas import DataFrame
from sklearn.neighbors import KNeighborsRegressor


class KnnSetAge(object):
    def __init__(self) -> None:
        """
        In this function you need to initialize the KNN Classifier from sklearn
        :return None
        """
        # write your code here
        self.reg = KNeighborsRegressor()

    def fit_data(self, x_train: DataFrame, y_train: DataFrame) -> None:
        """
        In this function you need to fit the input data and label to the KNN classifier
        :param x_train: Input data which format is DataFrame
        :param y_train: Input label which format is DataFrame
        :return None
        """
        # write your code here
        self.reg.fit(x_train, y_train)

    def predict_data(self, x_test: DataFrame, data: DataFrame) -> DataFrame:
        """
        In this function you need to use KNN classifier to predict input test data
        :param x_test: Input test data which format is DataFrame
        :param data: Input source data which format is DataFrame
        :return: The predicted label for input test data which format is DataFrame
        """
        # write your code here
        predicted_ages = self.reg.predict(x_test)
        data.loc[data["Age"].isnull(), "Age"] = predicted_ages
        return data
