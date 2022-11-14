# coding: utf-8
from numpy import ndarray
from pandas import DataFrame
from sklearn.linear_model import LogisticRegression


class LgClassifier(object):
    def __init__(self) -> None:
        """
        In this function you need to initialize the LogisticRegression classifier from sklearn
        """
        # write your code here
        self.clf = LogisticRegression(random_state=0)

    def fit_data(self, x_train: DataFrame, y_train: DataFrame) -> None:
        """
        In this function you need to fit the input data and label to the KNN classifier
        :param x_train: Input data which format is DataFrame
        :param y_train: Input label which format is DataFrame
        """
        # write your code here
        self.clf.fit(x_train, y_train)

    def predict_data(self, x_test: DataFrame) -> ndarray:
        """
        In this function you need to use KNN classifier to predict input test data
        :param x_test: Input test data which format is DataFrame
        :return: The predicted label for input test data which format is ndarray
        """
        # write your code here
        return self.clf.predict(x_test)
