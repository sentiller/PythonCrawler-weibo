import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
import re
from datetime import datetime,timedelta
import PIL.Image as Image
import os
from random import randint
import random

dict = {
    '21-2-21': 0,
    '21-2-22': 0,
    '21-2-23': 0,
    '21-2-24': 0,
    '21-2-25': 0,
    '21-2-26': 0,
    '21-2-27': 0,
    '21-2-28': 0,
    '21-3-1': 0,
    '21-3-2': 0,
    '21-3-3': 0,
    '21-3-4': 0,
    '21-3-5': 0,
    '21-3-6': 0,
    '21-3-7': 0,
    '21-3-8': 0,
    '21-3-9': 0,
    '21-3-10': 0,
    '21-3-11': 0,
    '21-3-12': 0,
    '21-3-13': 0,
    '21-3-14': 0,
    '21-3-15': 0,
    '21-3-16': 0,
    '21-3-17': 0,
    '21-3-18': 0,
    '21-3-19': 0,
    '21-3-20': 0,
    '21-3-21': 0,
    '21-3-22': 0,
    '21-3-23': 0,
    '21-3-24': 0,
    '21-3-25': 0,
    '21-3-26': 0,
    '21-3-27': 0,
    '21-3-28': 0,
    '21-3-29': 0,
    '21-3-30': 0,
    '21-3-31': 0,
    'other': 0
}

def drop_duplicate(file):
    df = pd.read_csv(file, header=0)
    datalist = df.drop_duplicates()
    datalist.to_csv(file,index=False)
    print('完成去重')

def classify(file,file1,file2,file3,file4,dict):
    f1 = open(file1, 'a', encoding='utf-8')
    f2 = open(file2, 'a', encoding='utf-8')
    f3 = open(file3, 'a', encoding='utf-8')
    f4 = open(file4, 'a', encoding='utf-8')
    df = pd.read_csv(file, header=0)
    # df = df.sort_values(by='time')
    # df.to_csv(file, index=False)
    for index, row in df.iterrows():
        print(index)
        # print(row["text"], row["time"])
        time = row["time"]
        span = re.search(r'(.*?) (.*?)', time).span()
        date = time[span[0]: span[1]-1]
        date_1 = pd.to_datetime("20"+date)
        if(date_1>pd.to_datetime('2021-2-20') and date_1<pd.to_datetime('2021-3-3')):
            f1.write(row["text"]+"\n")
            dict[date]+=1
            # print("1")
        elif(date_1>pd.to_datetime('2021-3-2') and date_1<pd.to_datetime('2021-3-9')):
            f2.write(row["text"]+"\n")
            dict[date]+=1
            # print('2')
        elif(date_1>pd.to_datetime('2021-3-8') and date_1<pd.to_datetime('2021-4-1')):
            f3.write(row["text"]+"\n")
            dict[date]+=1
            # print('3')
        else:
            f4.write(row["text"]+"\n")
            dict['other']+=1
            # print("4")
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    print('完成按日期分类')

def replace_char(old_string,index1,index2):
    # old_string = str(old_string)
    # 新的字符串 = 老字符串[:要替换的索引位置] + 替换成的目标字符 + 老字符串[要替换的索引位置+1:]
    new_string = old_string[:index1] + old_string[index2:]
    return new_string

def islinetextEmpty(linetext):
    state = 0
    pos = [0, 0]
    while (True):
        if (re.search(r'#', linetext) == None):
            break
        for i in re.finditer(r'#', linetext):
            if (state == 0):
                state = 1
                pos[0] = i.span()[0]
            elif (state == 1):
                pos[1] = i.span()[1]
                linetext = replace_char(linetext, pos[0], pos[1])
                state = 0
                pos = [0, 0]
                break
    linetext = ''.join(re.findall(r'[\u4e00-\u9fa5]+', linetext))
    return len(linetext)

def randomchoose(file):
    df = pd.read_csv(file, header=0)
    if(df.shape[0]<=20):
        print('完成随机选取')
        return
    droplist = []
    for index, row in df.iterrows():
        if(islinetextEmpty(row[0]) == 0):
            droplist.append(index)
        # print(index)
        time = row["time"]
        span = re.search(r'(.*?) (.*?)', time).span()
        date = time[span[0]: span[1]-1]
        date_1 = pd.to_datetime("20"+date)
        if(date_1>pd.to_datetime('2021-2-20') and date_1<pd.to_datetime('2021-3-3')):
            # continue
            droplist.append(index)
            # f2.write(row["text"]+"\n")
            # dict[date]+=1
            # print("1")
        elif(date_1>pd.to_datetime('2021-3-2') and date_1<pd.to_datetime('2021-3-9')):
            # continue
            droplist.append(index)
            # f2.write(row["text"]+"\n")
            # dict[date]+=1
            # # print('2')
        elif(date_1>pd.to_datetime('2021-3-8') and date_1<pd.to_datetime('2021-4-1')):
            continue
            # droplist.append(index)
            # f3.write(row["text"]+"\n")
            # dict[date]+=1
            # # print('3')
        else:
            # continue
            droplist.append(index)
            # f4.write(row["text"]+"\n")
            # dict['other']+=1
            # # print("4")
    df = df.drop(droplist)
    maxnum = df.shape[0]-1
    print(maxnum)
    li = random.sample(range(1, maxnum), maxnum-20)
    li.sort()
    print(li)
    print(len(li))
    df = df.reset_index(drop=True)
    df = df.drop(li)
    print(df)
    print(df.shape)
    df.to_csv(file,index=False)
    print('完成随机选取')


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None,random_state=None):
    h = randint(160, 180)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)

def make_wordcloud(file):
    text = open(file, encoding='utf-8').read()
    wordlist = jieba.cut(text, cut_all=True)
    wordlistspacesplit = " ".join(wordlist)
    mystopwords=[]
    with open('stopwords.txt', 'r', encoding='utf=8') as f:
        for line in f:
            word = line[0:-1]
            mystopwords.append(word)
    f.close()
    mystopwords.extend(['拉拉','货'])
    mask = np.array(Image.open('alice_color.png'))
    mywordcloud = WordCloud(
        mask = mask,
        # height=2000,
        # width=3000,
        stopwords=mystopwords,
        collocations=False,
        background_color='#3c414f',
        # color_func=random_color_func,
        colormap='PuBu',
        mode='RGBA',
        prefer_horizontal=1,
        font_path="C:\\Windows\\Fonts\\STSONG.TTF",
        max_words=150,
        min_font_size=20
    ).generate(wordlistspacesplit)
    # image_colors = ImageColorGenerator(mask)

    # plt.imshow(mywordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.imshow(mywordcloud)
    plt.axis("off")
    plt.show()
    print('完成词云：'+file)
    text.close()

if __name__ == '__main__':
    commentfile = 'commentfile222_5.csv'
    commentfile1 = 'commentfile1.txt'  # 爆发2.21- 3.2
    commentfile2 = 'commentfile2.txt'  # 分化3.3-3.8
    commentfile3 = 'commentfile3.txt'  # 反转3.9- 3.31
    commentfile4 = 'commentfile4.txt'  # 之外4.1-今天
    drop_duplicate(commentfile)
    randomchoose(commentfile)
    # classify(commentfile,commentfile1,commentfile2,commentfile3,commentfile4,dict)
    # print('频度如下：')
    # print(dict)
    # # make_wordcloud(commentfile3)


