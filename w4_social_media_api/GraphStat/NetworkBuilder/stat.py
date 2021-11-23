import pandas as pd
import numpy as np
from NetworkBuilder.node import get_degree


def cal_every_degree(edges):
    sr = list(edges.iloc[:,0])
    node = set(sr)
    degree_dict={}
    for i in node:
        print(i)
        degree_dict[i]=sr.count(i)
    return degree_dict

def cal_average_degree(degree_dict):
    return np.mean(list(degree_dict.values()))

def cal_degree_distribution(degree_dict):
    degree_distribution={}
    for i in degree_dict:
        degree_distribution[degree_dict[i]]=degree_distribution.get(degree_dict[i],0)+1
    return sorted(degree_distribution.items(), key=lambda e:e[0])

if __name__ == "__main__":
    vertices = pd.read_table('../vertices.txt', low_memory=False, header=None)
    edges = pd.read_table('../edges.txt', low_memory=False, header=None)
    degree_dict=cal_every_degree(edges)
    print(cal_average_degree(degree_dict))
    print(cal_degree_distribution(degree_dict))