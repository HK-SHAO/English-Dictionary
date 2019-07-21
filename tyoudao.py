import re
import time
import urllib.request


def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib.request.Request(url = url,headers=headers)    
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
        result2 = txt_wrap_by("""<div id="wordGroup2" class="trans-container tab-content hide more-collapse">""", """<div class="more"><a href="#" class="sp more_sp">&nbsp;</a>""", result)
        result = txt_wrap_by("""<span class="keyword">""", """<div id="webTrans" class="trans-wrapper trans-tab">""", result)
        pattern = re.compile(r'<[^>]+>', re.S)
        result = pattern.sub('', result)
        result = result.replace('\n', '【】')
        result = ' '.join(result.split())

        result2 = pattern.sub('', result2)
        result2 = result2.replace('\n', '【】')
        result2 = ' '.join(result2.split())

        dic = []
        dic.append(txt_wrap_by('{}【】 【】 英【】 '.format(content), '【】 【】 【】 美【】 ', result))
        dic.append(txt_wrap_by('【】 【】 【】 美【】 ', '【】 【】 【】 【】 【】 【】【】 【】', result))
        dic.append(txt_wrap_by('[【】', ']【】', result).replace('【】', ''))
        rsl = result2.replace('【】 【】 【】', '|').replace('【】', '').replace('  &nbsp', '').split('|')
        result2 = ''
        if len(rsl) > 1:
            n = 0
            for s in rsl:
                n += 1
                result2 += '{}.{}'.format(n, s)
                if n > 3:
                    break
            dic.append(result2[:-1])
        else:
            dic.append('')
        s = '{}  /{}/  /{}/'.format(content, dic[0][1:-1], dic[1][1:-1])
        return [s, dic[2], dic[3]]
    return []
    
def get(word):       
    return translate(word)
