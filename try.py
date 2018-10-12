def leap_year(y):
    y = int(input("请输入一个年份："))
    if(y%4) == 0:
        if(y%100) == 0:
            if(y%400) == 0:
                print("yes")
      # 整百年能被400整除的是闰年
            else:
                print("no")
        else:
            print("yes")
            # 非整百年能被4整除的是闰年
    else:
        print("no".format(y))
