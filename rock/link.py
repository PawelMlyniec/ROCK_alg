

class Link:
    def __init__(self, eps=1):
        self._eps = eps

    def compute_links(self, data):
        nbrlist = self.create_nbrlist(data, self._eps)

        data_size = len(data)
        link = {}

        for i in range(data_size):
            N = nbrlist[i]
            for j in range(len(N) - 1):
                for l in range(j+1, len(N)):

                    if N[j] in link:
                        if N[l] in link[N[j]]:
                            link[N[j]][N[l]] += 1
                        else:
                            link[N[j]][N[l]] = 1
                    else:
                        link[N[j]] = {N[l]: 1}

                    if N[l] in link:
                        if N[j] in link[N[l]]:
                            link[N[l]][N[j]] += 1
                        else:
                            link[N[l]][N[j]] = 1
                    else:
                        link[N[l]] = {N[j]: 1}

        return link

    def create_nbrlist(self, data, eps):
        data_size = len(data)

        nbrlist = [[] for j in range(data_size)]
        for i in range(0, data_size):
            for j in range(i + 1, data_size):
                distance = self.is_neighbor(data[i], data[j])
                if distance <= eps:
                    nbrlist[i].append(j)
                    nbrlist[j].append(i)

        return nbrlist

    def is_neighbor(self, first_point, second_point):
        return abs(second_point - first_point)
