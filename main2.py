import tyoudao
import tgoogle

f = open('dic.txt', encoding='utf-8')
fi = f.read()
f.close()

ls = eval(fi)
for li in ls[:400]:
    try:
        s1 = tgoogle.get(li[0])
        s2 = tyoudao.get(li[0])
    except KeyboardInterrupt:
        quit()
    except:
        print('【错误】{}'.format(li[0]))
        continue
    s = '【【a1】】{}【【a2】】| 【【a3】】{}【【a4】】\n【【a5】】{}【【a6】】\n{}【【a7】】'.format(li[1], s2[0], s1[0], s2[1])
    print(s)
    f = open('english2.txt', 'a+', encoding='utf-8')
    f.write(s + '\n')
    f.close()
