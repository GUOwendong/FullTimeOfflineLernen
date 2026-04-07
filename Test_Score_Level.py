#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/7 17:11
@File: Test_Score_Level.py
@Project: PythonProject1
@Desc: 
"""

while True:
    s = input("请输入您的分数：").strip()
    try:
        score = float(s)
        if score < 0 or score > 100:
            print("输入错误，请输入0～100之间的分数。")
        else:
            if score >= 90:
                print("A等级")
            elif score >= 60:
                print("B等级")
            else:
                print("C等级")
            break
    except ValueError:
                print("输入错误，请输入一个0到100之间的分数。")