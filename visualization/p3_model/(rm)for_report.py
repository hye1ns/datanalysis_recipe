import pandas as pd
from matplotlib import rc
import seaborn as sns
import matplotlib.pyplot as plt

from gensim.models.word2vec import Word2Vec

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)
# 맥 한글깨짐 방지
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

recipe_review = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1207.csv').iloc[:, 1:]
# recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_main_preprocessing_1207.csv').iloc[:, 1:]
# recipe_clustering = pd.read_csv('./data/recipe_main_clustering_221208.csv').iloc[:, 1:]
# review_w2v_model = Word2Vec.load('./save_model/review_w2v')
# hashtag_w2v_model = Word2Vec.load('./save_model/hashtag_w2v')

recipe_review_nickname = recipe_review.loc[:, ['index', '닉네임']].groupby(['닉네임']).count().sort_values(by=['index'], ascending=False)[:]
print(len(recipe_review_nickname))
exit()
plt.bar(recipe_review_nickname.index, recipe_review_nickname['index'])
plt.show()
exit()

# camping_sim = hashtag_w2v_model.wv.most_similar('보양식품')
# print(camping_sim)
# exit()

recipe_main_group = pd.concat([recipe_main, recipe_clustering['cluster_label']], axis=1)
recipe_main_group['인분'] = recipe_main_group['인분'].astype(float)
recipe_main_group['인분'] = recipe_main_group['인분'].astype(str)

for idx, row in recipe_main_group.iterrows():
    # 조회수 str to int
    views = row['조회수']
    views = views.replace(',', '')
    recipe_main_group.loc[idx, '조회수'] = views
recipe_main_group['조회수'] = recipe_main_group['조회수'].astype('int64')

recipe_269_a = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['index', '재료별']].groupby(['재료별']).count().sort_values(by=['index'], ascending=False)
recipe_269_b = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['index', '방법별']].groupby(['방법별']).count().sort_values(by=['index'], ascending=False)
recipe_269_c = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['index', '조리시간']].groupby(['조리시간']).count().sort_values(by=['index'], ascending=False)
recipe_269_d = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['index', '인분']].groupby(['인분']).count().sort_values(by=['index'], ascending=False)
recipe_269_e = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['index', '난이도']].groupby(['난이도']).count().sort_values(by=['index'], ascending=False)
recipe_review_nickname = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['조회수']]

fig, ax = plt.subplots(ncols=3, nrows=2)

plt.subplot(231)
plt.bar(recipe_269_a.index, recipe_269_a['index'], width=0.2)
plt.ylabel('재료별')

plt.subplot(232)
plt.bar(recipe_269_b.index, recipe_269_b['index'])
plt.ylabel('방법별')

plt.subplot(233)
plt.bar(recipe_269_c.index, recipe_269_c['index'])
plt.ylabel('조리시간')

plt.subplot(234)
plt.bar(recipe_269_d.index, recipe_269_d['index'])
plt.ylabel('인분')

plt.subplot(235)
plt.bar(recipe_269_e.index, recipe_269_e['index'])
plt.ylabel('난이도')
# axes[1][2].boxplot(recipe_269_c.index, recipe_269_c['index'])
# sns.barplot(data=recipe_269_a, y='index', ax=ax[0, 0])
# sns.barplot(data=recipe_269_b, y='index', ax=ax[0, 1])
# sns.barplot(data=recipe_269_c, y='index', ax=ax[0, 2])
# sns.barplot(data=recipe_269_d, y='index', ax=ax[1, 0])
# sns.barplot(data=recipe_269_e, y='index', ax=ax[1, 1])
plt.subplot(236)
sns.boxplot(y='조회수', palette="Set3", width=0.3, data=recipe_review_nickname)
plt.show()
exit()

recipe_review_nickname = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['index', '조회수']].groupby(['조회수']).count().sort_values(by=['index'], ascending=False)
# recipe_review_nickname = recipe_main_group[recipe_main_group['cluster_label'] == 269].loc[:, ['조회수']]
# print(recipe_review_nickname.describe())
# plt.figure(figsize=(5, 3))
sns.boxplot(y='조회수', palette="Set3", width=0.3, data=recipe_review_nickname)
# plt.boxplot([recipe_review_nickname['조회수']])
plt.title('269번 그룹의 조회수')

plt.show()
# plt.bar(recipe_review_nickname.index, recipe_review_nickname['index'])
# plt.show()