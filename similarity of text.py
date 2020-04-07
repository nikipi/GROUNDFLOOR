import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import math
import re
import time

#输入的是每一行
data=pd.DataFrame([['1','2','4'],['1','3','4'],['1','2','4'],['3','5','6']],columns=['one', 'two', 'three'])
print(data)
print(data.drop_duplicates())
f=data.drop_duplicates(keep=False)
#不保留重复值
print(f)


w=pd.concat([data.drop_duplicates(),data.drop_duplicates(keep=False)]).drop_duplicates(keep=False)
print(w)


inputStr = "hello 111 world 111"
replacedStr = inputStr.replace("111", "222")
print(replacedStr)
inputStr = "hello 123 world 456"
replacedStr = re.sub("\d+", "222", inputStr)
print(replacedStr)

dict3 = {'name':'z','Age':7,'class':'First'};
print("Value : ",dict3.__contains__('name'))
print("Value : ",dict3.__contains__('sex'))


'''
下面举一个例子，来说明余弦计算文本相似度】

举一个例子来说明，用上述理论计算文本的相似性。为了简单起见，先从句子着手。

句子A：这只皮靴号码大了。那只号码合适

句子B：这只皮靴号码不小，那只更合适

怎样计算上面两句话的相似程度？

基本思路是：如果这两句话的用词越相似，它们的内容就应该越相似。因此，可以从词频入手，计算它们的相似程度。

第一步，分词。

句子A：这只/皮靴/号码/大了。那只/号码/合适。

句子B：这只/皮靴/号码/不/小，那只/更/合适。

第二步，列出所有的词。

这只，皮靴，号码，大了。那只，合适，不，小，很

第三步，计算词频。

句子A：这只1，皮靴1，号码2，大了1。那只1，合适1，不0，小0，更0

句子B：这只1，皮靴1，号码1，大了0。那只1，合适1，不1，小1，更1

第四步，写出词频向量。

　　句子A：(1，1，2，1，1，1，0，0，0)

　　句子B：(1，1，1，0，1，1，1，1，1)

到这里，问题就变成了如何计算这两个向量的相似程度。
我们可以把它们想象成空间中的两条线段，都是从原点（[0, 0, ...]）出发，指向不同的方向。
两条线段之间形成一个夹角，如果夹角为0度，意味着方向相同、线段重合,这是表示两个向量代表的文本完全相等；
如果夹角为90度，意味着形成直角，方向完全不相似；如果夹角为180度，意味着方向正好相反。
因此，我们可以通过夹角的大小，来判断向量的相似程度。夹角越小，就代表越相似。
'''
text1 = "This game is one of the very best. games ive  played. the  ;pictures? \
        cant descripe the&&＊＊ real graphics in the game."

a=re.sub('[^a-zA-Z]',' ',text1)
#[^a-zA-Z]是去匹配目标字符串中非a—z也非A—Z的字符
print(a)


import jieba
import math
#把词划分出来
s1 = '这只皮靴号码大了。那只号码合适'
s1_cut = [i for i in jieba.cut(s1, cut_all=True) if i != '']
s2 = '这只皮靴号码不小，那只更合适'
s2_cut = [i for i in jieba.cut(s2, cut_all=True) if i != '']
print('s1 is',s1_cut)
print('s2 is',s2_cut)

#做出词的合集
word_set = set(s1_cut).union(set(s2_cut))
print('this is word set', word_set)

word_dict = dict()
i = 0
for word in word_set:
    word_dict[word] = i
    i += 1
print('num of words is',word_dict)
#计算出词频

s1_cut_code = [word_dict[word] for word in s1_cut]
print('s1_cut_code is',s1_cut_code)
#写出词频向量

s1_cut_code = [0]*len(word_dict)
for word in s1_cut:
    s1_cut_code[word_dict[word]]+=1
print('s1_cut_code2 is',s1_cut_code)
#写出词频向量
s2_cut_code = [word_dict[word] for word in s2_cut]
print(s2_cut_code)


s2_cut_code = [0]*len(word_dict)
for word in s2_cut:
    s2_cut_code[word_dict[word]]+=1
print(s2_cut_code)
#one hot编码计算根据在词袋中的位置表示出词在句子中出现的次数

# 计算余弦相似度
sum = 0
sq1 = 0
sq2 = 0
for i in range(len(s1_cut_code)):
	sum += s1_cut_code[i] * s2_cut_code[i]
	sq1 += pow(s1_cut_code[i], 2)
	sq2 += pow(s2_cut_code[i], 2)

try:
	result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
except ZeroDivisionError:
    result = 0.0
print(result)




