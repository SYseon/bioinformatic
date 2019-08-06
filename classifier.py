#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 04:27:42 2019

@author: seon
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


class Classifier():
    def __init__(self, X, y, clf_idx, clf_prm1 = None, cfl_prm2 None):
        self.X = X
        self.y = y
    
    def 