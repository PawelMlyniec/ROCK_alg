import pandas as pd
class Writer:
    def __init__(self):
        pass

    def save_results(self,threshold, clusters, time, path='results4/2sp2glob.csv'):
        with open(path, 'a') as f:
            f.write(f"{threshold},{clusters},{time}\n")

    def save_results_real(self,threshold, time, clusters, data, path='results4/mashroom2.csv'):
        with open(path, 'a') as f:
            f.write(f"thrashold,time,id,eatable,poisonous\n")
        for c in clusters:
            e = 0
            not_e = 0
            for p in c.points:
                if data[p][0] == 'e':
                    e += 1
                else:
                    not_e += 1

            with open(path, 'a') as f:
                f.write(f"{threshold},{time},{c.id},{e},{not_e}\n")
