# from request_data import update_data
from mysql import connector
import matplotlib.animation as animation
import mplfinance as mpf
import pandas as pd
import time
config_dict = {
    'host' : ',,,
    'port' : '3305',
    'user' : 'root',
    'database' : 'coin',
    'password' : ''
}

def database_connect(localhost, user_name, password, db_name, port_number):
    database = connector.connect(host = localhost, user = user_name, password = password, 
                                 database = db_name, port = port_number)
    return database

def database_cursor(database, order):
    db_cursor = database.cursor()
    sql = order
    db_cursor.execute(sql)
    rows = db_cursor.fetchall()
    return rows

database = database_connect(config_dict['host'], config_dict['user'], config_dict['password'], config_dict['database'], config_dict['port'])

def select_data(name):

    insert =  f'''SELECT candle_date_time_kst,opening_price,high_price,low_price,trade_price FROM coin_data where market like 'KRW-{name}' ORDER BY candle_date_time_kst;'''
    response = database_cursor(database,insert)
    return response


data = select_data('NEO')
df= pd.DataFrame(data, columns=['date','Open', 'High', 'Low', 'Close'])
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%S')
df.set_index('date', inplace=True)
df.drop_duplicates(inplace=True)

# fig = plt.figure(figsize=(20, 5))
# ax = fig.add_subplot(111)
colorset = mpf.make_marketcolors(up='tab:red', down='tab:blue', volume='tab:blue')
s = mpf.make_mpf_style(marketcolors=colorset)
mpf.plot(df,type='candle',style=s)
