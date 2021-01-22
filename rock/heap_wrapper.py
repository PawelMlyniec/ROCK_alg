from rock.goodnes_measure import GoodnessMeasure
from heapq import *
from rock.cluster import *

class HeapWrapper():
    def __init__(self, goodens_measure):
        self._goodens_measure =goodens_measure

    def build_local_heap(self, link, cluster):
        local_heap = []
        i = cluster.id
        if i in link:
            for j in link[i].keys():
                cluster2 = Cluster(g=0, id=j, points=[j])
                goodnes = self._goodens_measure.gm(link, cluster, cluster2)
                cluster2 = Cluster(g=-goodnes, id=j, points=[j])
                heappush(local_heap, cluster2)

        return local_heap

    def build_global_heap(self, link, clusters, local_heap_dict):
        global_heap = []
        for cluster in clusters:
            local_heap = local_heap_dict[cluster.id]
            if len(local_heap) != 0:
                max_cluster = min(local_heap)
                g = self._goodens_measure.gm(link, cluster, max_cluster)
                heappush(global_heap, Cluster(g=-g, id=cluster.id, points=cluster.points))
            else:
                heappush(global_heap, Cluster(g=0, id=cluster.id, points=cluster.points))

        return global_heap

    def delete(self, heap, cluster_id):
        for i, value in enumerate(heap):
            if value.id == cluster_id:
                del heap[i]
                heapify(heap)
                break


    def union_of_heaps(self, first_heap, second_heap):
        sum_of_clasters = []
        for cluster in first_heap:
            sum_of_clasters.append(cluster)
        for cluster in second_heap:
            sum_of_clasters.append(cluster)
        d = {x.id: x for x in sum_of_clasters}

        return list(d.values())

    def insert(self, heap, cluster, goodenss_measure):
        heappush(heap, Cluster(g=-goodenss_measure, id=cluster.id, points=cluster.points))

    def insert_global(self, heap, cluster, link, local_heap_dict):
        local_heap = local_heap_dict[cluster.id]
        if len(local_heap) != 0:
            max_cluster = min(local_heap)
            g = self._goodens_measure.gm(link, cluster, max_cluster)
            heappush(heap, Cluster(g=-g, id=cluster.id, points=cluster.points))
        else:
            heappush(heap, Cluster(g=0, id=cluster.id, points=cluster.points))

    def update(self, global_heap, cluster, local_heap, link):
        if len(local_heap) != 0:
            max_cluster = min(local_heap)
            g = self._goodens_measure.gm(link, cluster, max_cluster)
            for i, c in enumerate(global_heap):
                if c.id == cluster.id:
                    global_heap[i] = Cluster(g=-g, id=cluster.id, points=cluster.points)
                    heapify(global_heap)
                    break
        else:
            for i, value in enumerate(global_heap):
                if value[1].id == cluster.id:
                    global_heap[i] = Cluster(g=0, id=cluster.id, points=cluster.points)
                    heapify(global_heap)
                    break
