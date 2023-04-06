from sqlalchemy import create_engine
import pandas as pd
# DataFrame 생성
df = pd.read_csv('api_apply/criminal.csv',encoding='cp949')
# 데이터베이스 연결 정보
db_type = 'mysql'
host = '192.168.70.40'
port = '3305'
database = 'mydatabase'
username = 'root'
password = '7610'

# 데이터베이스 연결 엔진 생성
engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')

# DataFrame을 SQL 데이터베이스에 저장
df.to_sql('mytable', con=engine, if_exists='replace', index=False)

