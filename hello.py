for i in range(1,8,2):
    print(int((7-i)/2)*"",end = "")
    for j in range(i):
        print("*",end = "")
    print()
for i in range(5,0,-2):
    print(int((7-i)/2)*"",end = "")
    for j in range(i):
        print("*",end = "")
    print()


for i in range(1,8,2):
    for j in range(i):
        print("*",end = "")
    print()
for i in range(5,0,-2):
    for j in range(i):
        print("*",end = "")
    print()

def f(x):
    s = (2*x)**3+(-4*x)**2+(3*x)-6
    return s
mid = 0
for i in range(-10,10,1):
    x1 = int(i)
    x2 = int(i+1)
    if f(x1)*f(x2)<0:
        m,n =x1,x2
        while n-m>0.01:
            mid = (m+n)/2
            if f(m)*f(mid)<0:
                n = mid
            else:
                m =mid
    else:
        pass
print(round(mid,2))




n = int(input())
k = 1
s = 0
while s < n:
    s += 1 / k
    k += 1
else:
    print(k-1)
import math
r = input('请输入半径：')
r = float(r)
v = 4/3*math.pi*pow(r,3)
print(('体积是：'),v)



print(ord(input()))


print('请输入用电量：')
power = float(input())
if power <= 50:
    print(0.5*power)
if 50 < power <=100:
    print(0.5*50+0.7*(power-50))
else:
    print(0.5*50+0.7*100+1*(power-100))

num = int(input("请输入月份："))
if num in (1, 3, 5, 7, 8, 10, 12):
    print('day = 31')
elif num == 2:
    year = int(input('年份：'))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("day = 29")
else:
    print("day = 28")
if num in (4, 6, 9, 11):
    print('day = 30')






