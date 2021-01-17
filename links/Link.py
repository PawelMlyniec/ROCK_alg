

class Link:
    def __init__(self, eps=1):
        self._eps = eps

    def link(self,p_i, p_j):
        pass

    def compute_links(self, cluster_list):
        nbrlist = self.create_nbrlist(cluster_list, self._eps)

        data_size = len(cluster_list)
        link = [[0 for i in range(data_size)] for j in range(data_size)]

        for i in range(data_size):
            N = nbrlist[i]
            for j in range(len(N) - 1):
                for l in range(j+1, len(N)):
                    link[N[j]][N[l]] += 1
        return link

    def create_nbrlist(self, cluster_list, eps):
        data_size = len(cluster_list)

        nbrlist = [[] for j in range(data_size)]
        for i in range(0, data_size):
            for j in range(i + 1, data_size):
                distance = self.is_neighbor(cluster_list[i].points[0].value, cluster_list[i].points[0].value)
                if (distance <= eps):
                    nbrlist[i].append(j)
                    nbrlist[j].append(i)

        return nbrlist

    def is_neighbor(self, first_point, second_point):
        return abs(second_point - first_point)