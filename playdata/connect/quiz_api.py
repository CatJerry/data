from flask import Flask, jsonify, request
from sql_test import select,database_connect
import random
app = Flask(__name__)
config_dict = {
    'host' : '192.168.90.119',
    'port' : '3306',
    'user' : 'myname',
    'database' : 'mydb',
    'password' : '1234'
}
# GET 요청을 처리하는 예제API
@app.route('/hello',methods=["GET"])
def hello():
    return jsonify({'message': 'Hello World!'})


database = database_connect(config_dict['host'], config_dict['user'], config_dict['password'], config_dict['database'], config_dict['port'])
n = select()
length = len(n)
num = random.randint(0,length)
@app.route('/get_question',methods=['GET'])
# n = select()
def get_question():
    #DB접속
    #문제를 조회해서
    #dictionary형태로{문제:답}
    #jsonify(여기다가 넣기)로 리턴
    question = n[num][0]
    answer = n[num][1]
    return jsonify({'question':"answer"})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)

