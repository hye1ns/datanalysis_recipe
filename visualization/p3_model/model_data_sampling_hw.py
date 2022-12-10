import ast
import numpy as np
import pandas as pd

from gensim.models.word2vec import Word2Vec

# save_fname = '../p4_web/static/user1_data/yangchoding_recommend.csv'

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

# recipe_review = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1207.csv').iloc[:, 1:]
recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_main_preprocessing_1207.csv').iloc[:, 1:]
# review_w2v_model = Word2Vec.load('./save_model/review_w2v')
hashtag_w2v_model = Word2Vec.load('./save_model/hashtag_w2v')
# recipe_clustering = pd.read_csv('./data/recipe_main_clustering_221208.csv').iloc[:, 1:]

# [키워드 '캠핑장'과 유사한 단어 -> 마늘쫑새우볶음, 굴못먹는경우, 금체질, 과일김치, 티아민, 식초마늘장아찌, 저렴한, 꼬막볶음]
# [키워드 '인덕션요리'와 유사한 단어 -> 치킨무, 추석음식, 동그랑땡, 윤기나는, 부추무침, 동태전, 방울토마토, 이끌림밥상, 김치전]
# [키워드 '에어프라이어간식'과 유사한 단어 -> 저장식품, 멸치요리, 과일깍두기, 건강밥상, 파래, 원기회복, 견과류]
# [키워드 '편스토랑'과 유사한 단어 -> 마늘종볶음, 양파요리, 좋은, 류수영, 멸치요, 어묵, 가정식, 반찬레시피] # 채택
# camping_sim = hashtag_w2v_model.wv.most_similar('편스토랑')
# print(camping_sim)
count_df = pd.DataFrame()
for idx, row in recipe_main.iterrows():  # 해시태그 단어 빈도
    hashtag_str = str(row['해시태그_수정'])
    if hashtag_str == 'nan':
        continue
    hashtag_list = ast.literal_eval(hashtag_str)
    hashtag_list = set(hashtag_list)  # 중복 제거
    if '어묵' in hashtag_list:
        count_df = pd.concat([count_df, recipe_main[recipe_main['index'] == row['index']]], ignore_index=True)
        continue
print(count_df)
exit()

# [양초딩 님에게 추천할 셰프 : 요알남Mingstar, 혀니ㅋ]
recipe_main_chef = recipe_main[recipe_main['셰프'] == '혀니ㅋ']
count_df = pd.DataFrame(columns=['해시태그', 'count'])
for idx, row in recipe_main_chef.iterrows():  # 해시태그 단어 빈도
    hashtag_str = str(row['해시태그_수정'])
    if hashtag_str == 'nan':
        continue
    hashtag_list = ast.literal_eval(hashtag_str)
    hashtag_list = set(hashtag_list)  # 중복 제거
    for e in hashtag_list:
        if len(count_df[count_df['해시태그'] == e]) == 0:
            df4append = pd.DataFrame({'해시태그': [e], 'count': [1]})
            count_df = pd.concat([count_df, df4append], ignore_index=True)
        else:
            append_idx = count_df.index[(count_df['해시태그'] == e)]
            count_df.loc[append_idx, 'count'] += 1
print(count_df.sort_values(by=['count'], ascending=False)[:10])
exit()


# [양초딩 님이 높은 별점을 남긴 레시피와 유사한 레시피를 작성하는 셰프를 추천]
recipe_reivew_yang = recipe_review[recipe_review['닉네임'] == '양초딩']
recipe_reivew_yang = recipe_reivew_yang[recipe_reivew_yang['class'] == 1]  # 전부 1
yang_like = list(np.array(recipe_reivew_yang['index'].tolist()))
recommend = pd.DataFrame()
for yang_like_element in yang_like:
    recommend = pd.concat([recommend, recipe_clustering[recipe_clustering['index'] == yang_like_element]])
cluster_label = recommend.loc[:, ['index', 'cluster_label']].groupby(['cluster_label']).count().sort_values(by=['index'], ascending=False)
# print(cluster_label)  # cluster_label=269 그룹 count 5번으로 가장 높게 나옴
cluster_269_df = recipe_clustering[recipe_clustering['cluster_label'] == 269]
chef_count = cluster_269_df.loc[:, ['index', '셰프']].groupby(['셰프']).count().sort_values(by=['index'], ascending=False)
print(chef_count)
exit()
'''
요알남Mingstar        6
혀니ㅋ                2
딸기망고chsiiii        2
밥심은국력              2
츄츄맘                2
코코메이드              2
집밥레시피냉장고를부탁해       2
lee쉐프              2
핸디B                2
함박꽃                2
'''


# [양초딩 님이 작성하신 리뷰 중, '아이', '압력솥' 키워드로 w2v 유사도 확인]
# similar_list = review_w2v_model.wv.most_similar('압력솥')
# 압력솥: 여기저기, 단순, 통조림, 순간, 가을, 타이밍, 으깨지, 해용, 사오, 이해
cooker_df = pd.DataFrame()
for idx, row in recipe_review.iterrows():
    recipe_index = row['index']
    reivew_str = str(row['내용_전처리'])
    if reivew_str == 'nan':
        continue
    reivew_list = ast.literal_eval(reivew_str)
    if '압력솥' in reivew_list:
        cooker_df = pd.concat([cooker_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
    elif '여기저기' in reivew_list:
        cooker_df = pd.concat([cooker_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
    elif '통조림' in reivew_list:
        cooker_df = pd.concat([cooker_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
    elif '가을' in reivew_list:
        cooker_df = pd.concat([cooker_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
for idx, row in cooker_df.iterrows():  # 조회수 str to int
    views = row['조회수']
    views = views.replace(',', '')
    cooker_df.loc[idx, '조회수'] = int(views)
cooker_df = cooker_df.sort_values(by=['조회수'], ascending=False)
cooker_df = cooker_df.drop_duplicates(subset=['index'])  # index 같은거 drop dup
print(cooker_df[:20])
exit()


# similar_list = review_w2v_model.wv.most_similar('아이')
# 아이: 신랑, 아기, 식구, 아들, 딸내미, 초등학생, 남편, 아가, 딸아이, 덮밥
child_df = pd.DataFrame()
for idx, row in recipe_review.iterrows():
    recipe_index = row['index']
    reivew_str = str(row['내용_전처리'])
    if reivew_str == 'nan':
        continue
    reivew_list = ast.literal_eval(reivew_str)
    if '식구' in reivew_list:
        child_df = pd.concat([child_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
    elif '딸내미' in reivew_list:
        child_df = pd.concat([child_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
    elif '초등학생' in reivew_list:
        child_df = pd.concat([child_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
    elif '딸아이' in reivew_list:
        child_df = pd.concat([child_df, recipe_main[recipe_main['index'] == recipe_index]], ignore_index=True)
        continue
for idx, row in child_df.iterrows():  # 조회수 str to int
    views = row['조회수']
    views = views.replace(',', '')
    child_df.loc[idx, '조회수'] = int(views)
child_df = child_df.sort_values(by=['조회수'], ascending=False)
child_df = child_df.drop_duplicates(subset=['index'])  # index 같은거 drop dup
print(child_df[11:20])
exit()

# [양초딩 님이 자주 사용하는 '채소류', '볶음' 레시피 조회수 높은 것으로 4개 뽑기 -> recommend_class: 1]
recipe_veg_fry_df = recipe_main[recipe_main['재료별'] == '채소류']
recipe_veg_fry_df = recipe_veg_fry_df[recipe_veg_fry_df['방법별'] == '볶음']
for idx, row in recipe_veg_fry_df.iterrows():  # 조회수 str to int
    views = row['조회수']
    views = views.replace(',', '')
    recipe_veg_fry_df.loc[idx, '조회수'] = int(views)
recipe_veg_fry_df = recipe_veg_fry_df.sort_values(by=['조회수'], ascending=False)
print(recipe_veg_fry_df.head(10))
exit()

# [오기♥️ 님의 리뷰와 유사한 리뷰가 작성된 레시피]
ogi_review = []
recipe_reivew_ogi = recipe_review[recipe_review['닉네임'] == '양초딩']
for idx, row in recipe_reivew_ogi.iterrows():
    review_prep_str = str(row['내용_전처리'])
    if review_prep_str == 'nan':
        continue
    review_prep_list = ast.literal_eval(review_prep_str)
    ogi_review.append(review_prep_list)
ogi_review = sum(ogi_review, [])  # 이중 list 제거
print(len(ogi_review))
print(ogi_review)  # 아이, 압력솥
