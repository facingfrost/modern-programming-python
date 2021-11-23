import os
from functools import wraps

def check(func):
    @wraps(func)
    # 如果参数中有"\",则视为路径
    def wrapper(*args, **kwargs):
        dir_list = []
        for i in args:
            if "\\" in str(i):
                dir_list.append(str(i))
        for j in kwargs.items():
            if "\\" in str(j):
                dir_list.append(str(j))
        for dir in dir_list:
            if not os.path.exists(dir):
                os.makedirs(dir)
                print("创建目录:" + dir)
            else:
                print("已存在目录:" + dir)

    return wrapper


@check
def print_file(path):
    print(path)


if __name__ == "__main__":
    print_file("D:\\大三上\\10现代程序设计技术\\demo\\w8")
    print_file("D:\\大三上\\10现代程序设计技术\\demo\\w100")
    print_file("D:\\大三上\\10现代程序设计技术\\debug")