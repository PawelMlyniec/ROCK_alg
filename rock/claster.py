import collections
from collections import namedtuple  

Cluster = namedtuple('Cluster', ['g', 'id', 'points'])

def to_cluster_list(S):
    cluster_list = []
    for i, s in enumerate(S):
        cluster_list.append(Cluster(g=0, id=i, points=[i]))
    return cluster_list
