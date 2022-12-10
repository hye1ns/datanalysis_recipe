import ast
import pandas as pd

from gensim.models import Word2Vec

save_model = './save_model/review_w2v'
recipe_review = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1207.csv').iloc[:, 1:]

input_txt = []
for idx, row in recipe_review.iterrows():
    ini_str = str(row['내용_전처리'])
    if ini_str == 'nan':
        continue
    ini_list = ast.literal_eval(ini_str)  # str to list
    input_txt.append(ini_list)

# 모델학습(word2vec 기본 파라미터)
model = Word2Vec(sentences=input_txt, vector_size=100, window=5, min_count=1, workers=4, sg=1)

# 모델확인
print(model.wv.vectors.shape)  # 메트릭스 크기
print(model.wv.most_similar("감자"))  # 명사
print(model.wv.most_similar("맛있"))  # 형용사

# 모델저장
model.save(save_model)
