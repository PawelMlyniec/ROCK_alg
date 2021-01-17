import collections
from collections import namedtuple  

Cluster = namedtuple('Cluster', ['g', 'points'])
Point = namedtuple('Point', ['index', 'value'])


def to_cluster_list(S):
    cluster_list = []
    for i, s in enumerate(S):
        cluster_list.append(Cluster(g=0, points=[Point(index=i, value=s)]))
    return cluster_list
