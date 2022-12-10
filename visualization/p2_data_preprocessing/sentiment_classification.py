import pandas as pd

csv_save_fname = '../p2_data_preprocessing/data/recipe_review_preprocessing_1207.csv'

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

recipe_main = pd.read_csv('../p2_data_preprocessing/data/recipe_review_preprocessing_1202.csv').iloc[:, 1:]

recipe_main['class'] = 0
for idx, row in recipe_main.iterrows():
    if int(row['별점']) >= 3:
        recipe_main.loc[idx, 'class'] = 1
    else:
        recipe_main.loc[idx, 'class'] = 0

# recipe_main['class'] = recipe_main['class'].astype('int64')  # class 값을 int 형으로
print(recipe_main)
recipe_main.to_csv(csv_save_fname, encoding='utf-8')
