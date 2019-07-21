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