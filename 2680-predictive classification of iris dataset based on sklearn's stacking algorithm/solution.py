# coding: utf-8
from numpy import ndarray
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import StackingClassifier


class Stacking(object):
    def __init__(self) -> None:
        """
        In this function you need to initialize the StackingClassifier from sklearn
        """
        # write your code here
        estimators = [
            ('kn', KNeighborsClassifier()),
            ('mnb', MultinomialNB()),
            ('rf', RandomForestClassifier())
        ]
        final_estimator = LogisticRegression()
        self.model = StackingClassifier(estimators=estimators, final_estimator=final_estimator)

    def fit_data(self, x_train: ndarray, y_train: ndarray) -> None:
        """
        In this function you need to fit the input data and label to the KNN classifier
        :param x_train: Input data which format is ndarray
        :param y_train: Input label which format is ndarray
        """
        # write your code here
        self.model.fit(x_train, y_train)

    def predict_data(self, x_test: ndarray) -> ndarray:
        """
        In this function you need to use StackingClassifier to predict input test data
        :param x_test: Input test data which format is ndarray
        :return: The predicted label for input test data which format is ndarray
        """
        # write your code here
        return self.model.predict(x_test)