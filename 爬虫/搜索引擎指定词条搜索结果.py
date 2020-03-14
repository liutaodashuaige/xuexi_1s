# encoding:utf-8
import requests
#UA伪装
#头信息字典
headers={
    'Accept':'* / *',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN',
    'Cache - Control': 'no - cache',
    'Connection': 'Keep - Alive',
    'Host': 'www.baidu.com',
    'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
sr=input('键入关键字：')
#参数字典

url='http://www.baidu.com/s?wd='+sr+'&pn=1'

#携带参数与头信息的get请求
hezi=requests.get(url=url,headers=headers)
hezi.encoding='utf-8'
citiao_text=hezi.text
filename=sr+'.html'
with open(filename,'w',encoding='utf-8')as fp:
    fp.write(citiao_text)
print(filename,'保存完毕。')
