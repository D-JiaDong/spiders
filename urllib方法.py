import urllib
from urllib import request
from urllib import parse
url="http://www.baidu.com"

#发送请求
response=request.urlopen(url)
#返回对象
# <http.client.HTTPResponse object at 0x0000029A16BD2080>

#转换编码.decode('utf-8') 默认为"utf-8"
#encode() 字符串转换为二进制
#decode() 二进制转换为字符串
#print(response.read().decode('utf-8'))
# html=response.read().decode('utf-8')
# print(html)
# try:
#     file=open('bd.html','w',encoding='utf8')
#     file.write(response.read().decode())
# except IOError:
#     print(IOError)
# else:
#     file.close()


# #获取请求的url
# print(response.geturl())
# print(dict(response.getheaders()))
# #获取状态码
# print(response.getcode())
# #按行读取 返回列表 字节码
# print(response.readlines())

with open('bd.html','wb') as file:
   file.write(response.read())

url="https://img.tupianzj.com/uploads/allimg/202005/9999/d3e2657487.jpg"
response=request.urlopen(url)

with open('qing.jpg','wb') as file:
   file.write(response.read())

urllib.request.urlretrieve(url,'chun.jpg')