# 读取9.py生成的评论txt,并且生成词云
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

font_path = '/Library/Fonts/Arial Unicode.ttf'  # 字体的路径如果是windows系统就写你的字体路径就可以
# 打开文本
text = open('comments.txt','r').read()  # 读取评论保存页面

# 中文分词  通过jieba分词
text = ' '.join(jieba.cut(text))

# 生成对象
mask = np.array(Image.open('res/china.jpg'))
wc = WordCloud(mask=mask, font_path=font_path,mode='RGBA',background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存词云
wc.to_file('wordcloud.png')