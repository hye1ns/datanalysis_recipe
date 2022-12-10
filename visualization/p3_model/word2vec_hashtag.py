import ast
import pandas as pd

from gensim.models import Word2Vec

save_model = './save_model/hashtag_w2v'
recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_main_preprocessing_1207.csv').iloc[:, 1:]

input_txt = []
for idx, row in recipe_main.iterrows():
    hashtag_str = str(row['해시태그_수정'])
    if hashtag_str == 'nan':
        continue
    hashtag_list = ast.literal_eval(hashtag_str)  # str to list
    input_txt.append(hashtag_list)

# 모델학습(word2vec 기본 파라미터)
model = Word2Vec(sentences=input_txt, vector_size=100, window=5, min_count=1, workers=4, sg=1)

# 모델확인
print(model.wv.vectors.shape)  # 메트릭스 크기
print(model.wv.most_similar("캠핑장"))
print(model.wv.most_similar("초간단"))

# 모델저장
model.save(save_model)
