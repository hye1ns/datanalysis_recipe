import ast
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

save_fname = './data/recipe_main_clustering_221208.csv'

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_main_preprocessing_1207.csv').iloc[:, 1:]
# recipe_main['인분'] = recipe_main['인분'].astype('int64')

for idx, row in recipe_main.iterrows():
    # 조회수 str to int
    views = row['조회수']
    views = views.replace(',', '')
    recipe_main.loc[idx, '조회수'] = int(views)

    # 인분 NaN 값 0으로 바꾸기
    try:
        recipe_main.loc[idx, '인분'] = int(row['인분'])
    except:
        recipe_main.loc[idx, '인분'] = 0


    # 조리시간 분 단위로 수정
    cooking_time = row['조리시간']
    if cooking_time == '90분 이내':
        recipe_main.loc[idx, '조리시간'] = 90
    elif cooking_time == '5분 이내':
        recipe_main.loc[idx, '조리시간'] = 5
    elif cooking_time == '2시간 이상':
        recipe_main.loc[idx, '조리시간'] = 150
    elif cooking_time == '60분 이내':
        recipe_main.loc[idx, '조리시간'] = 60
    elif cooking_time == '10분 이내':
        recipe_main.loc[idx, '조리시간'] = 10
    elif cooking_time == '15분 이내':
        recipe_main.loc[idx, '조리시간'] = 15
    elif cooking_time == '30분 이내':
        recipe_main.loc[idx, '조리시간'] = 30
    elif cooking_time == '20분 이내':
        recipe_main.loc[idx, '조리시간'] = 20
    elif cooking_time == '120분 이내':
        recipe_main.loc[idx, '조리시간'] = 120
    else:
        recipe_main.loc[idx, '조리시간'] = 0

    # 난이도 서열척도로 변경
    hard = row['난이도']
    if hard == '아무나':
        recipe_main.loc[idx, '난이도'] = 1
    elif hard == '초급':
        recipe_main.loc[idx, '난이도'] = 2
    elif hard == '중급':
        recipe_main.loc[idx, '난이도'] = 3
    elif hard == '고급':
        recipe_main.loc[idx, '난이도'] = 4
    elif hard == '신의경지':
        recipe_main.loc[idx, '난이도'] = 5
    else:
        recipe_main.loc[idx, '난이도'] = 0


recipe_main_dummy = pd.get_dummies(recipe_main, columns=['재료별', '방법별'])

columns2use = ["재료별_건어물류", '재료별_곡류', '재료별_과일류', '재료별_달걀/유제품', '재료별_닭고기', '재료별_돼지고기',
               '재료별_밀가루', '재료별_버섯류', '재료별_소고기', '재료별_쌀', '재료별_육류', '재료별_채소류', '재료별_해물류',
               '방법별_굽기', '방법별_끓이기', '방법별_무침', '방법별_볶음', '방법별_부침', '방법별_비빔', '방법별_삶기',
               '방법별_절임', '방법별_조림', '방법별_찜', '방법별_튀김', '방법별_회',
               '조회수', '인분', '조리시간', '난이도']

# 정규화
scaler = StandardScaler()
recipe_main_dummy['조회수'] = scaler.fit_transform(recipe_main_dummy[['조회수']])
recipe_main_dummy['인분'] = scaler.fit_transform(recipe_main_dummy[['인분']])
recipe_main_dummy['조리시간'] = scaler.fit_transform(recipe_main_dummy[['조리시간']])
recipe_main_dummy['난이도'] = scaler.fit_transform(recipe_main_dummy[['난이도']])

estimator = KMeans(n_clusters=500).fit(recipe_main_dummy[columns2use])
y = estimator.predict(recipe_main_dummy[columns2use])
recipe_main_dummy['cluster_label'] = pd.Series(y)

print(recipe_main_dummy)
recipe_main_dummy.to_csv(save_fname, encoding='utf-8')  # save
exit()


list4ing = []
for idx, row in recipe_main.iterrows():
    ingredient_str = row['재료']
    ingredient_list = ast.literal_eval(ingredient_str)
    list4ing.append(ingredient_list)
list4ing = sum(list4ing, [])  # 이중 list 제거
print(set(list4ing))
exit()

print(len(recipe_main[recipe_main['조리시간']=='nan']))
