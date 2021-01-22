from helpers.plotter import Plotter
from helpers.reader import Reader
from helpers.writer import Writer
from rock.rock import Rock
import matplotlib.pyplot as plt
from sklearn import preprocessing
import time

def test2d():
    path = 'data/2d20C.csv'
    reader = Reader()
    writer = Writer()
    data = reader.read2d(path)
    thresholds = [0.99, 0.98, 0.95, 0.9]
    for t in thresholds:
        start = time.time()
        rock = Rock(threshold=t, is_cat=False)
        clusters = rock.cluster(data, 20)
        end = time.time()
        writer.save_results(t, len(clusters), end-start, path='results4/2d20C.csv')
        plotter = Plotter()
        plot = plotter.plot2d(clusters=clusters, dataset=data, name=f'plots4/2d20C{t}')
        plot.show()

def test_real():
    path = 'data/agaricus-lepiota.csv'
    reader = Reader()
    writer = Writer()
    data = reader.read_real(path)
    data2 = data[:, 1:]
    start = time.time()
    rock = Rock(threshold=0.9, is_cat=True)
    clusters = rock.cluster(data2, 2)
    end = time.time()
    writer.save_results_real(0.9, end - start, clusters, data)


if __name__ == '__main__':
    test2d()
