#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/6 00:17
@File: other_sprechen.py
@Project: PythonProject1
@Desc: 
"""
from sys import argv
script, filename = argv

print(f"我们即将清空文件{filename}。")
print("如果你不想清空文件，按CTRL-C (^C)退出。")
print("如果你想清空文件，请按回车键（RETURN）。")

input("你的选择：")
print("正在打开文件...")
with open(filename, "w", encoding='utf-8') as target:
    print("正在清空文件内容，再见了！")
    print("现在，请输入三行内容。")
    line1 = input("第一行：")
    line2 = input("第二行：")
    line3 = input("第三行：")
    print("正在写入文件...")
    target.write(line1)
    target.write('\n')
    target.write(line2)
    target.write('\n')
    target.write(line3)
    target.write('\n')
    print("操作完成，正在关闭文件...")