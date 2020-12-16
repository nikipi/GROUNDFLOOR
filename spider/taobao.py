
import re
import time
import pandas as pd
import string
import pandas as pd
import numpy as np
import nltk
import jieba #for tokenizing Chinese
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import collections
import random
import operator
import io

import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import re
import time
import pandas as pd
import string
import pandas as pd
import numpy as np
import nltk
import jieba #for tokenizing Chinese
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import collections
import random
import operator
import io

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import colors



def get_the_information(link, referer,cookie,user_agent):
    rate = []

    for n in range(1, 2):
        url = re.sub("currentPage=(.*?)&append", 'currentPage=' + str(n) + '&append', link)

        header={
                'referer': referer,
                'cookie':  cookie,
              'usee-agent': user_agent }

        time.sleep(5)

        data = requests.get(url, headers=header).text

        pat = '"rateContent":"(.*?)","formMall"'
        pat = re.compile('"rateContent":"(.*?)","fromMall"')
        pat.findall(data)
        rate.extend(pat.findall(data))

    df = pd.DataFrame()
    df['rate'] = rate
    return df


df=get_the_information('https://rate.tmall.com/list_detail_rate.htm?itemId=527659339307&spuId=519288069&sellerId=1023696028&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hv3vvbvnQvUpCkvvvvvjiWP2Lh6j3RPsshsjnEPmPW6jinRFS9tjYURF5WAjiPRUvCvCBk7eqMvr147Di40nGD1tSRs%2BAmRIOCvvpv9hCvi9hvCvvvpZpRvpvhMMGvvv9CvhAv7a5Xjam4eBOqb64B9Cka%2BfvsxI29jLeARFxjKOmAdXKKNB3rs8Tr%2BulQbc7Q%2Bu04d56K6we6nqWcEDoYr4h6%2B2y2fEVxHb8re166Kvhv8vvvpHwvvv2FvvC2vvvvvNIvvhcDvvmCp9vvBwwvvUV0vvCH8Qvv9o8UvpvVvpCmpJ2wuvhvmvvvpLJ1ZqwavvhvC9mvphvvv29CvvpvvhCvRvhvCvvvphv%3D&needFold=0&_ksTS=1608143634962_1138&callback=jsonp1139',
                       'https://detail.tmall.com/item.htm?spm=a230r.1.14.8.63464561MKM7Dm&id=527659339307&ns=1&abbucket=14&skuId=3143108000479',
                       't=81c3a1e1ef27b3eab361582d3f0b3c49; _tb_token_=eeed5a31e153e; cookie2=196083c6f39bb46db593b2c7e14b38d9; cna=jfo+GN118QgCAVRKcxwtPGu0; hng=GLOBAL%7Czh-CN%7CUSD%7C999; dnk=maglu%5Cu9E6D; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie14=Uoe0al0vAht1dw%3D%3D&pas=0&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&nk2=DlGh0bUWXg%3D%3D&vt3=F8dCuAJ1IMlgH726S9Y%3D&id2=UUtMGNbJ1IfPCA%3D%3D; tracknick=maglu%5Cu9E6D; lid=maglu%E9%B9%AD; uc4=nk4=0%40DDSwHZPGSN%2FD9qOE1tQH9LxW&id4=0%40U2l2wpMkqj54k%2BGCP6OkhMfDFypw; lgc=maglu%5Cu9E6D; sgcookie=E100OS2cQ%2BRBTUu0OmmrXLcPx%2BgixtTlS6iWhZBgNWHGqyk2PJogSgAOKzh5NaS9qyPAaniCsZYQWhbBp1nu9t1vBQ%3D%3D; csg=72088690; enc=UhaZze0SewcDhNk1Rme7Ki2oO6r5iJtUJ6y3lhvXcTfi7O9O63kLsN45ueWAbv2OIhJl2voH5YsF6RM48RtZzg%3D%3D; _m_h5_tk=6ec0053715e088f064aabd6a9a615a6b_1607799056416; _m_h5_tk_enc=c679562836f6f7313657009760b3f54a; xlly_s=1; tfstk=cxXGBiXT2eg5PTRhNR91qwkWklzRZGneWZ71L9so0d7wKeBFiHcEaxjUtebGHj1..; l=eB__sRfcODlNYTZfBOfZnurza77TQIRAguPzaNbMiOB19X5_kd3vvHwhNp-Md3QLtt1fGetr0YibvRLHRnZDikfQ7_5LaCRZnxf..; isg=BPPzoHFAqEBi_mQA4u-3J7uXgvEdKIfqHovFVaWQVZIcpBNGLfmDOziyX8xKBN_i',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~、《【】》\,\n \t。“（）'  # `|` is not present here
transtab = str.maketrans(dict.fromkeys(punct, ''))

df['rate'] = '|'.join(df['rate'].tolist()).translate(transtab).split('|')

import pandas as pd
import numpy as np

df=pd.read_csv('rate.csv')

df['dry_skin']=np.where(df['rate'].str.contains('干皮|干性皮肤'),1,0)
df['oil_skin']=np.where(df['rate'].str.contains('油皮|油性皮肤'),1,0)

rate=df['rate'].tolist()
print(rate)

input_dict = {"text": rate}

import paddlehub as hub
senta = hub.Module(name="senta_bilstm")
results = senta.sentiment_classify(data=input_dict)

review=[]
for result in results:
    review.append(result.get('positive_probs'))

df['positive']=pd.Series(review)

df.to_csv('rate.csv')










def clean_the_stop(x):

    stop_words = [line.strip() for line in io.open('/Users/ypi/Desktop/中文停用词表.txt', 'r', encoding='utf-8').readlines()]

    seg = jieba.cut(x, cut_all=False)

    text_split_no = []

    for words in seg:
          if words not in stop_words:
             text_split_no.append(words)

    return ','.join(text_split_no)

df['tokenized']=df['rate'].apply(clean_the_stop)


def make_wordcloud(text):
    mask = np.array(Image.open('/Users/ypi/Desktop/light'))
    color_list = ['#FF0000', '#a41a1a']
    colormap = colors.ListedColormap(color_list)
    font = r"/System/Library/Fonts/STHeiti Light.ttc"
    wordcloud = word_cloud = WordCloud(
        font_path=font,
        background_color=None,
        mode="RGBA",
        prefer_horizontal=1,
        mask=mask,
        height=800,
        width=500,
        scale=10,
        colormap=colormap,  # 设置颜色
        margin=2
    ).generate(text)
    plt.figure(figsize=[25, 15])
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

make_wordcloud(str(df['tokenized']) )
