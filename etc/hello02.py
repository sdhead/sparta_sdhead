from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# doc = {'name':'bob','age':24}

# db.user.insert_one(doc)

# user = db.user.find_one({'name':'bob'},{'_id':0})
# print(user)

# db.user.insert_one({'name':'bobby','age':21})
# db.user.insert_one({'name':'kay','age':27})
# db.user.insert_one({'name':'john','age':30})

# MongoDB에서 데이터 모두 보기
# all_user = list(db.user.find({},{'_id':0}))

# for user in all_user:
#     print(user)

# 예시 - 오타가 많으니 이 줄을 복사해서 씁시다!
# db.user.update_one({'name':'bobby'},{'$set':{'age':19}})

db.user.delete_one({'name':'bobby'})
