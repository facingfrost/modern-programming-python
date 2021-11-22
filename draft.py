from pyecharts import options as opts
from pyecharts.charts import Sankey


if __name__ == "__main__":
    G = (x*x for x in range(10))
    for i in range(10):
        print(next(G))