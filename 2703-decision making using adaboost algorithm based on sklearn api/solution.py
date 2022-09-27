#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numpy import ndarray
import numpy as np
from sklearn.ensemble import AdaBoostClassifier


def adaboost_sklearn(x_train: ndarray, y_train: ndarray, x_test: ndarray) -> ndarray:
    """
    :param xtrain: Training set X
    :param ytrain: Training set Y
    :param xtest: Testing set X
    :return: Return the prediction you got from model
    """
    # -- write your code here --
    model = AdaBoostClassifier()
    model.fit(x_train, y_train)
    return model.predict(x_test)






