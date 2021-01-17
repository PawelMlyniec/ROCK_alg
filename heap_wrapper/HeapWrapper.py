from goodnes_measure.GoodnesMeasure import GoodnesMeasure
from claster.claster import Claster
from heapq import *

class HeapWrapper():
    def __int__(self):
        pass

    def build_local_heap(self, link, index, s):
        claster = (-0, [[index, s]])
        q = []
        heappush(q, claster)
        return q


    def build_global_heap(self, link, S, q):
        goodenss_measure = GoodnesMeasure()
        Q = []
        for s in S:
            max_cluster = nsmallest(1, q[tuple(s)])
            g = goodenss_measure.g(link, )

    def extract_max(self, Q):
        pass

    def max(self, local_heap):
        pass

    def delete(self, local_heap, u):
        pass

    def insert(self, local_heap, w, goodenss_measure):
        pass

    def update(self, Q, w, local_heap):
        pass

    def deallocate(self, local_heap):
        pass