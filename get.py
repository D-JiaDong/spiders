import urllib.request
import urllib.parse

word=input('请输入你想要搜索的内容：')

url="http://www.baidu.com/s?"
data={
    'ie':'utf-8',
    'wd':word,
}
query_string=urllib.parse.urlencode(data)
url=url+query_string

response=urllib.request.urlopen(url)
with open(word+'.html','wb') as file:
    file.write(response.read())
file.close()