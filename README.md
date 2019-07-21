# English-Dictionary
**这是一个适用于高考的英语词典**

搜集了历年来各个省份的高三英语模拟卷和历年来的高考英语全国卷总共130多份电子文档，统计其中所有的大约50多万单词，得到不同单词的频数。使用python爬取了Google翻译的汉语释义和英文释义，有道词典的单词音标和单词的短语。整理好后用Word进行排版，最后导出pdf到网店进行封装打印成书。成果如下图：
![](/images/34.PNG)

## 简单介绍

- 此书分为三部分，重点部分，基础部分和单词目录。  
- 本书中所有的单词都按照频数排序。
- 所有的单词左上角会有一个频数统计，统计的是130多份高三考卷里50万单词中的此单词出现次数。  
- 所有的单词都有英美音标和谷歌翻译里地道的中文释义，释义区分词性，并用简单明了的中文区分。  
- 本书中的部分常用单词会有单词变形（不同词性和时态形式） 。
- 重点部分的单词的不同词性都会有英英释义（定义）和这个释义的例句（没有中文，目的是为了促进学生自己按照中文释义和英英释义去代入语境并理解，而不是依赖中文翻译）。  
- 重点部分的单词都有常见短语和翻译。  
- 基础部分的单词由于过于基础，所以不给出英英释义和例句。但是有音标，中文释义和单词变形等。  
- 单词目录是按照字母顺序排列的，方便查找。

## 词典制作简要

### 搜集和整理考题数据

主要是在百度文库，百度高考估分和e网通下载文档，下载和整理过滤均为手工。成果如下：
![](/images/27.PNG)

接着手工把所有文档打开，把所有文档中的文字整理到一个txt文件里，使用VS Code打开这个文档，用正则表达式`[^a-z]`去除所有的非英文字符，然后把所有的多余空格去掉，把不同单词之间的空格替换成逗号。效果如下：
![](/images/28.PNG)

### 编写Python程序统计单词频数

同时编写程序过滤掉重复的单词和长度小于4的单词，并且过滤掉常见的人名和地名。相比之前的程序，这个程序因为使用了字典而大幅度提高了运行效率。代码如下：

```
f = open('words.txt')
word = f.read().split(',')
f.close()

# 过滤表（去除人名地名）
f = open('filter.txt', encoding='utf-8')
fi = dict.fromkeys(f.read().split(','))
f.close()

dic = dict()
for w in word:
    if len(w) < 4 or w in fi:
        continue
    if len(w) == 4 and w[-1] == 's':
        continue
    dic.setdefault(w, 0)
    dic[w] += 1

# 去除重复单词
for w in list(dic.keys()):
    if not w in dic:
        continue
    if w + w[-1] + 'ing' in dic:
        dic[w] += dic.pop(w + w[-1] + 'ing')
    if w + w[-1] + 'ed' in dic:
        dic[w] += dic.pop(w + w[-1] + 'ed')
    if w + 'ing' in dic:
        dic[w] += dic.pop(w + 'ing')
    if w + 'ed' in dic:
        dic[w] += dic.pop(w + 'ed')
    if w + 's' in dic:
        dic[w] += dic.pop(w + 's')
    if w + 'es' in dic:
        dic[w] += dic.pop(w + 'es')
    if w + 'ly' in dic:
        dic[w] += dic.pop(w + 'ly')

l = []
for k in sorted(dic,key=dic.__getitem__,reverse=True):
    l.append([k, dic[k]])

f = open('dic.txt', 'w')
word = f.write(str(l))
f.close()
```

得到一个频数列表：
![](/images/29.PNG)

### 编写Google翻译爬虫和有道词典爬虫

这部分参考了网上的很多代码，因为代码太多所以只贴上main程序。其中的【【】】是标签，方便后面排版时进行文字处理。

```
import tyoudao
import tgoogle

f = open('dic.txt', encoding='utf-8')
fi = f.read()
f.close()

ls = eval(fi)
for li in ls[:3000]:
    try:
        s1 = tgoogle.get(li[0])
        s2 = tyoudao.get(li[0])
    except KeyboardInterrupt:
        quit()
    except:
        print('【错误】{}'.format(li[0]))
        continue
    s = '【【a1】】{}【【a2】】| 【【a3】】{}【【a4】】\n【【a5】】{}【【a6】】\n{}【【a7】】\n【【a8】】{}【【a9】】\n【【a10】】{}【【a11】】'.format(li[1], s2[0], s1[0], s2[1], s2[2], s1[1])
    print(s)
    f = open('english.txt', 'a+', encoding='utf-8')
    f.write(s + '\n')
    f.close()

```

最后得到排版前数据：
![](/images/30.PNG)

### 使用LibreOffice进行排版

说实话我不喜欢也不会用Office系列软件，由于没有正版Office软件，我只好用免费开源的LibreOffice进行排版。由于某些单词音标不全，我还只好手动去网上搜索然后编辑进去。排版过程及其痛苦，不停的使用搜索和替换功能，写了无数次正则表达式和用了无数次通配符。最坑的就是添加单词目录，我使用了各种文本处理方法手工制作了单词目录。在无数次机械般的试错和百度搜索之后，终于排版好了。最后进行微调和添加页码水印，导出pdf。
![](/images/31.PNG)

### 最终成果

最后打印封装这些就是网店的事情了，这里就不多说了。
![](/images/32.GIF)
![](/images/33.PNG)
![](/images/34.PNG)
![](/images/35.PNG)