import pymysql
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='sq5590iq3056!',
                     db='studyroom',
                     charset='utf8')
cursor = db.cursor()

sql = '''
CREATE TABLE user(

    id VARCHAR(15) NOT NULL,
    phone INT NOT NULL,
    roomnum INT NOT NULL,
    PRIMARY KEY(id, phone)
);
'''
cursor.execute(sql)

sql = '''
    SHOW TABLES
'''
cursor.execute(sql)
db.commit()
