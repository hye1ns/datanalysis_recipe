import re
import pandas as pd

from khaiii import KhaiiiApi
from pykospacing import Spacing
from hanspell import spell_checker

# columns 생략없이 보여주기
pd.set_option('display.max_columns', None)

csv_save_fname = '../p2_data_preprocessing/data/recipe_review_preprocessing_1202.csv'
excel_save_fname = '../p2_data_preprocessing/data/recipe_review_preprocessing_1202.xlsx'

spacing_rule_list = []  # spacing 잘못되는거 있음 적어넣기
significant_pos_list = ['NNG', 'NNP', 'NNB', 'NP', 'VV', 'VCP', 'VCN', 'VA']  # POS Tagging 중 필요한 것
stopwords = ['다지']  # 불용어

recipe_review_path = '../p1_blog_analysis/data/recipe_review_final.csv'
recipe_review = pd.read_csv(recipe_review_path).iloc[:, 1:]
recipe_review['내용_전처리'] = ''  # 전처리 한 list를 넣을 col 추가

for idx, row in recipe_review.iterrows():
    try:
        review_text = row['내용']

        if len(review_text) < 2:  # 리뷰 내용이 2글자 미만이면 pass
            continue

        # remove 특수문자
        review_text_removeSC = re.sub('[^A-Za-z0-9가-힣+]', ' ', review_text)

        # spacing review text
        spacing = Spacing()
        spaced_review_text = spacing(review_text_removeSC)

        # py-hanspell 맞춤법 교정
        spelled_spaced_review_text = spell_checker.check(spaced_review_text)
        checked_spelled_spaced_review_text = spelled_spaced_review_text.checked

        # for POS tagging (Khaiii)
        kapi = KhaiiiApi()

        title_sent = kapi.analyze(checked_spelled_spaced_review_text)

        significant_word_list = []
        for word in title_sent:
            word = str(word)
            word_str = word.split('\t')[1]
            word_list = re.split(' \+ |\. | ', word_str)
            for emt in word_list:
                word_emt = emt.split('/')
                if word_emt[1] in significant_pos_list:
                    if len(word_emt[0]) > 1:
                        if word_emt[0] not in stopwords:
                            significant_word_list.append(word_emt[0])
        significant_word_list_dup = list(set(significant_word_list))
        recipe_review.loc[idx, '내용_전처리'] = str(significant_word_list_dup)
    except Exception as e:
        print(e)
        print("row 내용:", row['내용'])
        print("checked_spelled_spaced_review_text:", checked_spelled_spaced_review_text)
        continue


# 저장
recipe_review.to_csv(csv_save_fname, encoding='utf-8')
recipe_review.to_excel(excel_save_fname, sheet_name='sheet1')
