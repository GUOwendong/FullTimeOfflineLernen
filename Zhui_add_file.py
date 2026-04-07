#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/5 21:57
@File: Zhui_add_file.py
@Project: PythonProject1
@Desc: 
"""
try:
    with open("Daller.txt","r",encoding="utf-8") as f:
        old_content = f.read()
except:
    old_content = ""

new_line = "我要找到你，一开始一路走，一辈子\n"
all_content = old_content + new_line
with open("Daller.txt","a",encoding="utf-8") as f:
    f.write(all_content)