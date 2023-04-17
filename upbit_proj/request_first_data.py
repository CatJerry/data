
import requests
import pandas as pd
from sqlalchemy import create_engine
from time import sleep
import pymysql
from mysql import connector

db_type = 'mysql'
host = '192.168.70.40'
port = '3305'
database = 'coin'
username = 'root'
password = '7610'

cnt = 100

# # MySQL 연결 설정
# conn = pymysql.connect(host=host, port=int(port), user=username, passwd=password, db=database)
# cursor = conn.cursor()
# 데이터베이스 연결 엔진 생성
engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')
def market_code():
    url = "https://api.upbit.com/v1/market/all?isDetails=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def minute_candle(code,count):
    url = f"https://api.upbit.com/v1/candles/minutes/1?market={code}&count={count}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def load_data():
    for i in range(len(name2)):
        code = name2['market'].iloc[i]
        print('실행중인 coin = ',code)
        coin_candle = minute_candle(code,cnt)
        df = pd.DataFrame(coin_candle)
        # DataFrame을 SQL 데이터베이스에 저장
        df.to_sql(name = f'coin_data', con=engine, if_exists='append', index=False)
        sleep(0.1)


# 이름 테이블 올리기
# KRW만 뽑았어용
name = pd.DataFrame(market_code())
name2 = name[name["market"].str[:3] == "KRW"]
# # DataFrame을 SQL 데이터베이스에 저장
name2.to_sql(name = f'coin_name', con=engine, if_exists='replace', index=True)

# 데이터 mysql에 적재
data = load_data()