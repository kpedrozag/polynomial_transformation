#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:31:36 2018

@author: ceisutb17
"""
import numpy as np


def polynomial_feature(grade):
    dataSet = np.loadtxt("ex2data1.txt",delimiter=',')
    X = dataSet[:,0]
    
    changes = np.zeros(X.shape)
    
    #changes = []
    #y=dataSet[:,1]
    if grade >= 2:
        for i in range(1, grade):
            aux = False
            aux = np.array(0)
            for value in X:
                aux = np.append(aux, value**(i+1))
            aux = np.delete(aux, 0)
            print("aux",aux.shape)
            X = np.c_[X, aux]
            print("x", X.shape)
    elif grade == 1:
        pass
        #return X
    else:
        pass
        #return "Error"
    
    print(X)


if __name__ == '__main__':
    polynomial_feature(3)