import mysql.connector as cn
import json


###------Connect to server------###
with open('/home/synferlo/mySQL/mydesktop_info.json', 'r') as f:
    info = json.load(f)
link = cn.connect(
        user = info['user'],
        password = info['password'],
        host = info['host']
        )


###------Create database------###
cursor = link.cursor()
cursor.execute("create database airbnb")
