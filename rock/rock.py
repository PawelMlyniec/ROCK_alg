from rock.link import Link
from rock.heap_wrapper import HeapWrapper
from rock.goodnes_measure import GoodnessMeasure
from rock.cluster import *
from heapq import *
import numpy as np

class Rock():
    def __init__(self, is_cat, threshold=0.5):
        self.threshold = threshold
        self._eps = threshold
        self._scaling_factor = 1.0 + 2.0 * ((1.0 - self.threshold) / (1.0 + self.threshold))
        self._is_cat = is_cat

    def cluster(self, S, k):
        goodens_measure = GoodnessMeasure(self.threshold)
        heap_wrapper = HeapWrapper(goodens_measure)

        clusters = to_cluster_list(S)

        link_mat = Link(self._is_cat).compute_links(data=S, eps=self._eps)
        max_index = len(S)

        local_heap_dict = {}

        for cluster in clusters:
            local_heap_dict[cluster.id] = heap_wrapper.build_local_heap(link_mat, cluster)

        global_heap = heap_wrapper.build_global_heap(link_mat, clusters, local_heap_dict)

        while len(global_heap) > k:
            if len(global_heap) % 20 == 0:
                print(len(global_heap))
            if len(link_mat) == 0:
                break
            u = heappop(global_heap)
            v = min(local_heap_dict[u.id])

            heap_wrapper.delete(global_heap, v.id)
            max_index+=1
            w = Cluster(g=0, id=max_index, points=u.points + v.points)
            local_heap_dict[w.id] = []
            cluster_heap_union = heap_wrapper.union_of_heaps(local_heap_dict[u.id], local_heap_dict[v.id])

            for x in cluster_heap_union:
                if x.id != u.id and x.id != v.id:
                    gm = goodens_measure.calculate_links(link_mat, x, u) + goodens_measure.calculate_links(link_mat, x, v)
                    if gm != 0:
                        if x.id in link_mat:
                            link_mat[x.id][w.id] = gm
                        else:
                            link_mat[x.id] = {w.id: gm}
                        if w.id in link_mat:
                            link_mat[w.id][x.id] = gm
                        else:
                            link_mat[w.id] = {x.id: gm}

                    heap_wrapper.delete(local_heap_dict[x.id], u.id)
                    heap_wrapper.delete(local_heap_dict[x.id], v.id)
                    goodnes = goodens_measure.gm(link_mat, x, w)
                    heap_wrapper.insert(local_heap_dict[x.id], w, goodnes)
                    heap_wrapper.insert(local_heap_dict[w.id], x, goodnes)
                    heap_wrapper.update(global_heap, x, local_heap_dict[x.id], link_mat)

            heap_wrapper.insert_global(global_heap, w, link_mat, local_heap_dict)
            del local_heap_dict[u.id]
            del local_heap_dict[v.id]
            link2_keys = list(link_mat.keys())
            for i in link2_keys:
                if i == u.id or i == v.id:
                    del link_mat[i]
                else:
                    if u.id in link_mat[i]:
                        del link_mat[i][u.id]
                    elif v.id in link_mat[i]:
                        del link_mat[i][v.id]
                    if len(link_mat[i]) == 0:
                        del link_mat[i]

        return global_heap



