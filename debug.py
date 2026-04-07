#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/5 19:51
@File: debug.py
@Project: PythonProject1
@Desc: 
"""

from sys import argv
script, user_name = argv
prompt = '>'
print(f"你好，{user_name},我是{script}脚本")
print("我想问你几个问题。")
print(f"{user_name},你喜欢我吗？")
likes = input(prompt)

print(f"{user_name},你住在哪里？")
lives = input(prompt)

print("你用的是什么电脑？")
computer = input(prompt)

print(f"""
好的，你对我的喜爱程度是：{likes}。
你住在：{lives},虽然我不太清楚那是哪里。
你用的是：{computer}电脑，很不错！
""")