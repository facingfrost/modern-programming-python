import pandas as pd


def init_node(vertices,id):
    '''
    :param id: 输入需要的ID号
    :return: 输出该节点属性字典
    '''
    sr = vertices.iloc[id]
    node_dict = {}
    node_dict['ID'] = sr[0]
    node_dict['Name'] = sr[1]
    node_dict['Weight'] = sr[2]
    node_dict['Type'] = sr[3]
    node_dict['Info'] = sr[4]
    return node_dict


def print_node(id):
    node_dict = init_node(id)
    print('ID: {0[ID]}\nName: {0[Name]}\nWeight: {0[Weight]}\nType:{0[Type]}\nInfo:{0[Info]}'.format(node_dict))

def get_degree(edges,id):
    sr = list(edges.iloc[:, 0])
    return sr.count(id)



if __name__ == "__main__":
    vertices = pd.read_table('../vertices.txt', low_memory=False, header=None)
    edges = pd.read_table('../edges.txt', low_memory=False, header=None)

