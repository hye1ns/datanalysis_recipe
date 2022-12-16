import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)
# 맥 한글깨짐 방지
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

recipe_review = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1207.csv').iloc[:, 1:]
recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_main_preprocessing_1207.csv').iloc[:, 1:]

print(recipe_review)
exit()


# [오기♥️ 님의 사용한 재료, 방법]
ing_df = pd.DataFrame(columns=['재료', 'count'])
method_df = pd.DataFrame(columns=['방법', 'count'])
recipe_reivew_ogi = recipe_review[recipe_review['닉네임'] == '양초딩']
for idx, row in recipe_reivew_ogi.iterrows():
    rec_index = int(row['index'])
    ing = recipe_main.loc[rec_index, '재료별']
    method = recipe_main.loc[rec_index, '방법별']
    if len(ing_df[ing_df['재료'] == ing]) == 0:
        ing_df4append = pd.DataFrame({'재료': [ing], 'count': [1]})
        ing_df = pd.concat([ing_df, ing_df4append], ignore_index=True)
    else:
        append_idx = ing_df.index[(ing_df['재료'] == ing)]
        ing_df.loc[append_idx, 'count'] += 1
    if len(method_df[method_df['방법'] == method]) == 0:
        method_df4append = pd.DataFrame({'방법': [method], 'count': [1]})
        method_df = pd.concat([method_df, method_df4append], ignore_index=True)
    else:
        append_idx = method_df.index[(method_df['방법'] == method)]
        method_df.loc[append_idx, 'count'] += 1
print(ing_df)
print()
print(method_df)
plt.bar(ing_df['재료'], ing_df['count'])
plt.show()
plt.bar(method_df['방법'], method_df['count'])
plt.show()
exit()

# [가장 많은 리뷰를 작성한 닉네임]
recipe_review_nickname = recipe_review.loc[:, ['index', '닉네임']].groupby(['닉네임']).count().sort_values(by=['index'], ascending=False)
print(recipe_review_nickname)
exit()
'''
맛있냠            68
하늘의그리움         76
양초딩            91
오기♥️          104
'''

# [class 개수 확인]
recipe_review_class = recipe_review.loc[:, ['index', 'class']].groupby(['class']).count()
print(recipe_review_class)
exit()
plt.bar(recipe_review_class.index, recipe_review_class['index'])
plt.show()
exit()

recipe_review_score = recipe_review.loc[:, ['index', '별점']].groupby(['별점']).count()
plt.bar(recipe_review_score.index, recipe_review_score['index'])
plt.show()
exit()

recipe_main_type_count = pd.DataFrame(recipe_review.iloc[:, 1:5].groupby(['재료별', '방법별']).count().iloc[:, 1]).T
