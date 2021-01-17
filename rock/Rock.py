from links import Link
from heap_wrapper import HeapWrapper
from goodnes_measure import GoodnesMeasure
from claster.claster import *


class Rock():
    def __init__(self, data, eps, number_of_clasters, threshold=0.5):
        self.q = {}
        self._data = data
        self._eps = eps
        self._number_of_clasters = number_of_clasters
        self._threshold = threshold
        self._adjacency_matrix = self._create_adjacency_matrix()
        self._scaling_factor = 1.0 + 2.0 * ((1.0 - threshold) / (1.0 + threshold))

    def claster(self, S, k):
        heap_wrapper = HeapWrapper()

        S = to_cluster_list(S)

        #table n x n with number of links
        link = Link.compute_links(S)

        #array of heaps
        q = {}
        for index, s in S:
            q[tuple(s)] = heap_wrapper.build_local_heap(link, index, s)

        #global heap
        Q = heap_wrapper.build_global_heap(S, q)

        while Q.size() > k:
            u = heap_wrapper.extract_max(Q)
            v = heap_wrapper.max(q[u])
            heap_wrapper.delete(Q, v)
            w = marge(u, v)

            for x in sum(q[u], q[v]):
                link_x_w = Link.link(x, u) + Link.link(x, v)
                heap_wrapper.delete(q[x], u)
                heap_wrapper.delete(q[x], v)
                heap_wrapper.insert(q[x], w, GoodnesMeasure.g(x, w))
                heap_wrapper.insert(q[w], x, GoodnesMeasure.g(x, w))
                heap_wrapper.update(Q, x, q[x])

            heap_wrapper.insert(Q, w, q[w])
            heap_wrapper.deallocate(q[u])
            heap_wrapper.deallocate(q[v])

    def _create_adjacency_matrix(self):
        data_size = len(self._data)
        adjacency_matrix = [[0 for i in range(data_size)] for j in range(data_size)]
        return adjacency_matrix


