import numpy as np

class Link:
    def __init__(self, is_cat):
        self.is_cat = is_cat

    def compute_links(self, data, eps):
        nbrlist = self.create_nbrlist(data, eps)

        data_size = len(data)
        link = {}

        for i in range(data_size):
            N = nbrlist[i]
            if i %100 == 0:
                print(f"links: {i}/{data_size}")
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
        scaling = 1
        if self.is_cat  == False:
            min = np.array([np.min(data) for p in range(len(data[0]))])
            max = np.array([np.max(data) for p in range(len(data[0]))])
            max_val = np.linalg.norm(min - max)
            scaling = max_val

        nbrlist = [[] for j in range(data_size)]
        for i in range(0, data_size):
            for j in range(i + 1, data_size):
                distance = self.is_neighbor(data[i], data[j], scaling)
                if distance >= eps:
                    nbrlist[i].append(j)
                    nbrlist[j].append(i)

        return nbrlist

    def is_neighbor(self, first_point, second_point, scaling):
        if self.is_cat:
            same = 0
            for i, j in zip(first_point, second_point):
                if i == j:
                    same += 1
            union = len(first_point)

            return same / union
        else:
            return (scaling-np.linalg.norm(first_point-second_point))/scaling


