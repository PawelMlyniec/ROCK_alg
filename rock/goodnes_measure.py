

class GoodnessMeasure:
    def __init__(self, threshold=0.5):
        self._threshold = threshold
        self._scaling_factor = 1.0 + 2.0 * ((1.0 - self._threshold) / (1.0 + self._threshold))

    def gm(self, link, cluster1, cluster2):
        number_links = self.calculate_links(link, cluster1, cluster2)
        n = len(cluster1)
        m = len(cluster2)
        divider = (n + m) ** self._scaling_factor - n ** self._scaling_factor - m ** self._scaling_factor

        return number_links / divider

    def calculate_links(self, link, cluster1, cluster2):
        number_links = 0

        if cluster1.id in link:
            if cluster2.id in link[cluster1.id]:
                number_links += link[cluster1.id][cluster2.id]

        return number_links

