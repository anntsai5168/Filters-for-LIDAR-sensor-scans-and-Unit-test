"""
Title: Filters for LIDAR sensor scans
03/03/2021
Ming-Yun (Ann) Tsai

P.S.
In the attachment, it says that "Each scan is as array of length N of float value......".
However, it also says that "Measured distances are typically in a range of [0.03, 50] meters". 
I'm not sure this is a typo or not, therefore, I assumed that the range is [0.03, 5.0].
"""

import numpy as np
import collections as cl
import sys



"""
Error Handling
"""
# D check : if D < 0, then exit the programm
def D_check(D):
    if D < 0:
        print "ERROR : D must bigger than zero."
        exit(1)


"""
Filters
"""

class Filter:

    def update(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class RangeFilter(Filter):

    range_min = 0.03
    range_max = 5.0

    def update(self, scan):
        for i in range(len(scan)):
            scan[i] = max(min(scan[i], self.range_max), self.range_min)
        return scan


class TemporalMedianFilter(Filter):
    

    def __init__(self, D, N):
        self.D = D
        self.N = N
        self.result = [] # store all the queues

        # check the value of D
        D_check(self.D)
        
        # queue, max size  = D
        for i in range(self.N):
            self.queue = cl.deque(maxlen = self.D+1)
            self.result.append(self.queue)
    

    def update(self, scan):

        output = []
        for i in range(self.N):
            self.result[i].append(scan[i]) # transpose & update result
            output.append(round(np.median(self.result[i]),3))
        return output



"""
MAIN
"""
if __name__ == '__main__':
    
    scans = [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
    N = len(scans[0])

    # create RangeFilter object
    obj_1 = RangeFilter()
    # create TemporalMedianFilter object
    obj_2 = TemporalMedianFilter(3, N)

    for scan in scans:
        #print scan, 'scan'

        # filter the scan
        af_range_filter = obj_1.update(scan) # return input for Temporal Median Filter
        final_output = obj_2.update(af_range_filter) # return final output

        #print af_range_filter, 'after RangeFilter', '\n', final_output, 'final output', '\n', "--------------------------------"

