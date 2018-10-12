car = 'subaru'
print("Is car == 'subaru'?I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I Predict False.")
print(car == 'audi')

phone = 'iphone'
print("Is phone == 'iphone'?I Predict True")
print(phone == 'iphone')

print("Is phone == 'Iphone'? I Predict False")
print(phone == 'Iphone')
print(phone.lower())

phone = 'Iphone'
if phone != 'iphone':
    print("It is not iphone.")

room = 2122
print(room == 2122)
print(room !=2122)
print(room >2122)
print(room <2122)
print(room>=2122)
print(room<=2122)


def recur_fibo(n):
    '''递归函数
    输出斐波那契数列'''
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

#获取用户输入
nterms = int(input('您要输入几项？'))

#检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波那契数列：")
    for i in range(nterms):
        print(recur_fibo(i))

from numpy import *
a = mat(random.randint(1,7,size = (3,5)))
print(a)


m1 = [[1,2,3,0],[4,5,6,0],[7,8,9,0]]
m2 = [[2,4,6,0],[1,3,5,0],[0,-1,-2,0]]
m3 = [4*[0]for i in range(3)]
for i in range(3):
    for j in range(4):
        m3[i][j] = m1[i][j]+m2[i][j]
print(m3)



from numpy import *
a1 = array([1,2,3])
a2 = mat(a1)
print(a2)

import numpy as np
a = np.array([[1,2,3],[4,5,6]],dtype = int)
print(a)

a2 = np.ones((2,3,4),dtype = np.int16)
print(a2)

a3 = np.empty((2,3))
print(a3)


import numpy as np
def f(x,y):
    return (x,y)
def g(x,y):
    return x+y
(x,y) = np.fromfunction(f,(3,5))
a4 = np.fromfunction(g,(3,5))
print(a4)


#yanghuisanjiao
n = int(input())
q = []
for _ in range(n):
    for _ in range(len(q) - 1):
        q.append(q.pop(0) + q[0])
    q.append(1)
    print(q)

#将一个数组逆序输出
if __name__=='_main_':
    n = int(input())
    a = (input([]))
    N = len(a)
    print(a)
    for i in range(int(N/2)):
        a[i],a[N-i-1] = a[N-i-1],a[i]
    print(a)


#使用递归求n!
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j*fact(j-1)
        return sum
    for i in range(int(input())):
        print(i,fact(i))

#将一个数组逆序输出
a = [2,4,5,7,8,9,13,180]
N = len(a)
print(a)
for i in range(int(N/2)):
    a[i],a[N-i-1] = a[N-i-1],a[i]
print(a)



str_in = input()
print(str_in)

a = [1,2,6,9,13,16,28,40,100,0]
print('original list is:')
for i in range(len(a)):
    print(a[i])
number = int(input('inser a new number:n'))
if number > a[len(a)-1]:
    a.append(number)
else:
    for i in range(len(a)):
        if a[i]>number:
            a.insert(i,number)
print(a)









end = a[9]
if number >end:
    a[10] = number
else:
    for i in range(10):
        if a[i]> number:
            temp1 = a[i]
            a[i] = number
            for j in range(i+1,11):
                temp2 = a[j]
                a[j] = temp1
                temp1 = temp2
            break
for i in range(11):
    print(a[i])