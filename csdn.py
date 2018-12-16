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

# 读入一个字符,输出其ASCII码
a = input()
print(ord(a))



#已知三角形三边求面积和周长
a = input()
b = input()
c = input()
a = float(a)
b = float(b)
c = float(c)
#海伦公式
s = 1/2*(a+b+c)
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
L = a+b+c
print(L)


x = int(input('请输入'))
x = abs(x)
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

n = int(input('n = '))
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
for n in range(1,int(input('n = '))+1):
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

for n in range(1,int(input('n = '))+1):
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


#斐波拉契数列前n项
nterms = int(input('需要输出几项？'))
n1 = 0
n2 = 1
count = 2
if nterms <=0:
    print('请输入一个正整数')
elif nterms == 1:
    print('斐波那契数列：')
    print(n1)
else:
    print('斐波那契数列：')
    print(n1,',',n2,end = ',')
    while count <nterms:
        nth =n1 +n2
        print(nth,end = ',')
        #更新值
        n1 = n2
        n2 = nth
        count +=1


#输入一个矩阵，求出各列的和
import numpy as np
a = np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7]],dtype = int)
print(a)
b = a.sum(axis = 0)
print(b)

#三级斐波拉契数列前n项
nterms = int(input('需要输出几项？'))
n1 = 0
n2 = 1
n3 = 1
count = 3
if nterms <=0:
    print('请输入一个正整数')
elif nterms == 1:
    print('斐波那契数列：')
    print(n1)
else:
    print('斐波那契数列：')
    print(n1,',',n2,',',n3,end = ',')
    while count <nterms:
        nth =n1 +n2 + n3
        print(nth,end = ',')
        #更新值
        n1 = n2
        n2 = n3
        n3 = nth
        count +=1


#陶陶摘苹果
L = input().split()
h = int(input())
n = int(len(L))
for i in range(n):
    if int(L[i]) > (h+30):
        n -= 1
    print(n)



#输入n个数，输出其中最大和最小
test = input('请输入一个数组：')
temp = []
for i in test.split(','):
    temp.append(int(i))
temp = sorted(temp)
print('从小到大:', temp)
print(temp[-1])
print(temp[0])



#将一个数插入排好序的序列

a1 = [2,5,7,8,9,13,180]
a2 = [4]
a3 = a1+a2
j = 0
while j<len(a3)-1:
    i = 0
    while i<len(a3)-(j+1):
        if a3[i] >a3[i+1]:
            a = a3[i]
            a3[i] = a3[i+1]
            a3[i+1] = a
        i +=1
    j +=1
print(a3)



#将两个数列合并，并保持从小到大的顺序
a1 = [2,5,7,8,9,13,180]
a2 = [3,4,10,11,12]
a3 = a1+a2
j = 0
while j<len(a3)-1:
    i = 0
    while i<len(a3)-(j+1):
        if a3[i] >a3[i+1]:
            a = a3[i]
            a3[i] = a3[i+1]
            a3[i+1] = a
        i +=1
    j +=1
print(a3)


#将一个数组逆序输出
a = [2,4,5,7,8,9,13,180]
N = len(a)
print(a)
for i in range(int(N/2)):
    a[i], a[N - i - 1] = a[N - i - 1], a[i]
print(a)







#杨辉三角
n = int(input())
q = []
for _ in range(n):
    for _ in range(len(q) - 1):
        q.append(q.pop(0) + q[0])
    q.append(1)
    print(q)




#求素数
n = int(input())
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

#求数阶乘之和
def recursion(n):
    if n == 1:
        return 1
    else:
        return n*recursion(n-1)
list = []
print('将1-n的阶乘写入列表，使用sum函数')
n = int(input('请输入n：'))
for i in range(1,n+1):
    list.append(recursion(i))
print(sum(list))







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



#将字符串转换为数字
str = input()
num = int(str)
print(num)

#判断一个年份是否为闰年
def year(y):
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
y = int(input("请输入一个年份："))
print(year(y) )


#输入一个日期，计算出自从2000.1.1到这一天过了多久
def which_day(year,month,day):
    list = [31,28,31,30,31,30,31,31,30,31,30,31]
    which_day = 0
    if((year%4) == 0 and (year%100) == 0 and (year%400) == 0):
        list[1] = 29
    for i in range(1,month):
        if month == 1:
            print(day)
        which_day = which_day + list[i-1]
    which_day = which_day +day
    print(which_day)
if __name__ == "__main__":
    year = int(input('请输入年份'))
    month = int(input('请输入月份'))
    day = int(input('请输入天'))
    which_day(year, month, day)






#辗转相除法求最大公约数
num1 = int(input('请输入一个数字：'))
num2 = int(input('请输入一个数字：'))
m = max(num1,num2)
n = min(num1,num2)
r = m%n
while r != 0:
    m = n
    n = r
    r = m%n
print(num1,'和',num2,'的最大公约数为',n)

#求2^n的值
r = 2
n =int(input())
num = 1
for i in range(1,n+1):
    num = num*r
print(num)


#输出1到n的所有素数
num = []
i = 2
n = int(input())
for i in range(2,n):
    j = 2
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        num.append(i)
print(num)

#全排列
def perm(n,begin,end):
    global count
    if begin >=end:
        print(n)

    else:
        i = begin
        for num in range(begin,end):
            n[num],n[i] = n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i] = n[i],n[num]
n = [1,2,3]
perm(n,0,len(n))



#查找数组中的一个数
def BinarySearch(array,t):
    min = 0
    max = len(array)-1

    while min<max:
        mid = (min + max) // 2
        if array[mid] > t:
            max = mid - 1
        elif array[mid] < t:
            min = mid + 1
        else:
            return array[mid]
    return -1
if __name__ =='__main__':
    print(BinarySearch([2,4,5,7,8,9,13,180],4))

#选择排序
def selectsort(list,order = 1):
    if not isinstance(order,int):
        raise TypeError ('order类型错误')
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if order == 1:
                if list[j] <list[min_index]:
                    min_index = j
            else:
                if list[j] >list[min_index]:
                    min_index = j
            if min_index != i:
                list[i],list[min_index] = list[min_index],list[i]
    print(list)
selectsort([5,180,8,7,9,4,13,2],1)

#冒泡排序
arr = [5,180,8,7,9,4,13,2]
def bubble_sort(arr):
    n = len(arr)
    for j in range(0,n-1):
        for i in range(0,n-1-j):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
bubble_sort(arr)
print(arr)


#插入排序
l = [5,180,8,7,9,4,13,2]
def direct_insert_sort(numbers):
    for i in range(1,len(numbers)):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp<numbers[j]:
            numbers[j+1] = numbers[j]
            j = j -1
        numbers[j+1] = temp
if __name__ == '__main__':
    direct_insert_sort(l)
    print(l)

#桶排序
import random
def bucketSort(list):
    buckets = [0]*((max(list)-min(list))+1)
    for i in range(len(list)):
        buckets[list[i]-min(list)]+=1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(list)]*buckets[i]
    return res
nums = [random.randint(1,100) for i in range(20)]
print(nums)
print(bucketSort(nums))


#快速排序
def parttion(v,left,right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while(low<high) and (v[high]>=key):
            high -=1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low +=1
        v[high] =v[low]
        v[low] = key
    return low
def quicksort(v,left,right):
    if left < right:
        p = parttion(v,left,right)
        quicksort(v,left,p-1)
        quicksort(v,p+1,right)
    return v
s = [5,180,8,7,9,4,13,2]
print('before sort:',s)
s1 = quicksort(s,left = 0,right = len(s)-1)
print('after sort:',s1)

#归并排序
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)
def merge(left,right):
    c = []
    h = j = 0
    while j < len(left) and h < len(right):
        if left[j] < right[h]:
            c.append(left[j])
            j+=1
        else:
            c.append(right[h])
            h+=1
    c += left[j:]
    c += right[h:]
    return c
lists = [5, 180, 8, 7, 9, 4, 13, 2]
sorted_lists = merge_sort(lists)
print(sorted_lists)








