import requests
import pandas as pd
from sqlalchemy import create_engine
from time import sleep


db_type = 'mysql'
host = '0.0.0.0'
port = '3306'
database = 'coin'
username = 'root'
password = '7610'

def market_code():
    url = "https://api.upbit.com/v1/market/all?isDetails=false"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def minute_candle(code):
    url = f"https://api.upbit.com/v1/candles/minutes/5?market={code}&count=100"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def now_traded_price():
    url = "https://api.upbit.com/v1/trades/ticks?count=1"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def now_price():
    url = "https://api.upbit.com/v1/ticker"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def now_call_price():
    url = "https://api.upbit.com/v1/orderbook"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

name = pd.DataFrame(market_code())
name2 = name[name["market"].str[:3] == "KRW"]
print(name2)
# KRW만 뽑았어용
# name_list = name2['market']

# 데이터베이스 연결 엔진 생성
engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')

for i in range(len(name2)):

    code = name2['market'].iloc[i]
    print('실행중인 coin = ',code)
    coin_candle = minute_candle(code)
    df = pd.DataFrame(coin_candle)
    # DataFrame을 SQL 데이터베이스에 저장
    df.to_sql(name = f'{code}', con=engine, if_exists='replace', index=False)
    sleep(1)

