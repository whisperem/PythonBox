# coding=utf-8
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import requests
import re
import json
import os
from tkinter import StringVar


def windows():
    global var
    root = tk.Tk()
    var = StringVar()
    root.geometry("400x300+450+100")
    root.resizable(width=False, height=False)
    root.title('百度文库下载器！！！')
    # photo = tk.PhotoImage(file="背景图片.gif")
    # theLabel = tk.Label(root,justify=tk.LEFT,image=photo,compound = tk.CENTER,font=("华文行楷",20),fg = "white")
    # theLabel.pack()
    label = tk.Label(root, text="输入文库地址: 注意链接格式需要以“.html”结尾，请自行补齐")
    label.pack(side='top')
    entry = tk.Entry(root,textvariable = var)
    entry.pack(side='top', expand='YES', fill='both')
    btn1 = tk.Button(root, text="下载", width=20, height=10, command=main)
    btn1.pack(side='right', expand='YES', fill='both')
    # btn1 = tk.Button(root, text="选择下载目录", width=20, height=10, command=chose)
    # btn1.pack(side='left')
    root.mainloop()
# def chose():
#     global dirpath
#     dirpath = tk.filedialog.askdirectory()
#     tk.messagebox.showinfo(title='添加结果', message='添加成功' + dirpath)

# def download():
#     tk.messagebox.showinfo(title='下载结果', message='成功下载到' + dirpath)


session = requests.session()
def fetch_url(url):
    return session.get(url).content.decode('gbk')

def get_doc_id(url):
    return re.findall('view/(.*).html', url)[0]

def parse_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]

def parse_title(content):
    return re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]

def parse_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result

def parse_txt(doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = fetch_url(content_url)
    md5 = re.findall('"md5sum":"(.*?)"', content)[0]
    pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
    rsign = re.findall('"rsign":"(.*?)"', content)[0]
    content_url = 'https://wkretype.bdimg.com/retype/text/' + doc_id + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsign
    content = json.loads(fetch_url(content_url))
    result = ''
    for item in content:
        for i in item['parags']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


def parse_other(doc_id):
    content_url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=" + doc_id + "&pn=1&rn=99999&type=ppt"
    content = fetch_url(content_url)
    url_list = re.findall('{"zoom":"(.*?)","page"', content)
    url_list = [item.replace("\\", '') for item in url_list]
    if not os.path.exists(doc_id):
        os.mkdir(doc_id)
    for index, url in enumerate(url_list):
        content = session.get(url).content
        path = os.path.join(doc_id, str(index) + '.jpg')
        with open(path, 'wb') as f:
            f.write(content)
    print("图片保存在" + doc_id + "文件夹")
    tk.messagebox.showinfo(title='下载结果', message='成功下载到当前目录')


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        print('已保存为:' + filename)
        tk.messagebox.showinfo(title='下载结果', message='成功下载到当前目录')



# test_txt_url = 'https://wenku.baidu.com/view/cbb4af8b783e0912a3162a89.html?from=search'
# test_ppt_url = 'https://wenku.baidu.com/view/2b7046e3f78a6529657d5376.html?from=search'
# test_pdf_url = 'https://wenku.baidu.com/view/dd6e15c1227916888586d795.html?from=search'
# test_xls_url = 'https://wenku.baidu.com/view/eb4a5bb7312b3169a551a481.html?from=search'
def main():
    # url = input('请输入要下载的文库URL地址')
    url = var.get()
    print(url)
    content = fetch_url(url)
    doc_id = get_doc_id(url)
    type = parse_type(content)
    title = parse_title(content)
    if type == 'doc':
        result = parse_doc(content)
        save_file(title + '.txt', result)
    elif type == 'txt':
        result = parse_txt(doc_id)
        save_file(title + '.txt', result)
    else:
        parse_other(doc_id)

if __name__ == '__main__':
    windows()

