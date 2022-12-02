import pandas as pd

from matplotlib import rc
import matplotlib.pyplot as plt

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

# 한글깨짐_for_mac
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

recipe_main_path = '../p1_blog_analysis/data/recipe_main_final.csv'
recipe_main = pd.read_csv(recipe_main_path).iloc[:, 1:]

import ast
hashtag_list = []
for hashtag_word in recipe_main.loc[:, "해시태그"]:
    hashtag_word = ast.literal_eval(hashtag_word)
    print(type(hashtag_word))
    exit()
    hashtag_list.append(hashtag_word)
hashtag_list = set(sum(hashtag_list, []))
print(hashtag_list)
exit()



# # plt 1 -> 상위 5명: 밥차리라, 노란장미, 만개의레시피, 좋아좋아3, 시크제이맘
# recipe_main_count = pd.DataFrame(recipe_main.iloc[:, 1:].groupby('셰프').count().iloc[:, 1])
# recipe_main_count.columns = ['count']
# recipe_main_count = recipe_main_count.sort_values('count', ascending=False)
#
# plt.bar(recipe_main_count.index, recipe_main_count['count'])
# plt.show()


# # plt 2 - 표 형태로 저장하면 좋을 듯
# recipe_main_type_count = pd.DataFrame(recipe_main.iloc[:, 1:5].groupby(['재료별', '방법별']).count().iloc[:, 1]).T
# print(recipe_main_type_count)


# # plt 3 -> 볶음 1위
# recipe_main_top1_by_method = recipe_main[recipe_main["셰프"] == "밥차리라"].groupby(['방법별']).count().iloc[:, 1]
# recipe_main_top1_by_method.columns = ['count']
#
# plt.bar(recipe_main_top1_by_method.index, recipe_main_top1_by_method)
# plt.show()


# # plt 4 -> 채소류 1위
# recipe_main_top1_by_ingredient = recipe_main[recipe_main["셰프"] == "밥차리라"].groupby(['재료별']).count().iloc[:, 1]
# recipe_main_top1_by_ingredient.columns = ['count']
#
# plt.bar(recipe_main_top1_by_ingredient.index, recipe_main_top1_by_ingredient)
# plt.show()

