import urllib.request
import urllib.parse
# 进不去  。。。
url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data={
'domain':'common',
'from':'en',
'query':'wolf',
'sign':'275695.55262',
'simple_means_flag':'3',
'to':'zh',
'token':'ce4ba7a890b5539bffeaf89b5c3d3e1a',
'transtype':'realtime',
}

data=urllib.parse.urlencode(data)
headers={
'Host': 'fanyi.baidu.com',
'Connection': 'keep-alive',
'Content-Length': '134',
'Accept': '*/*',
'Origin': 'https://fanyi.baidu.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Sec-Fetch-Mode': 'cors',
'Referer': 'https://fanyi.baidu.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'BIDUPSID=37218BEC5877C6783A3F839B86BF24E5; PSTM=1546095230; BDUSS=VlwOHFURGh1clc5bGNmM3p-ZXlBMFRtMkVUaVNMYWRQNnhpcjUtekdhQnR4UzFkSVFBQUFBJCQAAAAAAAAAAAEAAAAjyiLwwO9hbmc4OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG04Bl1tOAZdQ; BAIDUID=9A2FAD803D74BEC8C4854A00A3A8F509:FG=1; __guid=37525047.535785960061862660.1592448232563.664; monitor_count=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1592448233; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1592448233; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjsv5_shitong=1.0_7_97ad9803bda59557931b584dddd8785f3eba_300_1592448233387_223.89.2.111_b1e51c82; yjs_js_security_passport=48b5cc10a9c01518f3def4c44923ae68aa9d9ce7_1592448237_js',
}

request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(url=url,data=data.encode())
print(response.read().decode())