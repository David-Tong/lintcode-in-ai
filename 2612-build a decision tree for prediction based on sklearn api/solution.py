#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numpy import mod, ndarray
from sklearn.tree import DecisionTreeClassifier


def decision_tree(x_train: ndarray, y_train: ndarray, x_test: ndarray) -> ndarray:
    """
    :param xtrain: Training set X
    :param ytrain: Training set Y
    :param xtest: Testing set X
    :return: Return the prediction you got from model
    """
    # -- write your code here --
    clf = DecisionTreeClassifier()
    clf = clf.fit(x_train, y_train)
    return clf.predict(x_test)






