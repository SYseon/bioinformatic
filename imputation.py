# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn.impute import SimpleImputer


class MissingValue():
    
    def __init__(self, df:pd.DataFrame, i_mthd):
        self.dataframe = df
        if i_mthd == 0:
            #drop
            self.imputation = False
        elif i_mthd == 1:
            #mean
            self.imputation = SimpleImputer()
        elif i_mthd == 2:
            #most_frequent 
            self.imputation = SimpleImputer(strategy = "most_frequent")
        
        
    def run(self):
        if self.imputation == False:
            return self.dataframe.dropna()
        return self.imputation.fit_transform(self.dataframe)