#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/6 13:26
@File: with_benutzen.py
@Project: PythonProject1
@Desc: 
"""
from sys import argv
from os.path import exists
from_file = "test.txt"
to_file = "new_test.txt"

print(f"正在从{from_file}复制到{to_file}")
# we could do these two on one line too, how?

with open(from_file, "r", encoding="utf-8") as in_file:
    indata = in_file.read()

    print(f"输入文件的大小为{len(indata)}字节")
    print(f"目标文件存在吗？{exists(to_file)}")
    print("准备好后，按Enter键继续，按Ctrl-C取消。")
    input()

with open(to_file, "w", encoding="utf-8") as out_file:
    out_file.write(indata)

    print("好了，全部完成。")