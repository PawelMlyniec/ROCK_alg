from rock.link import Link
import numpy as np

def test_create_nbrlist():
    data = np.array([[3], [5], [7]])
    eps = 0.5
    link = Link(is_cat=False)

    nbrlist = link.create_nbrlist(data, eps)

    true_nbrlist = [[1],
                    [0,2],
                    [1]]
    assert nbrlist == true_nbrlist

def test_compute_links():
    data = np.array([[3], [5], [7], [15]])
    eps = 0
    link = Link(is_cat=False)

    link_mat = link.compute_links(data, eps)
    true_link_mat = {
        0: {1: 1,
            2: 1},
        1: {0: 1,
            2: 1},
        2: {0: 1,
            1: 1}
    }
    assert link_mat == true_link_mat

def test_compute_links():
    data = np.array([[3], [5], [8], [9]])
    eps = 0.3
    link = Link(is_cat=False)

    link_mat = link.compute_links(data, eps)
    true_link_mat = {
        0: {2: 1,
            3: 1},
        1: {3: 1,
            2: 1},
        2: {1: 1,
            3: 1,
            0: 1},
        3: {2: 1,
            1: 1,
            0: 1}
    }
    assert link_mat == true_link_mat