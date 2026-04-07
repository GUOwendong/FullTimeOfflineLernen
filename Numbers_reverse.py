#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/7 15:41
@File: Numbers_reverse.py
@Project: PythonProject1
@Desc: 
"""

number = int(input("请输入一3位正整数："))
if 100 <= number <= 999:
    a = number % 10
    b = (number // 10) % 10
    c = number // 100
    print("反转后的数字是：", a * 100 + b * 10 + c)
else:
    print("输入错误，请输入一个3位正整数。")