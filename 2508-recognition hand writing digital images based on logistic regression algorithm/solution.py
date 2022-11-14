# coding: utf-8
from numpy import ndarray
from sklearn.linear_model import LogisticRegression


class LogisticRegressionClassifier(object):
    def __init__(self, max_iter: int) -> None:
        """
        In this function you need to initialize the KNN classifier from sklearn
        :param max_iter: Given maximum iteration number which format is int
        """
        # write your code here
        self.clf = LogisticRegression(max_iter=max_iter)

    def fit_data(self, x_train: ndarray, y_train: ndarray) -> None:
        """
        In this function you need to fit the input data and label to the KNN classifier
        :param x_train: Input data which format is ndarray
        :param y_train: Input label which format is ndarray
        """
        # write your code here
        self.clf.fit(x_train, y_train)

    def predict_data(self, x_test: ndarray) -> ndarray:
        """
        In this function you need to use KNN classifier to predict input test data
        :param x_test: Input test data which format is ndarray
        :return: The predicted label for input test data which format is ndarray
        """
        # write your code here
        return self.clf.predict(x_test)
