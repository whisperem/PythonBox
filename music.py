# coding=utf-8
# 导入相应模块
import pygame
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame.locals import *
import time
import sys
# 初始化
pygame.init()
# 设置用于播放歌曲的列表
fileslist = []
def play():
    """ 播放歌曲 """
    pygame.mixer.music.unpause()
def pause():
    """ 暂停播放 """
    pygame.mixer.music.pause()
def stop():
    """ 停止播放 """
    pygame.mixer.music.stop()
def opensong():
    """ 打开歌曲路径 """
    filessonglist = filedialog.askopenfilenames()  # 打开多个文件
    if not filessonglist:  # 判断是否添加曲库
        messagebox.showwarning("音乐", "当前未选择歌曲")
        return
    for item in filessonglist:  # 添加到播放列表当中
        fileslist.append(item)
        listname = item.split('/')
        listsong.insert(END, listname[len(listname) - 1])

def quit():
    """ 关闭窗口 """
    root.quit()


def playcurrentsong(*args):
    """ 播放当前列表歌曲 """
    indexs = listsong.curselection()
    selectindex = int(indexs[0])
    pygame.mixer.music.load(fileslist[selectindex])
    pygame.mixer.music.play()


def frontsong():
    """ 上一首 """


def nextsong():
    """ 下一首 """


root = Tk()  # 创建窗口
root.Color = "red"
root.title("YTouchMusic")  # 标题
root.resizable(width=False,height=False)
root.geometry('250x440+500+200')  # 设置窗口大小和位置
listsong = Listbox(root)  # 添加歌曲列表
listsong.pack(padx=5, pady=10, side=LEFT, expand = YES, fill = Y)  # 将列表放在左侧
listsong.bind("<<ListboxSelect>>", playcurrentsong)  # 点击列表,播放对应歌曲
'''menu = Menu()
me = Menu()#一级菜单
root.config(menu=me)#加入一级菜单
'''
root.attributes('-toolwindow', False,
                '-alpha', 0.9,  # 设置透明度
                '-topmost', True)
pygame.init()
pygame.mixer.init()
l = Label(root, text="YTouch - why")
l.pack()

'''相关button '''
btn_ChooseMusic = Button(root, text="选择文件", command=opensong)
btn_ChooseMusic.pack(padx=1, pady=12)
btn_Pause = Button(root,text="暂停播放",command=pause)
btn_Pause.pack(padx=1, pady=1)
btn_Continue = Button(root, text="继续", command=play)
btn_Continue.pack(padx=1, pady=5,ipadx=15)
btn_Stop = Button(root, text="停止", command=stop)
btn_Stop.pack(padx=1, pady=5,ipadx=15)
btn_Quit = Button(root, text="关闭", command=quit)
btn_Quit.pack(padx=1, pady=5,ipadx=15)
root.mainloop()  # 必需组件