from goodnes_measure.GoodnesMeasure import GoodnessMeasure
from heapq import *
from claster.claster import *


class HeapWrapper():
    def __init__(self):
        pass

    def build_local_heap(self, link, cluster):
        goodens_measure = GoodnessMeasure()
        local_heap = []
        i = cluster.id
        for j in range(len(link[i])):
            if link[i][j] != 0:
                cluster2 = Cluster(g=0, id=j, points=[j])
                goodnes = goodens_measure.g(link, cluster, cluster2)
                cluster2 = Cluster(g=-goodnes, id=j, points=[j])
                heappush(local_heap, cluster2)

        return local_heap

    def build_local_heap2(self, link, cluster):
        goodens_measure = GoodnessMeasure()
        local_heap = []
        i = cluster.id
        if i in link:
            for j in link[i].keys():
                cluster2 = Cluster(g=0, id=j, points=[j])
                goodnes = goodens_measure.g2(link, cluster, cluster2)
                cluster2 = Cluster(g=-goodnes, id=j, points=[j])
                heappush(local_heap, cluster2)

        return local_heap


    def build_global_heap(self, link, clusters, local_heap_dict):
        goodness_measure = GoodnessMeasure()
        global_heap = []
        for cluster in clusters:
            local_heap = local_heap_dict[cluster.id]
            if len(local_heap) != 0:
                max_cluster = min(local_heap)
                g = goodness_measure.g(link, cluster, max_cluster)
                heappush(global_heap, (-g, cluster))
            else:
                heappush(global_heap, (0, cluster))

        return global_heap

    def build_global_heap2(self, link, clusters, local_heap_dict):
        goodness_measure = GoodnessMeasure()
        global_heap = []
        for cluster in clusters:
            local_heap = local_heap_dict[cluster.id]
            if len(local_heap) != 0:
                max_cluster = min(local_heap)
                g = goodness_measure.g2(link, cluster, max_cluster)
                heappush(global_heap, (-g, cluster))
            else:
                heappush(global_heap, (0, cluster))

        return global_heap

    def delete_from_global(self, heap, cluster_id):
        for i, value in enumerate(heap):
            if value[1].id == cluster_id:
                del heap[i]
                break
        heapify(heap)

    def delete_from_local(self, heap, cluster_id):
        for i, value in enumerate(heap):
            if value.id == cluster_id:
                del heap[i]
                break
        heapify(heap)

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
        goodness_measure = GoodnessMeasure()
        local_heap = local_heap_dict[cluster.id]
        if len(local_heap) != 0:
            max_cluster = min(local_heap)
            g = goodness_measure.g2(link, cluster, max_cluster)
            heappush(heap, (-g, cluster))
        else:
            heappush(heap, (0, cluster))

    def update(self, global_heap, cluster, local_heap, link):
        goodness_measure = GoodnessMeasure()
        if len(local_heap) != 0:
            max_cluster = min(local_heap)
            g = goodness_measure.g2(link, cluster, max_cluster)
            for i, value in enumerate(global_heap):
                if value[1].id == cluster.id:
                    global_heap[i] = (-g, cluster)
                    break
        else:
            heappush(global_heap, (0, cluster))
            for i, value in enumerate(global_heap):
                if value[1].id == cluster.id:
                    global_heap[i] = (0, cluster)
                    break
        heapify(global_heap)

    def deallocate(self, local_heap):
        pass