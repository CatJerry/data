from sqlalchemy import create_engine
import pandas as pd
import requests

url = f'https://apis.data.go.kr/B553912/tk_sales/v1/yearly_sales?serviceKey=oTPgW%252FDH05NohBbfUUlPu%252BqzSlbx0bIV3%252B%252BPrAHe%252BMQGVitqflrS%252BDSewtiJYO4FKc3ZrOfNo55vtp%252B7i4D6Vg%253D%253D&page=20&perPage=40&returnType=JSON'
db_type = 'mysql'
host = 'localhost'
port = '3306'
database = 'srt'
username = 'root'
password = '7610'

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

# 데이터베이스 연결 엔진 생성
engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')

# DataFrame을 SQL 데이터베이스에 저장
df.to_sql(name = 'srt_table', con=engine, if_exists='replace', index=False)


