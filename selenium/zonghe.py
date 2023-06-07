def ceshi():

    dan = [x for x in range(1, 11) if x % 2 != 0]
    shuzi = range(1,11)
    shuang = [x for x in range(1, 11) if x % 2 == 0]

#    for dan in shuzi:
#        if dan % 2 != 0:
 #           for i in shuzi:
 #               if dan * i < 500:
 #                  danshu = dan * i
#                   print(danshu)
 #               else:
 #                   break
 #               for shuang in shuzi:
 #                   if shuang % 2 == 0:
 #                       for ii in shuzi:
 #                           shuangshu = ii * i * shuang
 #                           if shuangshu < 1000:
 #                               print(shuangshu)
 #                           else:
 #                               break
#        else:
    for cishu in shuzi:

        for i in dan:
            if cishu * i <500:
                danshu = cishu * i
                print(danshu)
            for ii in shuang:
                if cishu * ii * i <999:
                    shuangshu = cishu * ii * i
                    #print(shuangshu)


#                for shuang in shuzi:
#                   if shuang % 2 == 0:
#                       for ii in shuzi:
#                            if shuang * i * ii < 999:
#                               shuangshu = shuang * dan * ii
#                               print(shuangshu)
#                            else:
#                                break

if __name__ == "__main__":
    ceshi()