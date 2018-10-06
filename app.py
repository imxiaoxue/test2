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

import math

a = []
sum = 0.0
for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input('input num:n')))
        for i in range(3):
            sum += a[i][i]
        print(sum)





