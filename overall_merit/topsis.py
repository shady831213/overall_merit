'''
3 某儿童医院2004～2008年7项指标的实际值，比较该医院这5年的医疗质量 。


'''

import numpy as np
from numpy.matlib import repmat

def normalization(a):
    #sqrt of sum of **2 by col
    v = np.sqrt(np.sum(np.asarray(a)**2, axis=0))
    return (a / repmat(v,a.shape[0], 1))

def getBestVector(a):
    return np.max(a,axis=0)

def getWorstVector(a):
    return np.min(a,axis=0)

def getDis(a, z):
    v = a - repmat(z, a.shape[0], 1)
    return np.sqrt(np.sum(np.asarray(v)**2, axis=1))

def getY(a, b):
    zPos = np.append(getBestVector(normalization(a)), getWorstVector(normalization(b)))
    zNeg = np.append(getWorstVector(normalization(a)), getBestVector(normalization(b)))
    dPos = getDis(normalization(np.append(a, b,axis=1)), zPos)
    dNeg = getDis(normalization(np.append(a, b,axis=1)), zNeg)
    Y=dNeg/(dPos + dNeg)
    return Y
