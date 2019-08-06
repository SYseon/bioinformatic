#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 00:39:33 2019

@author: seon
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

class Preprocessor():
    def __init__(self, df:pd.DataFrame):
        self.df = df
        
    def ohe_run(self, Auto = True, OHE_idx = None):
        #OneHotEncoding
        if Auto == True:
            arr = np.array(self.df)
            temp = np.array([])
            for i in range(arr.shape[1]):
                temp = np.append(temp, len(np.unique(arr[:,i])))
            OHE_idx = np.where(temp < 7)[0]
        OHE_df = self.df.iloc[:, [OHE_idx]]
        enc = OneHotEncoder()
        OHE_df = enc.fit_transform(OHE_df).toarray()
        OHE_df = pd.DataFrame(OHE_df)
        self.df = self.df.drop(OHE_idx, axis = 1)
        self.df = pd.concat(OHE_df, self.df)
        return self.df
        
    def prp_run(self, prp_mth):
        #Prerprocessing
        if prp_mth == 0:
            scaler = MinMaxScaler()
        elif prp_mth == 1:
            scaler = StandardScaler()
        self.df = scaler.fit_transform(self.df)
        return self.df