from sqlalchemy import create_engine
import pymysql
# import api_apply/criminal.csv
# from mysql import connector
import pandas as pd

df = pd.read_csv('api_apply/criminal.csv',encoding='cp949')
df = pd.DataFrame(df)
HOST = "172.18.0.0"
PORT = "3306"
USER = "soyoung"
PW = "0000"
DATABASE = 'mydb'

engine = create_engine(f"mysql+pymysql://{USER}:{PW}@{HOST}:{PORT}/{DATABASE}")
df.to_sql(name='criminals', con=engine, if_exists='append', index=False)
