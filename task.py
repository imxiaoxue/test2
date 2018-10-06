import math

a = input()
b = input()

print(int(a)+int(b))

a = int(input())
b = int(input())
c = int(input())
v = a*b*c
s = 2*(a*b+a*c+b*c)
print(v,s)


a = input()
h = input()
s = 1/2*int(a)*int(h)
print(s)

r = input('请输入半径：')
r = float(r)
c = 2*math.pi*r
print(('周长是：'),c)

print(ord(input()))


a = input()
b = input()
c = input()
a = float(a)
b = float(b)
c = float(c)
s = 1/2*(a+b+c)
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
L = a+b+c
print(L)

x = input()
x = abs(-1)
print("math.exp(x):",math.exp(x))

year = int(input("请输入一个年份："))
if(year%4) == 0:
    if(year%100) == 0:
        if(year%400) == 0:
            print("yes")
  # 整百年能被400整除的是闰年
        else:
            print("no")
    else:
        print("yes")
        # 非整百年能被4整除的是闰年
else:
    print("no".format(year))



score = int(input("请输入一个分数："))
if score >= 90:
    print('A')
elif 80 <= score < 90 :
    print('B')
elif 70 <= score <= 80:
    print('C')
elif 60 <= score < 70:
    print('D')
elif score < 60:
    print('E')

a = float(input())
b = float(input())
c = float(input())
def quadratic(a,b,c):
    p = b*b-4*a*c
    if p >= 0 and a!= 0:
        x1 = (-b+math.sqrt(p))/(2*a)
        x2 = (-b-math.sqrt(p))/(2*a)
        return x1,x2
    elif a == 0:
        x1=x2=-c/b
        return x1,x2
    else:
        return('No solution.')
print(quadratic(a,b,c))


print("请输入三个数：")
a = int(input())
b = int(input())
c = int(input())
if a>b:
    maxnum = a
else:
    maxnum = b
    if c>maxnum:
            maxnum = c
print(maxnum)

print("x = ")
x = int(input())
if x < 1:
    y = x
if 1 <= x <= 10:
    y = 2*x-1
else:
    y = 3*x-11
print(y)

print('请输入一个数字：')
n = input()
print(n[::-1])

print('请输入用电量：')
power = float(input())
if power <= 50:
    print(0.5*power)
if 50 < power <=100:
    print(0.5*50+0.7*(power-50))
else:
    print(0.5*50+0.7*100+1*(power-100))


r = int(input())
H = int(input())
x = int(input())
y = int(input())
if (pow(x,2)+pow(y,2)<pow(r,2)):
    print('此点在圆锥上')
s = math.sqrt(pow(x,2)+pow(y,2))
h = H*(r-s)/r
print(h)


print('x = ')
x = float(input())
if 1 <= x <= 10:
    y = x+2
else:
    y = x-1
print(y)

num = int(input("请输入月份："))
if num in (1,3,5,7,8,10,12):
    print('day = 31')
elif num ==2:
    year = int(input('年份：'))
if(year%4==0 and year%100!=0 or year%400==0):
    print("day = 29")
else:
    print("day = 28")
if num in (4,6,9,11):
    print('day = 30')

a = int(input())
b = int(input())
if (a >=90 and b >= 90):
    print('great')
if (a >=60 or b >= 60):
    print('so-so')
else:
    print('bad')




n = int(input())

def isPrime(n):
    if n <=1:
        print('NO')
    elif n ==2:
        print('YES')
        return
    elif n ==3:
        print('YES')
        return

    else:
        for i in range(2,int(math.sqrt(n))+1):
            print(i)
            return
    print('YES')

isPrime(n)


n = int(input())
k = 1
s = 0
while s < n:
    s += 1 / k
    k += 1
else:
    print(k-1)


n = int(input())
while n:
    n = int(input())
    if n == -1:
        break

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end = "")
    print()


Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a*10
    Sn.append(Tn)
    print(Tn)
from functools import reduce
Sn = reduce(lambda x,y:x+y,Sn)
print(Sn)


n = 0
s = 0
t = 1
for n in range(1,int(input())+1):
    t *= n
    s += t
    print(s)


for i in range(0,3):
    print(" "*(3-i) + '*'*(2*i+1))
for i in range(1,-1,-1):
    print(" "*(3-i) + '*'*(2*i+1))


a = 2
b = 1
s = 0

for n in range(1,int(input())+1):
    s += a/b
    t = a
    a = a+b
    b = t
print(s)

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


for n in range(100,1000):
    a = int(n/100)
    b = int(n/10%10)
    c = n%10
    if n == a**3+b**3+c**3:
        print(n)














