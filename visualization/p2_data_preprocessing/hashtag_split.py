import ast
import pandas as pd

save_fname = './data/recipe_main_preprocessing_1207.csv'

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

recipe_main = pd.read_csv('../p1_blog_analysis/data/recipe_main_final.csv').iloc[:, 1:]
recipe_main['해시태그'] = recipe_main['해시태그'].astype(str)  # 해시태그 값을 str 형으로

idx = 0
recipe_main['해시태그_수정'] = ''
for hashtag_str in recipe_main.loc[:, '해시태그']:  # dataframe 돌기
    new_hashtag_list = []
    if hashtag_str == 'nan':  # 해시태그 값이 없다면 pass 시키기
        idx += 1
        continue
    hashtag_list = ast.literal_eval(hashtag_str)  # str to list
    for hash_word in hashtag_list:
        hash_word_split = hash_word.split(' ')  # 띄어쓰기로 split (type: list)
        for hash_word2append in hash_word_split:
            hash_word2append = hash_word2append.replace('#', '')  # #태그가 있다면 제거
            new_hashtag_list.append(hash_word2append)
    recipe_main.loc[idx, '해시태그_수정'] = str(new_hashtag_list)  # list 형태로 dataframe에 저장이 안되기 때문에 str 형태로 저장
    idx += 1

print(recipe_main)
recipe_main.to_csv(save_fname, encoding='utf-8')  # save
