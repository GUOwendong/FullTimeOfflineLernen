#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/6 19:59
@File: Number_type.py
@Project: PythonProject1
@Desc: 
"""
#对除法进行了练习
a = 6
b = 2
c = a / b
print(c)
#对小数进行了感知
x = 0.1
y = 0.2
z = x + y
print(z)
e = 3
f = 7
d = e + f
print(d)
g = 10
if g == d:
    print(f"生活的确很难，谁说还不是！")
else:
    print(f"再怎么说我们还是加油向前走！")
#对while循环进行了联系
h = 0
while h < 1:
    h = h + 0.1
    print(h)

i = 0.3
j = 0.1 + 0.2
#compare
if i == j:
    print("True")
else:
    print("False")
#学习10进制 decimal
import decimal
k = decimal.Decimal('0.01')
l = decimal.Decimal('0.04')
m = k + l
print(m)
n = decimal.Decimal('0.05')
print(n)
if m == n:
    print("True")
else:
    print("False")

o = 0.00005
print(o)

p = 1 + 2j
print(p)
print(p.real)
print(p.imag)

#加减乘除，地板除
q = 3 / 2
print(q)
r = 3 // 2
print(r)
s = -3 // 2
print(s)

#divmod测试，尝试
t = divmod(7, 3)
print(t)
