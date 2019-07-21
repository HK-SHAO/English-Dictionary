import urllib.request
import re

def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib.request.Request(url = url,headers=headers)    
    response = urllib.request.urlopen(req)    
    data = response.read().decode('utf-8')    
    return data

def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()
    return ''
    
def translate(content):    
    content = urllib.parse.quote(content)    
    url = 'http://dict.youdao.com/w/{}'.format(content)
    result = open_url(url)    

    if len(result) > 0:
        r1 = txt_wrap_by("""<span class="keyword">""", """<div id="webTrans" class="trans-wrapper trans-tab">""", result)
        r2 = txt_wrap_by("""<a rel="#bilingual"><span>双语例句</span></a><a rel="#originalSound">""", """的双语例句">更多双语例句</a>""", result)
        r3 = txt_wrap_by("""<a rel="#wordGroup"><span>词组短语</span></a>""","""<!--例句选项卡 begin-->""", result)
        result = r1 + r2 + r3
        pattern = re.compile(r'<[^>]+>', re.S)
        result = pattern.sub('', result)
        result = result.replace('\n', '【】')
        result = ' '.join(result.split())

        dic = {'word':content, 'ying_yb':'', 'mei_yb':'', 'bianxing':'', 'shiyi':'', 'lijv':'', 'duanyv':'', 'jinyi':''}
        dic['ying_yb'] = txt_wrap_by('{}【】 【】 英【】 '.format(content), '【】 【】 【】 美【】 ', result)
        dic['mei_yb'] = txt_wrap_by('【】 【】 【】 美【】 ', '【】 【】 【】 【】 【】 【】【】 【】', result)
        dic['bianxing'] = txt_wrap_by('【】 【】 [【】 ', ']【】 【】 原声例句权威例句', result)
        dic['shiyi'] = txt_wrap_by('【】 【】 【】 【】 【】 【】【】 【】 ', '【】 【】', result)
        dic['lijv'] = txt_wrap_by('原声例句权威例句', '【】 【】 【】', result)
        dic['duanyv'] = txt_wrap_by('【】 【】 【】 【】 【】 【】 【】 ', '【】 【】 【】 【】【】', result)
        dic['jinyi'] = txt_wrap_by('【】 【】 【】 【】【】', '【】 【】 【】【】【】 【】', result)

        print(dic)
        f = open('trans.txt', 'w', encoding='utf-8')
        f.write(str(dic).replace('【】', '\n'))
        #f.write(result)
        f.close()
    
def main():       
    while True:    
        content = input("输入待翻译内容：")    
        if content == 'q!':    
            break    
        translate(content)    
        
if __name__ == "__main__":    
    main()  
