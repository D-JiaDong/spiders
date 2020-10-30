#URLError: 断网 服务区连接失败 找不到指定的服务器
import urllib.request
import urllib.parse
import urllib.error
url="http://www.danol.com/"
url="http://www.bbbbbbbdu.com"
try:
    response=urllib.request.urlopen(url)
    print(response)
except urllib.error.URLError as e:
    print(e.code)
