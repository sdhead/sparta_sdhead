from flask import Flask,render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
   # return 'This is Home!'
   return render_template('index.html')


@app.route('/read_info', methods=['GET'])
def listing():
   # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
   # 2. articles라는 키 값으로 영화정보 내려주기
   all_memorys = list(db.familymemory.find({},{'_id':0}))
   #  return jsonify({'result':'success', 'all_memory':all_memorys}
   return jsonify({'result':'success', 'all_memory':all_memorys})
   



## API 역할을 하는 부분
@app.route('/save_info', methods=['POST'])
def saving_data():
   # 1. 클라이언트로부터 데이터를 받기
   # 2. mongoDB에 데이터 넣기

   write_name = request.form['in_writer']  # 작성자
   write_time = request.form['in_date']  # 작성일
   write_filePath = request.form['in_filePath']  # 사진경로
   write_urlLink = request.form['in_urlPath']  # URL
   write_memo = request.form['in_memo']  # 내용

   doc = {
      'writer' : write_name,
      'date' : write_time,
      'picture_path' : write_filePath,
      'url' : write_urlLink,
      'memo' : write_memo
   }

   db.familymemory.insert_one(doc)

   return jsonify({'result': 'success', 'msg':'POST-저장이 완료되었습니다.!'})

   


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)