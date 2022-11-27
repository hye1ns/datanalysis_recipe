import re
import time
import requests
from bs4 import BeautifulSoup

import pandas as pd

save_review_fname = './data/recipe_review.csv'
save_recipe_fname = './data/recipe_main.csv'

by_type = {'밑반찬': '63', '메인반찬': '56', '국/탕': '54', '찌개': '55', '디저트': '60', '면/만두': '53',
           '밥/죽/떡': '52', '퓨전': '61', '양념/잼/소스': '58', '양식': '65', '샐러드': '64', '스프': '68',
           '빵': '66', '과자': '69', '차/음료/술': '59'}  # cat4
by_situation = {'일상': '12', '초스피드': '18', '손님접대': '13', '술안주': '19', '다이어트': '21',
                '도시락': '15', '영양식': '43', '간식': '17', '야식': '45', '명절': '44'}  # cat2
by_ingredient = {'소고기': '70', '돼지고기': '71', '닭고기': '72', '육류': '23', '채소류': '28', '해물류': '24',
                 '달걀/유제품': '50', '쌀': '47', '밀가루': '32', '건어물류': '25', '버섯류': '31', '과일류': '48',
                 '곡류': '26'}  # cat3
by_method = {'볶음': '6', '끓이기': '1', '부침': '7', '조림': '36', '무침': '41', '비빔': '42',
             '찜': '8', '절임': '10', '튀김': '9', '삶기': '38', '굽기': '67', '회': '37'}  # cat1

recipe_idx = 1
list4df = []
list4rdf = []
try:
    for type_key, type_value in by_type.items():
        for situ_key, situ_value in by_situation.items():
            for ing_key, ing_value in by_ingredient.items():
                for method_key, method_value in by_method.items():
                    main_url = 'https://www.10000recipe.com/recipe/list.html?q=&query=&' \
                            'cat1={m}&cat2={s}&cat3={i}&cat4={t}' \
                            '&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='\
                            .format(m=method_value, s=situ_value, i=ing_value, t=type_value)
                    response = requests.get(main_url, headers={'User-Agent':'Mozilla/5.0'})
                    time.sleep(1)

                    if response.status_code == 200:  # 정상 연결시
                        soup = BeautifulSoup(response.text, 'html.parser')
                        page_len = len(soup.select('#contents_area_full > ul > nav > ul > li'))
                        for page in range(1, page_len+1):
                            if page != 1:
                                main_url = main_url + '&page=' + str(page)
                                response = requests.get(main_url, headers={'User-Agent':'Mozilla/5.0'})
                                soup = BeautifulSoup(response.text, 'html.parser')
                                time.sleep(2)
                            sources = soup.select('#contents_area_full > ul > ul > li > div.common_sp_thumb > a')
                            for source in sources:
                                recipe_url = 'https://www.10000recipe.com' + str(source).split('href')[1].split('"')[1]
                                response_r = requests.get(recipe_url, headers={'User-Agent':'Mozilla/5.0'})
                                soup_r = BeautifulSoup(response_r.text, 'html.parser')
                                time.sleep(1)

                                title = soup_r.select('#contents_area > div.view2_summary.st3 > h3')[0].text
                                views = soup_r.select('#contents_area > div.view2_pic > div.view_cate.st2 > div > span')[0].text
                                chef = soup_r.select('#contents_area > div.view2_pic > div.user_info2 > span')[0].text

                                try:
                                    servings = soup_r.select('#contents_area > div.view2_summary.st3 > div.view2_summary_info > span.view2_summary_info1')[0].text
                                    servings = re.sub(r'[^0-9]', '', servings)

                                    cooking_time = soup_r.select('#contents_area > div.view2_summary.st3 > div.view2_summary_info > span.view2_summary_info2')[0].text
                                    difficulty = soup_r.select('#contents_area > div.view2_summary.st3 > div.view2_summary_info > span.view2_summary_info3')[0].text
                                except:  # 작성이 안되어있는 경우
                                    servings = None
                                    cooking_time = None
                                    difficulty = None

                                try:
                                    ingredient_s = soup_r.select('#divConfirmedMaterialArea > ul')
                                    ingredient = []
                                    for ing in ingredient_s:
                                        for i in ing.find_all('li'):
                                            ingredient.append(i.text.split('\n')[0].strip())
                                except:
                                    continue

                                try:
                                    intro = soup_r.select('#recipeIntro')[0].text.strip()
                                except:
                                    intro = None

                                try:
                                    cooking_order = []
                                    process = 1
                                    while True:
                                        try:
                                            cooking_order_s = soup_r.select('#stepdescr'+str(process))[0].text.strip()
                                            cooking_order.append(cooking_order_s)
                                            process += 1
                                        except:
                                            break
                                except:
                                    continue

                                try:
                                    hashtag_s = soup_r.select('#contents_area > div.view_step > div.view_tag')[0].find_all('a')
                                    hashtag = []
                                    for ht in hashtag_s:
                                        hashtag.append(ht.text[1:])  # 1: 샵 제거
                                except:
                                    hashtag = None

                                list4df.append([recipe_idx, type_key, situ_key, ing_key, method_key, title, recipe_url, views, chef, servings, cooking_time, difficulty, ingredient, intro, cooking_order, hashtag])
                                recipe_idx += 1

                                review_s = soup_r.select('#contents_area > div.view_reply > div > div.media')
                                if len(review_s) == 0:
                                    continue
                                for rev in review_s:
                                    review = []
                                    review.append(recipe_idx)
                                    review.append(rev.find('b').text.strip())  # 닉네임
                                    review.append(rev.find('h4').text.strip().split(' ')[-2])  # 날짜
                                    review.append(rev.find('h4').text.strip().split(' ')[-1])  # 시간

                                    star = str(rev.find('span')).count('icon_star2_on')
                                    review.append(star)  # 별점

                                    context = rev.find('p').text.strip()
                                    review.append(context)  # 내용
                                    list4rdf.append(review)

                                add_review_s = soup_r.select('#moreViewReviewList > div.media')
                                if len(add_review_s) == 0:
                                    continue
                                for rev in add_review_s:
                                    review = []
                                    review.append(recipe_idx)
                                    review.append(rev.find('b').text.strip())  # 닉네임
                                    review.append(rev.find('h4').text.strip().split(' ')[-2])  # 날짜
                                    review.append(rev.find('h4').text.strip().split(' ')[-1])  # 시간

                                    star = str(rev.find('span')).count('icon_star2_on')
                                    review.append(star)  # 별점

                                    context = rev.find('p').text.strip()
                                    review.append(context)  # 내용
                                    list4rdf.append(review)

                                if recipe_idx % 200 == 0:
                                    recipe_df = pd.DataFrame(list4df,
                                                             columns=['index', '종류별', '상황별', '재료별', '방법별', '제목', 'url', '조회수', '셰프', '인분',
                                                                      '조리시간', '난이도', '재료', '인트로', '조리순서', '해시태그'])
                                    review_df = pd.DataFrame(list4rdf, columns=['index', '닉네임', '작성날짜', '작성시간', '별점', '내용'])

                                    recipe_df.to_csv(save_recipe_fname, encoding='utf-8')
                                    review_df.to_csv(save_review_fname, encoding='utf-8')
                                    del [[recipe_df, review_df]]

                                    print(type_key, situ_key, ing_key, method_key)
                                    print(recipe_idx, "번째까지 완료")
                                    print('페이지: ', page, '제목: ', title)
                                    print()
                    else:
                        print('정상 연결되지 않았습니다: ', response.status_code)
except Exception as e:
    print(e)
    print(recipe_url)
    exit()

recipe_df = pd.DataFrame(list4df, columns=['index', '종류별', '상황별', '재료별', '방법별', '제목', 'url', '조회수', '셰프', '인분', '조리시간', '난이도', '재료', '인트로', '조리순서', '해시태그'])
review_df = pd.DataFrame(list4rdf, columns=['index', '닉네임', '작성날짜', '작성시간', '별점', '내용'])

pd.set_option('display.max_columns', None)
print(recipe_df)
print(review_df)

recipe_df.to_csv(save_recipe_fname, encoding='utf-8')
review_df.to_csv(save_review_fname, encoding='utf-8')
