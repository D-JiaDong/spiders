import urllib.request
import urllib.parse

url="http://www.baidu.com/"

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

# 创建一个handler
handler=urllib.request.HTTPHandler()
# 通过handler创建一个opener opener就是一个对象
opener=urllib.request.build_opener(handler)
# 构建请求对象
request=urllib.request.Request(url=url,headers=headers)
# 发送请求
reponse=opener.open(request)

print(reponse.read().decode())

