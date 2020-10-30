import urllib.request
import urllib.parse

# url='https://movie.douban.com/j/chart/top_list?type=5&interval' \
#     '_id=100%3A90&action=&start=0&limit=20 '
url='https://movie.douban.com/j/chart/top_list?type=5&interval' \
    '_id=100%3A90&action=&'

# start=0&limit=20 开始和偏移量

page=int(input("请输入想要第几页的数据"))
number=int(input("请输入一页多少数据"))

data={
    'start':(page-1)*number,
    'limit':number,
}

query_string=urllib.parse.urlencode(data)
url=url+query_string

# 构建请求对象
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'

}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
print(response.read().decode())