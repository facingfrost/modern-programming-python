def copy_part(copied_path, copying_path, start, end):
    '''
    :param copied: 被复制的文件
    :param copying: 复制到的文件
    :param start: 开始的某一行
    :param end: 结束的某一行
    '''
    i = 0
    while True:
        line = f1.readline()
        i += 1
        if i > start and i <= end:
            f2.write(line)
        if i > end:
            break


if __name__ == "__main__":
    f1 = open(r'../newmovies.txt', 'rb')
    f2 = open(r'../edges.txt', 'ab')
    copy_part(f1, f2, 34285, 176712)
