import urllib.request
import urllib.parse

url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

city=input("请输入要查询的城市")
page=input('请输入要查询第几页')
size=input('请输入要查询对少')
formdata={
'cname': city,
'pid': '',
'pageIndex': page,
'pageSize': size,
}

formdata=urllib.parse.urlencode(formdata).encode()

headers={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'
}

request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request,formdata)
print(response.read().decode())