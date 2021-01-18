class GoodnessMeasure:
    def __init__(self):
        self._threshold = 0.5
        self._scaling_factor = 1.0 + 2.0 * ((1.0 - self._threshold) / (1.0 + self._threshold))

    def gm(self, link, cluster1, cluster2):
        number_links = self.calculate_links(link, cluster1, cluster2)
        n = len(cluster1)
        m = len(cluster2)
        divider = (n + m) ** self._scaling_factor - n ** self._scaling_factor - m ** self._scaling_factor

        return number_links / divider

    def calculate_links(self, link, cluster1, cluster2):
        number_links = 0

        for index1 in cluster1.points:
            for index2 in cluster2.points:
                if index1 in link:
                    if index2 in link[index1]:
                        number_links += link[index1][index2]

        return number_links

