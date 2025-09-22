import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
except:
    print('not able to connect')

cursor=conn.cursor()

query='create database 10000coders'

cursor.execute(query)


conn.commit()
cursor.close()
conn.close()