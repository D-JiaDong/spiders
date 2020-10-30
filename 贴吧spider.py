import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os
url='https://tieba.baidu.com/f?&ie=utf-8&pn=50'

# pn第n页 （n-1）*50

tiebaname=input("请输入吧名")
startpage=int(input("请输入起始页码"))
endpage=int(input("请输入结束页码"))

if os.path.exists(tiebaname):
    pass
else:
    os.mkdir(tiebaname)
for page in range(startpage,endpage+1):
    query_string={
        'kw':tiebaname,
        'pn':(page-1)*50
    }

    query_string=urllib.parse.urlencode(query_string)
    url_=url+query_string

# 构建请求对象
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'
    }
    resquest=urllib.request.Request(url=url_,headers=headers)
    print("第{}页开始下载".format(page))
    response=urllib.request.urlopen(resquest)
# 声明文件名
    filename=tiebaname+'_'+str(page)+'.html'
    filepath=tiebaname+'/'+filename
# 写入文件
#     print(response.read().decode('utf-8'))
    with open(filepath,'wb') as fp:
        fp.write(response.read())
    print("第{}页下载结束".format(page))
    # html = BeautifulSoup(response.read().decode(), "html.parser")
    # print(html)
    # print(response.read().decode())