# [LSTM을 쓰지 않아도 ㄱㅊ다는걸 앎 아까워서..]

import ast
import pandas as pd

recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1202.csv').iloc[:, 1:]

'''
리뷰 데이터의 별점이 3점 이상이면 긍정, 3점 미만이면 부정으로 classification -> class: 0(부정), 1(긍정)
'''

# data setting for model input
dict_idx = 0
dict4mapping = {}
X = []
y = []
# word -> num
for idx, row in recipe_main.iterrows():
    review_str = row['내용_전처리']
    review_list = ast.literal_eval(review_str)

    list4appendX = []
    for element in review_list:
        try:
            dict4mapping[element]
        except:
            dict4mapping[element] = dict_idx
            dict_idx += 1
        list4appendX.append(dict4mapping[element])
    X.append(list4appendX)

    if int(row['별점']) >= 3:
        y.append(1)
    else:
        y.append(0)
