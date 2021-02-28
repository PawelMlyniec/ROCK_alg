from rock.cluster import Cluster
from rock.goodnes_measure import GoodnessMeasure


def test_calculate_links():
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

    gm = GoodnessMeasure()
    true_link_num = 1
    link_num = gm.calculate_links(link=link_mat, cluster1=cluster1, cluster2=cluster2)

    assert true_link_num == link_num

def test_gm():
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

    gm = GoodnessMeasure()
    true_gm_val = 0.1364
    gm_val = gm.gm(link=link_mat, cluster1=cluster1, cluster2=cluster2)
    assert abs(true_gm_val - gm_val) < 0.0001

