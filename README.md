# datanalysis_recipe

## 만개의 레시피 크롤링
### recipe_main.csv 데이터 타입
columns 개수: 16개

index : (int) 요리 레시피 고유번호 \
종류별 : (str) 밑반찬, 메인반찬, 국/탕, 찌개, 디저트, 면/만두, 밥/죽/떡, 퓨전, 양념/잼/소스, 양식, 샐러드, 스프,
           빵, 과자, 차/음료/술 중 하나 \
상황별 : (str) \
재료별 : (str) \
방법별 : (str) \
제목 : (str) \
url : (str) 레시피 작성된 주소 \
조회수 : (str) \
셰프 : (str) \
인분 : (int) ex. 3 : 3인분 \
조리시간 : (str) \
난이도 : (str) \
재료 : (list) \
인트로 : (str) 요리 알려주기 전에 작성된 문구 \
조리순서 : (list) 조리 순서대로 \
해시태그 : (list) 


### recipe_review.csv 데이터 타입
columns 개수: 6개

index : (int) 요리 레시피 고유번호 \
닉네임 : (str) 요리후기 작성한 닉네임 \
작성날짜 : (str) \
작성시간 : (str) \
별점 : (int) \
내용 : (str) 후기