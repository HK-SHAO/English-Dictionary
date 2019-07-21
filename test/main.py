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
        result = txt_wrap_by("""<span class="keyword">""", """<div id="webTrans" class="trans-wrapper trans-tab">""", result)
        pattern = re.compile(r'<[^>]+>', re.S)
        result = pattern.sub('', result)
        result = result.replace('\n', '【】')
        result = ' '.join(result.split())

        dic = []
        dic.append(txt_wrap_by('{}【】 【】 英【】 '.format(content), '【】 【】 【】 美【】 ', result))
        dic.append(txt_wrap_by('【】 【】 【】 美【】 ', '【】 【】 【】 【】 【】 【】【】 【】', result))
        dic.append(txt_wrap_by('[【】', ']【】', result))
    
def main():       
    while True:    
        content = input("输入待翻译内容：")    
        if content == 'q!':    
            break    
        translate(content)    
        
if __name__ == "__main__":    
    main()  
