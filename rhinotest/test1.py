import rhinoMorph

import matplotlib
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

def read_data(filename, encoding='cp949', start=1):
    with open(filename, 'r', encoding=encoding) as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[start:]
    return data

def write_data(data, filename, encoding='cp949'):
    with open(filename, 'w', encoding=encoding) as f:
        f.write(data)

data = read_data('ratings_test.txt' , encoding='utf-8')
data = data[:500]
# print(data[:3])
# print(len(data))

# len_data = []
# for d in data:
#     len_data.append(len(d[1].split()))

# print("첫번째 문장의 어절 길이:", len_data[0])

# import numpy as np

# print('텍스트 최대 길이: {}'.format(np.max(len_data)))
# print('텍스트 최소 길이: {}'.format(np.min(len_data)))
# print('텍스트 평균 길이: {:.2f}'.format(np.mean(len_data)))
# print('텍스트 길이 표준편차: {:.2f}'.format(np.std(len_data)))
# print('텍스트 중간 길이: {}'.format(np.median(len_data)))

# print('제 1 사분위 텍스트 길이: {}'.format(np.percentile(len_data, 25)))
# print('제 3 사분위 텍스트 길이: {}'.format(np.percentile(len_data, 75)))

# plt.figure(figsize=(8, 5))
# plt.boxplot([len_data], labels=['어절'], showmeans=True)
# plt.show()

# rn = rhinoMorph.startRhino()

# morphed_data = ''
# for data_each in data:
#     morphed_data_each = rhinoMorph.onlyMorph_list(rn, data_each[1], pos=['NNG', 'NNP', 'VV', 'VA', 'XR', 'IC', 'MM', 'MAG', 'MAJ'], eomi= True)
#     # print(morphed_data_each)
#     joined_data_each = ' '.join(morphed_data_each) # 문자열을 하나로 연결
#     if joined_data_each: # 내용이 있는 경우만 저장하게 함
#         morphed_data += data_each[0]+"\t"+joined_data_each+"\t"+data_each[2]+"\n"

# 형태소 분석된 파일 저장
# write_data(morphed_data, 'ratings_morphed.txt', encoding='utf-8')

data = read_data('ratings_morphed.txt', encoding='utf-8', start=0)

data_text = [line[1] for line in data]
# print(data_text)
mergedText = ' '.join(data_text)
mergedTextList = mergedText.split(' ')
# print(mergedTextList[:10])
# print(len(mergedTextList))

# Counter
from collections import Counter

# 불용어
stopwords_ko = ["하다", "있다", "되다", "그", "않다", "없다", "나", "말", "사람", "이", "보다", "한", "때", "년", "같다", "대하다", "일", "이", "생각", "위하다", "때문", "그것", "그러나", "가다", "받다", "그렇다", "알다", "사회", "더", "그녀", "문제", "오다", "그리고", "크다", "속"]

mergedTextList_no_stopwords = [word for word in mergedTextList if not word in stopwords_ko]
# print(mergedTextList)
# print('--------------------------------------------')
# print(mergedTextList_no_stopwords)

# print('불용어 제거 전 길이:', len(mergedTextList))
# print('불용어 제거 후 길이:', len(mergedTextList_no_stopwords))

wordInfo = Counter(mergedTextList_no_stopwords)
print('wordInfo:', wordInfo)

linedata = ' '.join(mergedTextList_no_stopwords)

# print('--------------------------------------------')
# print(linedata)

from wordcloud import WordCloud
cloud = WordCloud(font_path=font_path, width=800, height=600).generate(linedata)
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()