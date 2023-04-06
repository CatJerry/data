from mysql import connector
import requests

HOST = '192.168.90.119'
PORT = '3306'
USER = 'myname'
PASSWORD = '1234'
DATABASE = 'mydb'

def conn_db():
  conn = connector.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, database=DATABASE)
  return conn
lotto_numbers = {}

def lotto_api():
    for i in range(1,1060):
        url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}'
        response = requests.get(url)
        lotto_numbers[i] = response.json()
    return lotto_numbers

# 입력 함수
def insert_data():
  # db연결
  connection_result = conn_db()
  cursor = connection_result.cursor()
  lotto_api()
  # query문 실행
  for i in range(1,1060):
    num1 = lotto_numbers[i]["drwtNo1"]
    num2 = lotto_numbers[i]["drwtNo2"]
    num3 = lotto_numbers[i]["drwtNo3"]
    num4 = lotto_numbers[i]["drwtNo4"]
    num5 = lotto_numbers[i]["drwtNo5"]
    num6 = lotto_numbers[i]["drwtNo6"]
    bonus = lotto_numbers[i]["bnusNo"]
    sql = f"INSERT into lotto_number_lsy (roundNum, num1,num2, num3,num4, num5, num6, bonus) values({i}, {num1}, {num2}, {num3}, {num4}, {num5}, {num6}, {bonus});"
    cursor.execute(sql)
    connection_result.commit()
  # db연결해제
  connection_result.close()
  print("잘 저장되었습니다")
  return

insert_data()