#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:test2.py
@time:2022/10/05
"""
import tkinter as tk

root_window = tk.Tk()
# 设置窗口title
root_window.title('南通大学图书馆预约')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('450x300')
# 更改左上角窗口的的icon图标,加载C语言中文网logo标
# 这里的mac没有图标拉jb倒
root_window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root_window["background"] = "#ECECEC"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text = tk.Label(root_window, text="南通大学图书馆预约", bg="red", fg="blue", font=('黑体', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()
input = tk.Entry(root_window)
input.pack(side='left')
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button = tk.Button(root_window, text="关闭", bg="red", fg="blue", command=root_window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
# 进入主循环，显示主窗口
root_window.mainloop()
