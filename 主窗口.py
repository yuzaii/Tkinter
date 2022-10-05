#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:主窗口.py
@time:2022/10/05
"""
# 导入tk
from tkinter import *

# 创建一个主窗口对象
window = Tk()
# 调用mainloop()显示主窗口
window.title('主窗口')

# 窗口长
w = 450
# 窗口宽
h = 300
# 窗口大小 px*px加上+num1+num2 num1为左+右- num2为上+下-
# window.geometry(f'{w}x{h}+100-100')
# 如果我需要使得窗口居中 就需要获取屏幕的宽度
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
print(screenWidth, screenHeight)
# 获取左边和上边的坐标
x=int(screenWidth/2-w/2)
y=int(screenHeight/2-h/2)
print(x,y)
window.geometry(f'{w}x{h}+{x}+{y}')
window.mainloop()
