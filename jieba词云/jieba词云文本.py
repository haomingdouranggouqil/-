import jieba
import re
path = '庾子山集.txt'
openpath = '庾子山集jieba分词文本.txt'
file = open(path, 'r')
write = open(openpath, 'a+')
txt = file.read()
file.close()
'''
text = ' '.join(jieba.cut(txt))
jiebatext = re.split('。|，|？| |！|；|\n', text)
for i in jiebatext:
    if i == '':
        jiebatext.remove('')
        '''
text = []
exclude= "，。！？、 （）【】<>《》=：+-*—“”…\n"
for i in jieba.cut(txt):
    if i in exclude:
        pass
    else:
        text.append(i)

texttxt = ' '.join(text)
write.write(texttxt)
write.close()
