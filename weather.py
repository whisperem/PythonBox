# coding=utf-8
from tkinter import *
from tkinter import StringVar
import json
import requests
root = Tk()
root.resizable(width=False,height=False)
root.geometry("500x500+500+100")
root.title("我是贴心小棉袄，查询一下天气吧！")
var = StringVar()
t = Text(root,bg='white')
t.place(y=60,width=450,height=400)
def getweather():
    city = var.get()     #用来获得单行文本框输入的内容
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='
    response = requests.get(url + city)
    data = response.json()['data']['forecast'][0]
    # {'date': '6日星期三', 'fengxiang': '西风', 'high': '高温 25℃', 'fengli': '<![CDATA[<3级]]>', 'type': '晴', 'low': '低温 13℃'}
    # forecast = weather_dict.get('data').get('forecast')
    # forecast[0].get('fengxiang')
    s = '%s :%s, %s' % (city, data['low'], data['high'])
    s1 = '风向 ：%s' %(data['fengxiang'])
    s2 = '风力 ：%s' % (data['fengli'])
    s3 = '天气：%s' % (data['type'])
    s4 = '日期：%s' % (data['date'])

    t.insert('1.0','\n'+s + '\n'+s3+'\n'+s1+'\n'+s2+'\n'+s4+'\n')  # 在多行文本框中插入获取的天气内容

#     # #将json数据转换为dict数据
#     # forecast = weather_dict.get('data').get('forecast')
#     # print('城市：',weather_dict.get('data').get('city'))
#     # print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
#     # print('感冒：',weather_dict.get('data').get('ganmao'))
#     # print('风向：',forecast[0].get('fengxiang'))
#     # print('风级：',forecast[0].get('fengli'))
#     # print('高温：',forecast[0].get('high'))
#     # print('低温：',forecast[0].get('low'))
#     # print('天气：',forecast[0].get('type'))
#     # print('日期：',forecast[0].get('date'))
#     # print('*******************************')
#     # four_day_forecast =input('是否要显示未来四天天气，是/否：')
#     # if four_day_forecast == '是' or 'Y' or 'y':
#     #     for i in range(1,5):
#     #         print('日期：',forecast[i].get('date'))
#     #         print('风向：',forecast[i].get('fengxiang'))
#     #         print('风级：',forecast[i].get('fengli'))
#     #         print('高温：',forecast[i].get('high'))
#     #         print('低温：',forecast[i].get('low'))
#     #         print('天气：',forecast[i].get('type'))
#
label = Label(root,text ="请输入需要查询的地点",font=("华文行楷",15),height=2)
label.place(x=0,y=0,anchor='nw')
entry = Entry(root,bg = 'yellow',font=('微软雅黑',15),width = 15,textvariable = var)
entry.place(x=390,y=0,anchor='ne')
Button(root,text='查询',bg='red',height=1,width = 13,command=getweather).place(x=390,y=0)
# Label_info =Label(root,bg='white',justify='left',anchor='nw')
# Label_info.place(y=60,width=450,height=400)

if __name__ == '__main__':
    root.mainloop()
