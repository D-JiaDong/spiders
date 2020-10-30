import urllib.request
import urllib.parse
url="http://www.moe.gov.cn/jyb_sy/sy_jyyw/index.html"

# response=urllib.request.urlopen(url)
# print(response.read().decode())
# 伪装自己的UA 让服务端认为你是浏览器在上网
# 构建请求对象：urllib.request.Request()

headers={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
# 构建请求对象：urllib.request.Request()
response=urllib.request.urlopen(request)
print(response.read().decode())
