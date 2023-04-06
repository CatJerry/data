from mysql import connector

def database_connect(localhost, user_name, password, db_name, port_number):
    database = connector.connect(host = localhost, user = user_name, password = password, 
                                 database = db_name, port = port_number)
    return database

def database_cursor_2(database, order):
    db_cursor = database.cursor()
    sql = order
    db_cursor.execute(sql)
    database.commit()
def database_cursor_3(database, order):
    db_cursor = database.cursor()
    sql = order
    db_cursor.execute(sql)
    rows = db_cursor.fetchall()
    return rows
# 테이블 생성
order_sql_group_table_make = """CREATE TABLE sql_group_lsy
(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(20) NOT NULL
)"""
order_quiz_table_make = """CREATE TABLE quiz_lsy
(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
sql_group INT NOT NULL,
question VARCHAR(255) NOT NULL,
answer VARCHAR(255) NOT NULL,
FOREIGN KEY(sql_group) REFERENCES sql_group_lsy(id)
)"""
def category_insert():
    category = input('질문 유형을 입력하시오 : ')
    order3 = f'''INSERT INTO sql_group_lsy (name) values('{category}');'''

config_dict = {
    'host' : '192.168.90.119',
    'port' : '3306',
    'user' : 'myname',
    'database' : 'mydb',
    'password' : '1234'
}

def quiz_insert(category,question,answer):
    insert =  f'''INSERT INTO quiz_lsy (sql_group,question,answer) values({category},'{question}','{answer}');'''
    database_cursor_2(database,insert)

database = database_connect(config_dict['host'], config_dict['user'], config_dict['password'], config_dict['database'], config_dict['port'])
# quiz_insert()
# database_cursor_2(database, order_sql_group_table_make)
# database_cursor_2(database, order_quiz_table_make)
# database_cursor_2(database,order3)

def select():
    insert =  f'''SELECT question,answer FROM quiz_lsy '''
    response = database_cursor_3(database,insert)
    return response
