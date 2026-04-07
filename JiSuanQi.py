#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/7 16:23
@File: JiSuanQi.py
@Project: PythonProject1
@Desc: 
"""
first = int(input("输入第一个数字："))
second = int(input("输入第二个数字："))
operator = input("输入运算符：")
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
else:
    print("无效的运算符，请输入 +、-、* 或 /。")
