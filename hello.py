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


#使用递归求n!
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j*fact(j-1)
    return sum
for i in range(int(input())):
    print('%d! = %d'%(i,fact(i)))


#对十个数进行排序
n = 10
#input data
print('please input ten num:n')
l = []
for i in range(n):
    l.append(int(input('input a number:n')))
print()
for i in range(n):
    print(l[i])
print()
# sort ten num
for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if l[min]>l[j]:min = j
    l[i],l[min] = l[min],l[i]
print('after sorted')
for i in range(n):
    print(l[i])

#输入矩阵，求各斜行的和  false
a = []
sum = 0.0
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(float(input('input num:n')))
for i in range(3):
    sum += a[i][i]
print(sum)




#将一个数插入以排好序的数组   ????
a = [1,2,6,9,13,16,28,40,100,0]
print('original list is:')
for i in range(len(a)):
    print(a[i])
number = int(input('inser a new number:n'))
end = a[9]
if number >end:
    a[10] = number
else:
    for i in range(10):
        if a[i]>number:
            temp1 = a[i]
            a[i] = number
            for j in range(i+1,11):
                temp2 = a[j]
                a[j] = temp1
                temp1 = temp2
            break
for i in range(11):
    print(a[i])

a = [9,6,5,4,1]
N = len(a)
print(a)
for i in range(int(N/2)):
    a[i],a[N-i-1] = a[N-i-1],a[i]
print(a)


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


