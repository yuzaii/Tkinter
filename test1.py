#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:test1.py
@time:2022/10/05
"""
"""
'''
一个最简单的 Tkinter 程序至少应包含以下四个部分：
导入 tkinter 模块
创建主窗口，也称 root 窗口（即根窗口）
添加人机交互控件，同时编写相应的事件函数
通过主循环（mainloop）来显示主窗口
'''
"""
import tkinter as tk

# 调用Tk()创建主窗口
root_window = tk.Tk()
# 给主窗口起一个名字，也就是窗口的名字
root_window.title('我的第一个窗口城区程序')
# 开启主循环，让窗口处于显示状态
root_window.mainloop()
