import urllib.request
import time
from HandleJs import Py4Js


def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib.request.Request(url = url, headers=headers)    
    i = 0
    response = None
    while i < 2:
        try:
            response = urllib.request.urlopen(req, timeout=3)
            break
        except:
            time.sleep(3)
            i += 1
    data = response.read().decode('utf-8')    
    return data    
    
def translate(content,tk):    
    content = urllib.parse.quote(content)    
    url = """http://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&source=bh&ssel=0&tsel=0&kc=1&tk=%s&q=%s"""%(tk,content)
    result = str(open_url(url)).replace('null', '"null"').replace('true', 'True').replace('false', 'False')
    table = eval(result)

    # 单词释义
    ss1 = ''
    for i in table[1]:
        s2 = ''
        n = 0
        for i2 in i[1]:
            n += 1
            s2 += '{}，'.format(i2)
            if n == 3:
                break
        ss1 += '；{}：{}'.format(i[0], s2[0:-1])

    # 单词定义及例句
    ss2 = ''
    for i in table[12]:
        s2 = ''
        n = 0
        for i2 in i[1]:
            n += 1
            s2 += '\n{}：{}'.format(n, i2[0])
            if len(i2) > 2:
                s3 = ''
                if i2[-1] == '.':
                    s3 = '{}{}'.format(i2[2][0].upper(), i2[2][1:])
                else:
                    s3 = '{}{}.'.format(i2[2][0].upper(), i2[2][1:])
                s2 += '\n例：{}'.format(s3)
            if n == 2:
                break
        ss2 += '{}定义：{}\n'.format(i[0], s2)
    return [ss1[1:], ss2]

js = Py4Js()
def get(word):    
    tk = js.getTk(word)    
    return translate(word, tk)
