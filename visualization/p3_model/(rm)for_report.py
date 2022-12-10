import ast
import numpy as np
import pandas as pd

from gensim.models.word2vec import Word2Vec

# save_fname = '../p4_web/static/user1_data/yangchoding_recommend.csv'

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_main_preprocessing_1207.csv').iloc[:, 1:]
# hashtag_w2v_model = Word2Vec.load('./save_model/hashtag_w2v')
# review_w2v_model = Word2Vec.load('./save_model/review_w2v')

recipe_review = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1207.csv').iloc[:, 1:]
recipe_clustering = pd.read_csv('./data/recipe_main_clustering_221208.csv').iloc[:, 1:]

recipe_main = recipe_main.concat([recipe_main, recipe_clustering], axis=1)
print(recipe_main)
exit()

recipe_reivew_yang = recipe_review[recipe_review['닉네임'] == '양초딩']
recipe_reivew_yang = recipe_reivew_yang[recipe_reivew_yang['class'] == 1]  # 전부 1
yang_like = list(np.array(recipe_reivew_yang['index'].tolist()))
recommend = pd.DataFrame()
for yang_like_element in yang_like:
    recommend = pd.concat([recommend, recipe_clustering[recipe_clustering['index'] == yang_like_element]])
cluster_label = recommend.loc[:, ['index', 'cluster_label']].groupby(['cluster_label']).count().sort_values(by=['index'], ascending=False)
# print(recommend)
# print(cluster_label)  # cluster_label=269 그룹 count 5번으로 가장 높게 나옴
cluster_269_df = recipe_clustering[recipe_clustering['cluster_label'] == 269]
print(cluster_269_df)
exit()
chef_count = cluster_269_df.loc[:, ['index', '셰프']].groupby(['셰프']).count().sort_values(by=['index'], ascending=False)
print(chef_count)