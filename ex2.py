# coding:utf-8
'''
3 某儿童医院2004～2008年7项指标的实际值，比较该医院这5年的医疗质量 。
平均住院日、病死率、院内感染率为低优指标，其余为高优指标。

'''
import numpy as np
import overall_merit.topsis as topsis

dataPos = np.array(([21584, 76.7, 78.3, 97.5],
                    [24372, 86.3, 91.1, 98.0],
                    [22041, 81.8, 91.1, 97.3],
                    [21115, 84.5, 90.2, 97.7],
                    [24633, 90.3, 95.5, 97.9]))

dataNeg = np.array(([7.3, 1.01, 2.0],
                    [7.4, 0.8, 2.0],
                    [7.3, 0.62, 3.2],
                    [6.9, 0.6, 2.9],
                    [6.9, 0.25, 3.6]))

y = topsis.getY(dataPos, dataNeg)
print y
