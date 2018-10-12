

#求矩阵各斜行的和???
matrix = [[1,2,3,4,5],
          [2,3,4,5,6],
          [3,4,5,6,7]]
for i in range(4):
    for j in range(i,4):
        sum = matrix[i][j]




#exp()函数


import math
#求素数??????
n = int(input('n = '))
def isPrime(n):
    if n <=1:
        print("No,it isn't.")
    elif n ==2:
        print("Yes,it is.")
        return
    elif n ==3:
        print("Yes,it is.")
        return

    else:
        for i in range(2,int(math.sqrt(n))+1):
            print(i)
            return
    print("Yes,it is.")

isPrime(n)






#勒让德多项式?????
def Pnx():
    if n == 0:
        Pnx = 1
        print(Pnx)
    if n ==1:
        Pnx = x
        print(Pnx)
    else:
        Pnx = ((2*n-1)*x-Pnx((n-1),x)-(n-1)*Pnx((n-2),x))/n


#变量轮换????
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a
print(fib(int(input())))

#输出数列第n项







#输出一列全排列数，输出下一列








#输入一串括号，判断是否匹配?????
symbols = {'}':'{',']':'[',')':'(','>':'<'}
symbols_l,symbols_r = symbols.values(),symbols.keys()
def check(s):
    arr = []
    for c in s:
        if c in symbols_l:#左符号入栈
            arr.append(c)
        elif c in symbols_r:#右符号要么出栈，要么匹配失败
            if arr and arr[-1] == symbols[c]:
                arr.pop()
            else:
                return False
        return True
print(check('3*{3+[(2-3)*(4+5)]}'))
print(check('3*{3+[4-6}]'))



#0-1背包
#数塔

