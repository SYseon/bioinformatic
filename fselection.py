#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 04:00:05 2019

@author: seon
"""

from sklearn.svm import LinearSVC
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA
import pandas as pd

class Fselection():
    def __init__(self, X:pd.DataFrame, y:pd.DataFrame):
        self.X = X
        self.y = y
    
    def var(self, threshold): 
        sel = VarianceThreshold(threshold)
        self.X = sel.fit_transform(self.x)
        return self.X
    
    def wrapper(self, clf_idx, clf_prm1 = 0.01,  clf_prm2 = 50):
        if clf_idx == 0:
            clf = LinearSVC(C=clf_prm1, penalty = "l1", dual = False).fit(self.X, self.y)
        elif clf_idx == 1:
            clf = ExtraTreesClassifier(n_estimators=clf_prm2).fit(self.X, self.y)
        model = SelectFromModel(clf, prefit = True)
        self.X = model.transform(self.X)
        return self.X
    
    def pca(self, n_cpnt):
        model = PCA(n_cpnt)
        self.X = model.fit_transform(self.X)
        return self.X