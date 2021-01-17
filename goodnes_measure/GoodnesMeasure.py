class GoodnessMeasure():
    def __int__(self):
        self._threshold = 0.5
        self._scaling_factor = 1.0 + 2.0 * ((1.0 - self._threshold) / (1.0 + self._threshold))

    def g(self, link, cluster1, cluster2):
        number_links = self.calculate_links(link, cluster1, cluster2)
        n = len(cluster1)
        m = len(cluster2)
        devider = (n + m) ** self._scaling_factor - n ** self._scaling_factor - m ** self._scaling_factor

        return number_links / devider

    def calculate_links(self, link_mat, cluster1, cluster2):
        number_links = 0

        for index1 in cluster1:
            for index2 in cluster2:
                number_links += link_mat[index1][index2]

        return number_links
