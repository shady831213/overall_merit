import numpy as np
from numpy.matlib import repmat

def normalization(a):
    #sqrt of sum of **2 by col
    v = np.sum(a, axis=0)
    return (a / repmat(v,a.shape[0], 1))

#generate judge array
def genJudgeArray(vector):
    a = repmat(vector, vector.size, 1)
    return a/a.T

#get eigvector and eigvelue
def getEig(a):
    b,c = np.linalg.eig(a)
    idx = b.argmax()
    return (b[idx], c[:,idx])
#get eigvector and eigvelue approximate
def getEigApp(a):
    b = np.sum(normalization(a),axis=1)
    c = np.asarray(normalization(np.asmatrix(b).T).T)
    lamb = (1.0/c.size) * np.sum(b/c)
    return (lamb,c)

#consistency check
def checkCon(lamb, n):
    # n > 0
    if (n < 1):
        raise ValueError('n should be more than 1, but is %d'%(n))
    #               1  2  3     4      5    6     7     8     9     10
    ri = np.array(([0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49,
                    1.51, 1.54, 1.56, 1.58, 1.59, 1.5943, 1.6064, 1.6133, 1.6207, 1.6292,
                    1.6385, 1.6403, 1.6462, 1.6497, 1.6556, 1.6587, 1.6631, 1.667, 1.6693, 1.6724]))
    ci = (lamb - n) / n - 1
    cr = ci/ri[n-1]
    return (cr<0.1)

class ahpCell:
    def __init__(self, name = ''):
        self._name = name

    def get_judgeVector(self):
        return self._judgeVector

    def set_judgeVector(self, value):
        self._judgeVector = value

    def get_name(self):
        return self._name

    def get_conStatus(self):
        return self._conStatus

    def get_eigVector(self):
        return self._eigVector

    def process(self):
        #self._judgeArray = normalization(genJudgeArray(self._judgeVector))
        self._judgeArray = genJudgeArray(self._judgeVector)
        #self._lamb, self._eigVector = getEig(self._judgeArray)
        self._lamb, self._eigVector = getEigApp(self._judgeArray)
        self._conStatus = checkCon(self._lamb, self._judgeVector.size)
        return (self._conStatus, self._eigVector)

    #dump members
    def dump(self):
        np.set_printoptions(precision=5)
        print '---------------------------------------------------'
        print (self._name)
        print '---------------------------------------------------'
        print '###################################################'
        for name, value in vars(self).items():
            if (name == '_name') :
                continue
            print ('%s='%(name))
            print (value)
            print '###################################################'


class ahpLayer:
    def __init__(self, name, data, dLayer = None):
        self._name = name
        self._cells = []
        self._data = data
        self._dLayer = dLayer

    def get_name(self):
        return self._name

    def set_dLayer(self, dLayer):
        self._dLayer = dLayer

    def get_dLayer(self):
        return self._dLayer

    # def build(self):
    #     for i in range(self._data.shape(0)) :
    #         cell = ahpCell('item%0d'%(i))
    #         cell.set_judgeVector(self._data[i,:])
    #         self._cells.append(cell)
    #     if (self._dLayer) :
    #         self._dLayer.build()

    def process(self):
        my_result = np.zeros(self._data.shape)
        for i in range(self._data.shape[0]):
            cell = ahpCell('item%0d' % (i))
            cell.set_judgeVector(np.asarray(self._data[i, :]))
            conStatus, eigVector = cell.process()
            if (not conStatus):
                raise ValueError('consistency check in %s\.%s failed'%(self._name, cell.get_name()))
            my_result[i, :] = eigVector
            self._cells.append(cell)
        if (self._dLayer) :
            d_result = self._dLayer.process()
            self._result = np.dot(my_result,d_result)
            return self._result
        else :
            self._result = my_result
            return self._result


    # dump members
    def dump(self):
        print '==================================================='
        print (self._name)
        print ('_result = ')
        print (self._result)
        print '==================================================='
        for cell in self._cells:
            cell.dump()
        if (self._dLayer) :
            self._dLayer.dump()

class ahp :
    def __init__(self, name):
        self._name = name
        self._top = None

    def add_layer(self, Layer):
        if (not self._top) :
            self._top = Layer
        else :
            self._end.set_dLayer(Layer)
        self._end = Layer


    def process(self):
        self._result = self._top.process()
        return self._result

    def dump(self):
        print '***************************************************'
        print (self._name)
        print ('_result = ')
        print (self._result)
        print '***************************************************'
        self._top.dump()

