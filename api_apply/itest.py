from sqlalchemy import create_engine
import pandas as pd
import requests
import json

url = 'https://apis.data.go.kr/B553912/tk_sales/v1/yearly_sales?serviceKey=인증키&page=20&perPage=40&returnType=JSON'

db_type = 'mysql'
host = '0.0.0.0'
port = '3305'
database = 'srt_new'
username = 'soyoung'
password = '7610'

# API 서비스키 디코딩
url = requests.utils.unquote(url)

# API 응답 결과를 JSON 형식으로 디코딩
response = requests.get(url)
if response.status_code == 200:
    try:
        data = json.loads(response.text)
        df = pd.DataFrame(data['data'])
    except json.JSONDecodeError:
        print('JSON 디코딩 오류')
else:
    print(f'API 요청 오류: {response.status_code}')

# 데이터베이스 연결 엔진 생성
engine = create_engine(f'{db_type}://{username}:{password}@{host}:{port}/{database}')

# DataFrame을 SQL 데이터베이스에 저장
df.to_sql('srt', con=engine, if_exists='replace', index=False)
