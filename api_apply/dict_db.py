from mysql import connector
import requests
class sql_data:
    def __init__(self, user_dict):
        self.user_dict = user_dict
        self.database = connector.connect(host = self.user_dict['host'], user = self.user_dict['user'],
                                     password = self.user_dict['password'], database = self.user_dict['database'],
                                     port = self.user_dict['port'])
    def database_return(self):
        return self.database
class sql_functions(sql_data):
    def __init__(self, user_dict, order):
        super().__init__(user_dict)
        self.order = order
    # DB 데이터를 읽어들이는 함수
    def database_read(self):
        self.db_cursor = self.database.cursor()
        self.sql = stp("type order to read database\n>")
        self.db_cursor.execute(sql)
        self.rows = db_cursor.fetchall()
        return self.rows
    # DB 데이터를 수정하는 함수
    def database_cursor(self):
        self.db_cursor = self.database.cursor()
        self.sql = stp("type order\n>")
        self.db_cursor.execute(sql)
        # 변경 사항의 저장
        self.database.commit()
    # DB 데이터를 수정하는 함수2
    def database_cursor_2(self):
        self.db_cursor = self.database.cursor()
        self.sql = self.order
        self.db_cursor.execute(self.sql)
        # 변경 사항의 저장
        self.database.commit()
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={
    'serviceKey' : f'oTPgW%2FDH05NohBbfUUlPu%2BqzSlbx0bIV3%2B%2BPrAHe%2BMQGVitqflrS%2BDSewtiJYO4FKc3ZrOfNo55vtp%2B7i4D6Vg%3D%3D', 
    'pageNo' : '1', 
    'numOfRows' : '1000', 
    'dataType' : 'json', 
    'base_date' : '20210628', 
    'base_time' : '0600', 
    'nx' : '55', 
    'ny' : '127' 
    }

user_dict = {
    'host' : '192.168.90.119',
    'port' : '3306',
    'user' : 'myname',
    'database' : 'mydb',
    'password' : '1234'
}

response = requests.get(url, params=params)
response2 = response.json()
re = response2['response']['body']['items']['item']
name_list = list(re.keys())
order = "CREATE TABLE {} ({})".format("test_lsy", " VARCHAR(255),".join(name_list) + " VARCHAR(255)")
connected_1 = sql_functions(user_dict, order)
connected_1.database_cursor_2()