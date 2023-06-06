import csv
#循环次数的条件赋值

def ceshi():
    cishu = 0

    #写入内容
    with open('product.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        #循环写入数据

        while cishu < 10 :
            writer.writerow(['aaa'])
            cishu += 1


        print(writer)

if __name__ == "__main__":
    ceshi()