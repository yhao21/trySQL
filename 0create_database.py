import mysql.connector as cn
import json





###------Connect to MySQL------###

with open('/home/synferlo/mySQL/local_info.json', 'r') as f:
    data = json.load(f)

db = cn.connect(
        host = data['host'],
        user = data['user'],
        password = data['password']
        )
print(db)


###------Create a database------###
dothis = db.cursor()
dothis.execute('create database myfirstdb')




