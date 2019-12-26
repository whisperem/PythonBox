# coding=utf-8
import tkinter
# 导入选择文件模块filedialog
import tkinter.filedialog
#导入压缩模块zipfile
import zipfile
# 导入文件操作模块
import os
import tkinter.messagebox

root = tkinter.Tk()
root.resizable(width=False,height=False)
root.geometry('300x400')
root.title('压缩软件1.0')

# 设置文件全局变量，用于压缩和解压缩函数
filelists = []
#添加文件函数
def addfiles():
    global filelists
    # 添加文件操作，需用到filedialog
    paths = tkinter.filedialog.askopenfilenames(title='请选择所需的文件')
    # 保存用户添加的文件，并赋予全局变量
    # 遍历用户元祖，逐个添加
    for path in paths:
        filelists.append(path)
    # 显示获得的路径
    label_info['text'] = '\n'.join(filelists)

def compress():
    global filelists
    #用户选择压缩路径
    zippath = tkinter.filedialog.asksaveasfilename(filetypes = (('zip文件','*.zip'),))
    # 创建并打开压缩文件
    zp = zipfile.ZipFile(zippath,'a')
    # 压缩文件
    for filename in filelists:
        zp.write(filename,os.path.basename(filename))
    # 关闭压缩
    zp.close()
    # 显示压缩成功信息
    tkinter.messagebox.showinfo(title='操作结果',message='压缩成功')

def uncompress():
    #打开路径查找需要解压的文件
    zippath = tkinter.filedialog.askopenfilename()
    #打开文件
    zp = zipfile.ZipFile(zippath,'r')
    #解压文件
    dirpath = tkinter.filedialog.askdirectory()
    zp.extractall(dirpath)
    #关闭解压
    zp.close()
    #添加提示信息
    tkinter.messagebox.showinfo(title='解压结果',message='解压成功'+dirpath)
btn_addfiles = tkinter.Button(root,text='添加文件',command = addfiles)
btn_addfiles.place(x=10,y=20,width=80,height=30)

btn_compress = tkinter.Button(root,text='压缩文件',command = compress)
btn_compress.place(x=110,y=20,width=80,height=30)

btn_uncompress = tkinter.Button(root,text='解压文件',command = uncompress)
btn_uncompress.place(x=210,y=20,width=80,height=30)
label_info = tkinter.Label(root,bg='yellow',anchor = 'nw',justify='left')
label_info.place(x=10,y=70,width=280,height=320)
if __name__ == '__main__':
    root.mainloop()