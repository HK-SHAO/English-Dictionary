import requests #导入需要的包
import json

search = input("请输入你要翻译的内容:")

url = "http://fanyi.baidu.com/extendtrans" #请求的地址
headers={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"} #设置请求的头部

#设置提交的数据
posData={"query":search, "from":"en", "to":"zh"}

response = requests.post(url=url,data=posData,headers=headers)#模拟请求

#获取response的数据有2种方式 一种是text获取的直接是文本格式 但是可能有乱码 需要手动设置response.encoding("编码") 解决乱码
#还有一种就是response.content 里面存的是网站直接返回的数据 二进制格式 然后通过decode解码即可
#因为返回的是json对象，所以我们将最后解码后的字符串进行json格式转换 使用json.loads()进行转换
json_data=json.loads(response.content.decode())

#然后我们可以通过格式化工具进行json的解析
print(json_data)