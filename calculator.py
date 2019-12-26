# coding=utf-8
import os
import tkinter as tk
from math import *
root = tk.Tk()  # 给出一个窗口
root.geometry('+500+200')
root.resizable(width=False,height=False)
root.title('calculator')  # 设置窗口名字
window = tk.Frame(root, bg='pink')  # 新建一个框架
window.pack(expand=tk.YES, fill='x')  # tk.YES 组件显示在附配件中心位置 痛苦，fill='x'填充x方向

# 定义变量
display = tk.StringVar()

# 创建输入框
e = tk.Entry(window,bd=10,width=30, textvariable=display)
e.grid(row=0, column=0, sticky=tk.N, columnspan=50, rowspan=2)  # columnspan  rowspan 从组件所置单元格算起在列表上的跨度

tk.Button(window, text='1', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '1')).grid(row=3,column=0)  # INSERT 表示在光标处插入内容
tk.Button(window, text='2', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '2')).grid(row=3,column=1)  # lambda:后面直接跟需要执行的东西
tk.Button(window, text='3', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '3')).grid(row=3,column=2)  # lambda python内置的 简化简单函数的写法
tk.Button(window, text='4', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '4')).grid(row=4, column=0)
tk.Button(window, text='5', width=6, height=3,bg='yellow', command=lambda: e.insert(tk.INSERT, '5')).grid(row=4, column=1)
tk.Button(window, text='6', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '6')).grid(row=4, column=2)
tk.Button(window, text='7', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '7')).grid(row=5, column=0)
tk.Button(window, text='8', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '8')).grid(row=5, column=1)
tk.Button(window, text='9', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '9')).grid(row=5, column=2)
tk.Button(window, text='0', width=6,height=3, bg='yellow', command=lambda: e.insert(tk.INSERT, '0')).grid(row=4, column=3)
tk.Button(window, text='.', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, '.')).grid(row=5, column=3)
tk.Button(window, text='+', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, '+')).grid(row=2, column=0)
tk.Button(window, text='-', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, '-')).grid(row=2, column=1)
tk.Button(window, text='*', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, '*')).grid(row=2, column=2)
tk.Button(window, text='/', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, '/')).grid(row=2, column=3)
tk.Button(window, text='sqrt', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, 'sqrt(')).grid(row=2,
                                                                                                      column=4)  # 开根
tk.Button(window, text='(', width=6,height=3, bg='blue', command=lambda: e.insert(tk.INSERT, '(')).grid(row=3, column=4)
tk.Button(window, text=')', width=6,height=3,bg='blue', command=lambda: e.insert(tk.INSERT, ')')).grid(row=4, column=4)
tk.Button(window, text='=', width=6,height=3, bg='blue', command=lambda: cal(display)).grid(row=5, column=4)
tk.Button(window, text='del', width=6,height=3, bg='blue', command=lambda: e.delete('0', 'end')).grid(row=3, column=3)
# 将字符串转化为表达式
def cal(display):
    display.set(eval(display.get()))  # display.get() 得到Entr内容
window.mainloop()
if __name__ == '__main__':
    os.system("calculator.py")