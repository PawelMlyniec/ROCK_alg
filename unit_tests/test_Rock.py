from rock.rock import Rock
import numpy as np

def test_claster():
    rock = Rock(is_cat=False, threshold=0.8)
    clusers = rock.cluster(np.array([[0],[1],[2],[3],[4],[5],
                            [10],[11],[12],[13],[14],
                            [15], [100]]), 3)
    assert len(clusers) == 3
