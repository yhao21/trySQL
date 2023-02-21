import pandas as pd
from sqlalchemy import create_engine 
import mysql.connector as cn
import json



df = pd.read_csv('/home/synferlo/my_disk/git/machine_learning/498/time_data/chicago_crime_2018.csv')



with open('/home/synferlo/mySQL/local_info.json', 'r') as f:
    data = json.load(f)

host = data['host']
user = data['user']
password = data['password']
link = cn.connect(
        host = host,
        user = user,
        password = password
        )

db = 'chicago_crime'
cursor = link.cursor()
cursor.execute(f"create database if not exists {db}")

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
        .format(host = host, user = user, pw = password, db = db))


df.to_sql('crime_info', engine, index = False, if_exists = 'replace')
