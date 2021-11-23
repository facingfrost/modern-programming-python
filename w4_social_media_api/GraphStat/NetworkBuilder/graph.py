import pandas as pd
from NetworkBuilder.node import get_degree
from NetworkBuilder.node import init_node
import pickle

def init_graph(vertices,edges):
    graph_dict = {}
    nodes = set(list(vertices.iloc[:,0]))
    for i in nodes:
        print(i)
        node_dict = init_node(vertices,i)
        degree = get_degree(edges,i)
        graph_dict[i] = {"node":node_dict,"degree":degree}
    return graph_dict

def save_graph(graph_dict):
    return pickle.dumps(graph_dict)

def save_graph(series):
    return pickle.loads(series)

if __name__ == "__main__":
    vertices = pd.read_table('../vertices.txt', low_memory=False, header=None)
    edges = pd.read_table('../edges.txt', low_memory=False, header=None)
    graph_dict = init_graph(vertices,edges)
    print(graph_dict)
