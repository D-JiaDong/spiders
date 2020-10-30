import urllib.request
import urllib.parse

post_url="https://fanyi.baidu.com/sug"
word=input("请输入您要查询的英文单词")
form_data={
    'kw':word
}
headers={
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'
}
# post请求不需要拼接

#处理post表单数据
form_data=urllib.parse.urlencode(form_data).encode()

#构造请求对象
request=urllib.request.Request(url=post_url,headers=headers)
#发送请求
response=urllib.request.urlopen(request,data=form_data)
print(response.read().decode('utf-8'))
