from matplotlib import pyplot as plt
import pandas as pd

def count_job(edges):
    job_list=list(edges.iloc[:,3])
    job_title = ['director','starring','writer','English']
    num = [0,0,0,0]
    for i in job_list:
        if i == 'director':
            num[0]+=1
        elif i == 'starring':
            num[1]+=1
        elif i == 'writer':
            num[2]+=1
        else:
            num[3]+=1
    plt.bar(range(len(num)), num, tick_label=job_title)
    plt.show()




if __name__ == "__main__":
    vertices = pd.read_table('../vertices.txt', low_memory=False, header=None)
    edges = pd.read_table('../edges.txt', low_memory=False, header=None)
    count_job(vertices)