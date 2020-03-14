# encoding:utf-8
import requests
import json
from tkinter import *

#图形界面
mygui=Tk(className='百度翻译')
Label1 = Label(mygui,text='关键字：').pack()
sr1 = StringVar()
e1 = Entry(mygui,textvariable=sr1,width=50).pack()
Label2 = Label(mygui,text='译文：').pack()
text1 = Text(mygui,width=50,height=10,font='宋体')
text1.pack()

#定义触发函数
def fy():
    url='https://fanyi.baidu.com/sug'
    #sr=input('键入关键字：')
    sr=sr1.get()
    #参数字典
    cszd={
        'kw':sr
    }
    #UA伪装
    #头信息字典
    headers={
        'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }

    #发起post请求
    hezi=requests.post(url=url,data=cszd,headers=headers)
    #返回响应数据对应类型的对象(json将返回obj)
    dic_obj=hezi.json()
    #转化为字符串
    #json_str=json.dumps(dic_obj,indent=2,ensure_ascii=False)
    #字典字段取值
    text1.delete(1.0,END)
    text1.insert(END,dic_obj['data'][0]['k']+dic_obj['data'][0]['v'])
    #text1.insert(END,json_str)
    #存储该返回值
    #fp=open('./'+sr+'.json','w',encoding='utf-8')
    #json.dump(dic_obj,fp=fp,ensure_ascii=False)
    #print('爬取完成。')

b1=Button(mygui,text='翻译',width=10,command=fy).pack()
mygui.mainloop()

