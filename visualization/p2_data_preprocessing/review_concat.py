import pandas as pd

recipe_review1_path = '../p1_blog_analysis/data/recipe_review.csv'
recipe_review2_path = '../p1_blog_analysis/data/recipe_review_2.csv'
recipe_review3_path = '../p1_blog_analysis/data/recipe_review_3.csv'
recipe_review4_path = '../p1_blog_analysis/data/recipe_review_4.csv'
recipe_review5_path = '../p1_blog_analysis/data/recipe_review_5.csv'
save_fname = '../p1_blog_analysis/data/recipe_review_final.csv'

recipe_review1 = pd.read_csv(recipe_review1_path).iloc[:, 1:]
recipe_review2 = pd.read_csv(recipe_review2_path).iloc[:, 1:]
recipe_main = pd.concat([recipe_review1, recipe_review2], ignore_index=True).iloc[:, :]

del recipe_review1
del recipe_review2

recipe_review3 = pd.read_csv(recipe_review3_path).iloc[:, 1:]
recipe_main = pd.concat([recipe_main, recipe_review3], ignore_index=True).iloc[:, :]

del recipe_review3

recipe_review4 = pd.read_csv(recipe_review4_path).iloc[:, 1:]
recipe_main = pd.concat([recipe_main, recipe_review4], ignore_index=True).iloc[:, :]

del recipe_review4

recipe_review5 = pd.read_csv(recipe_review5_path).iloc[:, 1:]
recipe_main = pd.concat([recipe_main, recipe_review5], ignore_index=True).iloc[:, :]

del recipe_review5

print(recipe_main)
recipe_main.to_csv(save_fname, encoding='utf-8')
