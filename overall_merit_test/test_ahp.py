import unittest
import numpy as np

import overall_merit.ahp as dut

class AHPestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGenJudgeArray(self):
        a = np.arange(1.0, 4.0)
        expect = np.array(([1.0, 2.0, 3.0], [1.0 / 2, 1.0, 3.0 / 2], [1.0 / 3, 2.0 / 3, 1.0]))
        actaul = dut.genJudgeArray(a)
        np.testing.assert_array_equal(expect, actaul, 'not equal')

    def testGetEig(self):
        a = dut.genJudgeArray(np.arange(1.0, 4.0))
        expect_value = 2.9999999999999991
        expect_vector = np.array(([ 0.85714286,  0.42857143,  0.28571429]))
        actaul_value, actaul_vector = dut.getEig(a)
        np.testing.assert_almost_equal(actaul_value, expect_value, err_msg='not equal', decimal=10)
        np.testing.assert_array_almost_equal(actaul_vector, expect_vector, err_msg='not equal', decimal=8)


    def testGetEigApp(self):
        a = np.array(([1, 2, 6],[1.0/2, 1, 4], [1.0/6, 1.0/4, 1]))
        b,c = dut.getEigApp(a)
        np.testing.assert_almost_equal(b, 3.0, err_msg='not equal', decimal=10)
        np.testing.assert_array_almost_equal(c, np.array(([[0.58694639,0.32377622,0.08927739]])), err_msg='not equal', decimal=8)


if __name__ == '__main__':
    unittest.main()
