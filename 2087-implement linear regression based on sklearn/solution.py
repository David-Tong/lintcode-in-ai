# coding: utf-8
from sklearn import datasets, linear_model
from numpy import ndarray


class Diabetes(object):

    def __init__(self):
        # write your code here
        # you can do necessary initialization here
        self.reg = linear_model.LinearRegression()

    def train(self, X_train: ndarray, y_train: ndarray):
        # write your code here
        # you should train the input data
        self.reg.fit(X_train, y_train)

    def test(self, X_test: ndarray) -> ndarray:
        # write your code here
        # you should return a prediction corresponding to the X_test input
        return self.reg.predict(X_test)
