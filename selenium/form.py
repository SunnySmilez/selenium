#循环次数
def ceshi():
    shuzhi = range(1,51)
    for shu in shuzhi:
        if shu % 2 != 0:
            print(shu)
        if shu > 50:
            break



if __name__ == "__main__":
    ceshi()