from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def write_order():
    order_name = request.form['name_give'] #주문자 이름
    order_cnt = request.form['cnt_give'] #주문수량
    order_address = request.form['address_give'] #주문자 주소
    order_tel = request.form['tel_give'] #주문자 전화번호

    doc = {
        'name' : order_name,
        'cnt' : order_cnt,
        'address' : order_address,
        'tel' : order_tel
    }

    db.tire_order.insert_one(doc)

    return jsonify({'result':'success', 'msg': '주문이완료되었습니다-POST'})


@app.route('/order_list', methods=['GET'])
def read_orderList():  
    order_view = list(db.tire_order.find({},{'_id':0}))
    
    return jsonify({'result':'success', 'all_order': order_view})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)