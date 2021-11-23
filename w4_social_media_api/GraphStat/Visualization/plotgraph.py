from NetworkBuilder.stat import cal_every_degree
from NetworkBuilder.stat import cal_degree_distribution
from matplotlib import pyplot as plt
import pandas as pd

def plot_distribution(degree_distribution):
    x=[]
    y=[]
    for i in degree_distribution:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y)
    plt.show()
    return 0

if __name__ == "__main__":
    vertices = pd.read_table('../vertices.txt', low_memory=False, header=None)
    edges = pd.read_table('../edges.txt', low_memory=False, header=None)
    degree_dict=cal_every_degree(edges)
    degree_distribution=cal_degree_distribution(degree_dict)
    plot_distribution(degree_distribution)