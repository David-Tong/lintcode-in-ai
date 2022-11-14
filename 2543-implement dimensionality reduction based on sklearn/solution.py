# coding: utf-8
import pandas as pd
from pandas import DataFrame
from numpy import ndarray

from sklearn.decomposition import PCA

def dimensionality_reduction(input_data: DataFrame) -> ndarray:
    """
    In this function you need to initialize the KNN classifier from sklearn
    :param input_data: Input data which data type is DataFrame
    :return: Data after dimensionality reduction which data type should be ndarray
    """
    # write your code here
    pca = PCA(n_components=2)
    pca.fit(input_data)
    return pca.fit_transform(input_data)