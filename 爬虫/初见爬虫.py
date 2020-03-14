# encoding:utf-8
import requests
#1.指定url
url='https://www.sogou.com/'
#2.发起请求/返回响应对象
hezi=requests.get(url=url)
hezi.encoding='utf-8'
#3.获取响应数据/返回字符串形式响应数据
pachong_text=hezi.text
print(pachong_text)
#4.持久性保存
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(pachong_text)
    print('爬取完成~')