from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# 한 개 찾기 - 예시
# (1) 영화제목 '매트릭스'의 평점을 가져오기

# user = db.movies.find_one({'movie':'매트릭스'})
# print('매트릭스의 평점은 : ' + user['point'])


# (2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
# user = db.movies.find_one({'movie':'매트릭스'})
# where_point = user['point']

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_movie = list(db.movies.find({'point':where_point},{'_id':False}))

# for movie in same_movie:
#     print(movie['movie'])


# (3) '매트릭스'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
user = db.movies.find_one({'movie':'매트릭스'})
where_point = user['point']

# 바꾸기 - 예시
# db.movies.update_one({'name':'bobby'},{'$set':{'age':19}})
db.movies.update_many({'point':where_point},{'$set':{'point':0}})



