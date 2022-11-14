#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numpy import ndarray
from sklearn.linear_model import LinearRegression


def linear_regression(xtrain: ndarray, ytrain: ndarray, xtest: ndarray) -> ndarray:
    """
    :param xtrain: Training set X
    :param ytrain: Training set Y
    :param xtest: Testing set X
    :return: Return the prediction you got from model
    """
    # -- write your code here --
    reg = LinearRegression()
    reg.fit(xtrain, ytrain)
    return reg.predict(xtest)
