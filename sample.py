#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/5 20:41
@File: sample.py
@Project: PythonProject1
@Desc: debug调试用
"""
from sys import argv
script, filename = argv
txt = open(filename)
print(f"这是你的文件{filename}:")
print(txt.read())

print("请再次输入文件名：")
file_again = input(">")

txt_again = open(file_again)
print(txt_again.read())
