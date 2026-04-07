#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: guowendong
@Date: 2026/4/6 15:46
@File: path_debug.py
@Project: PythonProject1
@Desc: 
"""

print(r"\Desktop\one\two\three\now")

"""用python设计第一个游戏"""
names = 3
while names > 0:
    temp = input("不妨猜一下郭文东心里现在想的那个数字：")
    guess = int(temp)
    if guess == 8:
        print("你娃是我肚里蛔虫吗？这么屌！")
        print("既然这么厉害，那我就送你一更棒棒糖吧，嘿嘿嘿...")
        break
    else:
        if guess < 8:
            print("小了小了")
        else:
            print("大了大了")
    names = names - 1
print("游戏结束，不玩了！")