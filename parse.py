import urllib.parse
image_url="https://img.tupianzj.com/uploads/allimg/170120/9-1F120203304.jpg"

#url只能由一些特定的字符组成
#如果出现其他的 比如￥ 空格 中文 就要对其进行编码
url='http://www.baidu.com/index.html?name=狗蛋&pwd=123456'
ret=urllib.parse.quote(url)
re=urllib.parse.unquote(ret)
print(ret)
print(re)

url='http://www.baidu.com/index.html'
url='http://www.baidu.com/index.html'
#假如参数有 name age sex height
data={
'name':'张三',
'age':18,
'sex':'nv',
'height':180,
}
lt=[]
for k,v in data.items():
    lt.append(k+'='+str(v))
query_string='&'.join(lt)
url=url+'?'+query_string
print(url)

# 编码url
query_string=urllib.parse.urlencode(data)
print(query_string)