# coding=utf-8
import tkinter as tk
import os
# 创建主窗口对象
root = tk.Tk()
root.resizable(width=False,height=False)
# 设置主窗口大小（最小值）
root.geometry('200x500')
root['cursor']='spider'
root.title('哆啦A梦小口袋')
# 在内存中创建一个按钮
# def changebg(eventobj):#设置点击事件背景
#     eventobj.widget['bg'] = 'red'
def onClickbtn1():
    os.system("python calculator.py")
    # import calculater
def onClickbtn2():
    os.system("python baidu.py")
def onClickbtn4():
    os.system("python yasuo.py")
def onClickbtn5():
   os.system("python zidian.py")
def onClickbtn3():
    os.system("python weather.py")
def onClickbtn6():
    os.system("python music.py")
def onClickbtn8():
    os.system("python game.py")
def onClickbtn9():
    os.system("python love.py")
def onClickbtn7():
    # os.system("python train1.py")
    pass
imgbtn1 = tk.PhotoImage(file = '1.gif',width=101,height=101)
btn1 = tk.Button(root,text="计算器",cursor='heart',image=imgbtn1,command = onClickbtn1)
btn1.grid(row=0,column=0,rowspan=2)
# btn1.bind('<FocusIn>',changebg)
imgbtn2 = tk.PhotoImage(file='2.gif',width=101,height=101)
btn2 = tk.Button(root,text="百度文库",image=imgbtn2,cursor='heart',command = onClickbtn2)
btn2.grid(row=0,column=1,rowspan=2)
imgbtn3 = tk.PhotoImage(file = '3.gif',width=101,height=101)
btn3 = tk.Button(root,text="天气查询",cursor='heart',image = imgbtn3,command = onClickbtn3)
btn3.grid(row=2,column=0,rowspan=2)
imgbtn4 = tk.PhotoImage(file='4.gif',width=101,height=101)
btn4 = tk.Button(root,text="压缩",cursor='heart',image=imgbtn4,command = onClickbtn4)
btn4.grid(row=2,column=1,rowspan=2)
imgbtn5 = tk.PhotoImage(file='5.gif',width=101,height=101)
btn5 = tk.Button(root,text="字典",cursor='heart',image = imgbtn5,command = onClickbtn5)
btn5.grid(row=4,column=0,rowspan=2)
# music = tkinter.PhotoImage(file = 'music.gif')
imgbtn6 = tk.PhotoImage(file='6.gif',width=101,height=101)
btn6 = tk.Button(root,text='音乐盒',cursor='heart',image =imgbtn6,command = onClickbtn6)
btn6.grid(row=4,column=1,rowspan=2)
imgbtn8 = tk.PhotoImage(file='8.gif',width=101,height=101)
btn8 = tk.Button(root,text='五子棋',cursor='heart',image =imgbtn8,command = onClickbtn8)
btn8.grid(row=6,column=1,rowspan=2)
imgbtn9 = tk.PhotoImage(file='9.gif',width=101,height=101)
btn9 = tk.Button(root,text='五子棋',cursor='heart',image =imgbtn9,command = onClickbtn9)
btn9.grid(row=6,column=0,rowspan=2)


# imgbtn7 = tk.PhotoImage(file='7.gif',width=410,height=100)
btn7 = tk.Button(root,text='破解合集,敬请期待！',cursor='heart',bg='yellow',command = onClickbtn7)
btn7.grid(row=8,column=0,rowspan=4,columnspan=4,ipadx=50,ipady=20)

if __name__ == '__main__':
    # 加入消息循环
    root.mainloop()
