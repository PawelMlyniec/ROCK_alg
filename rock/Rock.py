from links.Link import Link
from heap_wrapper.HeapWrapper import HeapWrapper
from goodnes_measure.GoodnesMeasure import GoodnessMeasure
from claster.claster import *
from heapq import *

class Rock():
    def __init__(self, data, eps, number_of_clasters, threshold=0.5):
        self.q = {}
        self._data = data
        self._eps = eps
        self._number_of_clasters = number_of_clasters
        self._threshold = threshold
        self._adjacency_matrix = self._create_adjacency_matrix()
        self._scaling_factor = 1.0 + 2.0 * ((1.0 - threshold) / (1.0 + threshold))

    def cluster(self, S, k):
        heap_wrapper = HeapWrapper()
        goodens_measure = GoodnessMeasure()
        clusters = to_cluster_list(S)
        #table n x n with number of links

        link2 = Link(eps=4).compute_links2(data=S)
        link3 = Link(eps=4).compute_links3(data=S)
        link = Link(eps=4).compute_links(data=S)

        #array of heaps
        local_heap_dict = {}
        #local_heap_dict2 = {}
        for cluster in clusters:
            #local_heap_dict[cluster.id] = heap_wrapper.build_local_heap(link, cluster)
            local_heap_dict[cluster.id] = heap_wrapper.build_local_heap2(link3, cluster)

        #global heap
        #global_heap = heap_wrapper.build_global_heap(link, clusters, local_heap_dict)
        global_heap = heap_wrapper.build_global_heap2(link3, clusters, local_heap_dict)

        while len(global_heap) > k:
            #take local heap firstly with one cluster
            u = heappop(global_heap)[1]
            v = min(local_heap_dict[u.id])

            heap_wrapper.delete_from_global(global_heap, v.id)

            w = Cluster(g=0, id=max(v.id, u.id)+10, points=u.points + v.points)
            local_heap_dict[w.id] = []
            cluster_heap_union = heap_wrapper.union_of_heaps(local_heap_dict[u.id], local_heap_dict[v.id])

            for x in cluster_heap_union:
                if x.id != u.id and x.id != v.id:
                    gm = goodens_measure.calculate_links2(link3, x, u) + goodens_measure.calculate_links2(link3, x, v)
                    if gm != 0:
                        if x.id in link3:
                            link3[x.id][w.id] = gm
                        else:
                            link3[x.id] = {w.id: gm}
                        if w.id in link3:
                            link3[w.id][x.id] = gm
                        else:
                            link3[w.id] = {x.id: gm}

                    heap_wrapper.delete_from_local(local_heap_dict[x.id], u.id)
                    heap_wrapper.delete_from_local(local_heap_dict[x.id], v.id)
                    goodnes = goodens_measure.g2(link3, x, w)
                    heap_wrapper.insert(local_heap_dict[x.id], w, goodnes)
                    heap_wrapper.insert(local_heap_dict[w.id], x, goodnes)
                    heap_wrapper.update(global_heap, x, local_heap_dict[x.id], link3)

            heap_wrapper.insert_global(global_heap, w, link3, local_heap_dict)
            del local_heap_dict[u.id]
            del local_heap_dict[v.id]
            link2_keys = list(link3.keys())
            for i in link2_keys:
                if i == u.id or i == v.id:
                    del link3[i]
                else:
                    link2_i_keys = list(link3[i].keys())
                    for j in link2_i_keys:
                        if j == u.id or j == v.id:
                            del link3[i][j]

    def _create_adjacency_matrix(self):
        data_size = len(self._data)
        adjacency_matrix = [[0 for i in range(data_size)] for j in range(data_size)]
        return adjacency_matrix


