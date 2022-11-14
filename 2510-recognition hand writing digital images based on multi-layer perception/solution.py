# coding: utf-8
from numpy import ndarray
from sklearn.neural_network import MLPClassifier


class MultiLayerProceptronClassifier(object):
    def __init__(self, layer_1: int, layer_2: int) -> None:
        """
        In this function you need to initialize the KNN classifier from sklearn
        :param max_iter: Given maximum iteration number which format is int
        """
        # write your code here
        hidden_layer_sizes = [layer_1, layer_2]
        self.clf = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=100)

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
