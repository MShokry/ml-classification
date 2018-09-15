#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:56:56 2017

@author: mshokry
"""

import numpy as np

x = np.array([2.5,0.3,2.8,0.5])
y = np.array([1,-1,1,1])
w = np.array([1])

# product of p(y|x,w)
#1/(1+exp(-wT h(xi)))
def p(x,w):
    return 1/(1+np.exp(-(w.T*x)))

py_plus = p(x,w)
py = (y==-1)*(1-p(x))+(y==1)*(p(x,w))
#Liklehood of py => product of p(y|x,w)
np.prod(py)
#0.23
#Derivative of l => sum(h(x)* if(y=1)-p(y=+1|x,w) )
pp = (1*(y==1) - py_plus)
dl = np.sum(x*pp)
round(dl,2)
#0.37
