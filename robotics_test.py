"""
Title: Unit test for robotics.py
03/03/2021
Ming-Yun (Ann) Tsai

Total Tests: 4
"""

import unittest
import robotics



class TestError(unittest.TestCase):

    """
    TEST INVALID D : 
	when D < 0
    """
    def test_D_error(self):
        D = -3
        with self.assertRaises(SystemExit) as err: 
            robotics.D_check(D)
        self.assertEqual(err.exception.code, 1)


class TestProgram(unittest.TestCase):

    """
    TEST ENTIRE PROGRAM : 
	Running through both RangeFilter and TemporalMedianFilter
    """
    def test_whole(self):

        scans = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
        right_output =  [[0.03, 1.0, 2.0, 1.0, 3.0], [0.515, 3.0, 3.5, 1.0, 3.0], [1.0, 3.0, 4.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0], [2.5, 3.0, 4.0, 1.0, 1.515]]
        
        N = len(scans[0])
        obj_1 = robotics.RangeFilter()
        obj_2 = robotics.TemporalMedianFilter(3, N)

        result = []

        for scan in scans:
            result.append(obj_2.update(obj_1.update(scan)))
        
        self.assertEqual(result, right_output)

    """
    TEST RangeFilter
    """
    def test_range_filter(self):

        scans = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
        right_output = [[0.03, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 5.0, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 0.03], [3.0, 3.0, 3.0, 1.0, 3.0], [5, 2.0, 4.0, 0.03, 0.03]]

        obj = robotics.RangeFilter()
        result = []

        for scan in scans:
            result.append(obj.update(scan))

        self.assertEqual(result, right_output)

    """
    TEST TemporalMedianFilter
    """
    def test_temporal_median_filter(self):

        scans = [[0.03, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 5.0, 1.0, 3.0], [2.0, 3.0, 4.0, 1.0, 0.03], [3.0, 3.0, 3.0, 1.0, 3.0], [5, 2.0, 4.0, 0.03, 0.03]]
        right_output =  [[0.03, 1.0, 2.0, 1.0, 3.0], [0.515, 3.0, 3.5, 1.0, 3.0], [1.0, 3.0, 4.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0], [2.5, 3.0, 4.0, 1.0, 1.515]]

        N = len(scans[0])
        obj = robotics.TemporalMedianFilter(3, N)
        result = []

        for scan in scans:
            result.append(obj.update(scan))

        self.assertEqual(result, right_output)



if __name__ == "__main__":

    unittest.main(exit = False, verbosity = 2) # without calling sys.exit, with more details



