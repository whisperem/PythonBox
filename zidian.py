# coding=utf-8
import tkinter
from tkinter import messagebox
import requests
from tkinter import StringVar
# class Zd:
# def __int__():
root = tkinter.Tk()
root.title('中英互译')
root.resizable(width=False,height=False)
root.geometry('500x100+500+300')
def translation():
    content = entry.get()
    if content =='':
        messagebox.showinfo('提示','请输入要翻译的单词')
    else:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        date = {}
        date['i']=content
        date['from']='AUTO'
        date['to']='AUTO'
        date['smartresult']='dict'
        date['client']='fanyideskweb'
        # 加密时间戳
        # date['salt']='15690498311326'
        # 加密数字签名
        # date['sign']='6700c91f1b678fa425e388f03300708b'
        date['ts']='1569049831132'
        date['bv']='a4f4c82afd8bdba188e568d101be3f53'
        date['doctype']='json'
        date['version']='2.1'
        date['keyfrom']='fanyi.web'
        date['action']='FY_BY_CLICKBUTTION'
        result = requests.post(url,data=date,headers = header)
        translation =result.json()
        translation = translation['translateResult'][0][0]['tgt']
        res.set(translation)

# self.windows()
# self.translation()
# def windows(self,root):
label = tkinter.Label(root, text='输入需要翻译的内容:', font=('微软雅黑'))
label.grid()
label1 = tkinter.Label(root, text='翻译之后的结果:', font=('微软雅黑'))
label1.grid()
# 为翻译结果赋值一个变量
res = tkinter.StringVar()
entry = tkinter.Entry(root, font=('华文仿宋', 15), width=37, bg='yellow')
entry.grid(row=0, column=2)
entry1 = tkinter.Entry(root, width=37, bg='yellow', font=('华文仿宋', 15), textvariable=res)
entry1.grid(row=1, column=2, sticky='W')
btn = tkinter.Button(root, text='翻译', font=('微软雅黑', 10), width=20, command=translation)
btn.grid(row=2, column=0, sticky='ws')
btn1 = tkinter.Button(root, text='退出', font=('微软雅黑', 10), width=20, command=root.quit)
btn1.grid(row=2, column=2, sticky='e')
root.mainloop()



# file = Zd()
# file.windows(root)
# file.translation()


