import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

class Plotter:
    def __init__(self):
        pass

    def plot2d(self, clusters, dataset, name):
        data = []
        colors = np.random.choice([colrgb for col, colrgb in matplotlib.colors.cnames.items()], len(clusters))
        map = {}
        for i, c in enumerate(clusters):
            map[c.id] = colors[i]

        for cluster in clusters:
            label = cluster.id
            for d in cluster.points:
                data.append([dataset[d][0],dataset[d][1], map[label]])


        data = pd.DataFrame(data=data, columns=['x', 'y', 'label'])
        plt.show()
        plot = data.plot.scatter(x='x', y='y', c='label').get_figure()
        plot.savefig(f'{name}.png')
        plot
        return plot

    def plot2d2(self, clusters, dataset):
        data = []
        colours = ['b', 'r', 'y', 'g', 'c', 'm', 'k', 'peru', 'salmon']
        map = {}

        print(len(clusters))

        for i, c in enumerate(clusters):
            map[c.id] = colours[i]

        for cluster in clusters:
            label = cluster.id
            for d in cluster.points:
                data.append([dataset[d][0], dataset[d][1], map[label]])

        data = pd.DataFrame(data=data, columns=['x', 'y', 'label'])
        for label in set(data['label']):
            cond = data['label'] == label
            plt.plot(data[cond, 'x'], data[cond, 'y'], linestyle='none', marker='o', label=label)
        plt.show()
        plot = data.plot.scatter(x='x', y='y', c='label').get_figure()
        plot.savefig('test.png')
        plot
        return plot

