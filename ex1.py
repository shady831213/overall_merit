# coding:utf-8
'''
有杭州,昆明,拉萨三个旅游地供选择, 假如选择的标准和依据有:景色,费用,饮食,居住和旅途，哪一个为最佳旅游地点 .

'''
import numpy as np
import overall_merit.ahp as ahp

# Layer1 data
dataL1 = np.mat(([[1.0, 2.0, 7.0, 5.0, 5.0]]))

# Layer2 data
dataL2 = np.mat(([1.0, 2.0, 6.0],
                 [1.0, 1.0 / 3, 1.0 / 8],
                 [1.0, 1.0, 3.0],
                 [1.0, 3.0, 4.0],
                 [1.0, 1.0, 1.0 / 4]))

# build AHP
myAHP = ahp.ahp('myAHP')
layer1 = ahp.ahpLayer('layer1', dataL1)
myAHP.add_layer(layer1)
layer2 = ahp.ahpLayer('layer2', dataL2)
myAHP.add_layer(layer2)

# computation
myAHP.process()

# dump
myAHP.dump()
