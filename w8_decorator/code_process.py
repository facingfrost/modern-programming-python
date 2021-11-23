import pickle
from line_profiler import LineProfiler
from memory_profiler import profile
import sys
from tqdm import tqdm


class Traverse:
    def __init__(self,range):
        self.range = range
        self.list = []

    @profile
    def traverse(self):
        total = self.range
        for i in range(self.range):
            self.list.append(i)
        f = open('output.txt', 'wb')
        pickle.dump(self.list, f)

if __name__ == "__main__":
    example = Traverse(100000)
    example.traverse()
