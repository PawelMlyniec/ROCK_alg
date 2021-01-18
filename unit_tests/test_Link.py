from rock.link import Link


def test_create_nbrlist():
    data = [3, 5, 7]
    eps = 2
    link = Link(eps)

    nbrlist = link.create_nbrlist(data, eps)

    true_nbrlist = [[1],
                    [0,2],
                    [1]]
    assert nbrlist == true_nbrlist


def test_compute_links():
    data = [3, 5, 7]
    eps = 4
    link = Link(eps)

    link_mat = link.compute_links(data)
    true_link_mat = [[0,1,1],
                     [0,0,1],
                     [0,0,0]]
    assert link_mat == true_link_mat