from rock.cluster import Cluster
from rock.goodnes_measure import GoodnessMeasure
from rock.heap_wrapper import HeapWrapper

link_mat = {
    0: {1: 1,
        2: 1},
    1: {0: 1,
        2: 1},
    2: {0: 1,
        1: 1}
}
cluster1 = Cluster(g=0, id=0, points=[0])
cluster2 = Cluster(g=0, id=1, points=[1])
cluster3 = Cluster(g=0, id=2, points=[2])

def test_build_local_heap():
    gm = GoodnessMeasure()
    heap_wrapper = HeapWrapper(gm)
    local_heap = heap_wrapper.build_local_heap(link_mat, cluster1)
    heap_ids = [1, 2]

    for id, cluster in zip(heap_ids, local_heap):
        assert id == cluster.id


def test_build_global_heap():
    gm = GoodnessMeasure()
    heap_wrapper = HeapWrapper(gm)
    clusters = [
        cluster1,
        cluster2,
        cluster3
    ]

    local_heap_dict = {}
    for cluster in clusters:
        local_heap_dict[cluster.id] = heap_wrapper.build_local_heap(link_mat, cluster)

    global_heap = heap_wrapper.build_global_heap(link_mat, clusters, local_heap_dict)

    heaps_ids = [0,1,2]
    for id, cluster in zip(heaps_ids, global_heap):
        assert id == cluster.id
