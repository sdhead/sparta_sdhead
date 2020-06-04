# Flask 프레임워크를 사용하겠다.
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})   


@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})   


# @app.route('/mypage')
# def mypage():
#    return 'This is mypage!'   

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True) # Flask 프레임워크를(서버) 실행하겠다. 종료할때는 CTRL+C