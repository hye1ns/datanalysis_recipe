import pandas as pd

pd.set_option('display.max_columns', None)

data_path = '../p1_blog_analysis/data/'
save_fname = '../p1_blog_analysis/data/recipe_main_final.csv'

recipe_main1 = pd.read_csv(data_path + 'recipe_main.csv')
recipe_main2 = pd.read_csv(data_path + 'recipe_main_2.csv')
recipe_main3 = pd.read_csv(data_path + 'recipe_main_3.csv')
recipe_main4 = pd.read_csv(data_path + 'recipe_main_4.csv')
recipe_main5 = pd.read_csv(data_path + 'recipe_main_5.csv')

recipe_main = pd.concat([recipe_main1, recipe_main2, recipe_main3, recipe_main4, recipe_main5], ignore_index=True).iloc[:, 1:]

# 메모리 효율을 위해
del recipe_main1
del recipe_main2
del recipe_main3
del recipe_main4
del recipe_main5

# recipe_main1.rename(columns={'Before':'After'})
for idx in range(len(recipe_main)):
    recipe_main.loc[idx, "셰프"] = recipe_main.loc[idx, "셰프"].strip()
print(recipe_main)
recipe_main.to_csv(save_fname, encoding='utf-8')
