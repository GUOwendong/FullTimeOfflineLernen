#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/6 12:28
@File: Boole_value.py
@Project: PythonProject1
@Desc: 
"""
from sys import argv
from os.path import exists
from_file = "test.txt"
to_file = "new_test.txt"

print(f"正在从{from_file}复制到{to_file}")
# we could do these two on one line too, how?

in_file = open(from_file, encoding="utf-8")
indata = in_file.read()

print(f"输入文件的大小为{len(indata)}字节")
print(f"目标文件存在吗？{exists(to_file)}")
print("准备好后，按Enter键继续，按Ctrl-C取消。")
input()

out_file = open(to_file, "w", encoding="utf-8")
out_file.write(indata)

print("好了，全部完成。")

out_file.close()
in_file.close()

