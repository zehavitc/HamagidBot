__author__ = 'zehavitc'

import sqlite3 as lite
import os
# def connect():
# """ Connect to MySQL database """
#     try:
#         conn = .connector.connect(host='localhost',
#                                        database='python_mysql',
#                                        user='root',
#                                        password='secret')
#         if conn.is_connected():
#             print('Connected to MySQL database')
#
#     except Error as e:
#         print(e)
#
#     finally:
#         conn.close()

def WriteToDb(value, category):
        self.con.execute("INSERT INTO Category VALUES(?,?)", (value, category))

con = lite.connect('./category.sqlite3')
con.execute(("CREATE TABLE Category(Value VARCHAR(250), ValCategory VARCHAR(250))"))
con.text_factory = lambda x: unicode(x, 'utf-8', 'replace')


path = os.path.dirname(os.path.abspath(__file__))
sqlDb = os.path.join(path, 'hewiki-20150702-categorylinks.sql')
f = open(sqlDb, 'r')
line = f.readline()
while line is not None:
    if not line.startswith("INSERT INTO"):
        line = f.readline()
        continue
    startIdx = line.find('(') + 1
    endIdx = line.find(')')
    while (startIdx < len(line) and endIdx != -1):
        data = line[startIdx:endIdx].split(',')
