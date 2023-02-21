import mysql.connector as cn
import json
import pandas as pd
import numpy as np

def show(result):
    for i in result:
        print(i)


with open('/home/synferlo/mySQL/local_info.json', 'r') as f:
    usr_info = json.load(f)
    
'''
###------Get all databases: show databases------###
'''



#link = cn.connect(
#        user = usr_info['user'],
#        password = usr_info['password'],
#        host = usr_info['host']
#        )
#cursor = link.cursor()
#command = "show databases"
#cursor.execute(command)
#show(cursor)


'''
###------Create new database------###
'''

#link = cn.connect(
#        user = usr_info['user'],
#        password = usr_info['password'],
#        host = usr_info['host']
#        )
#
#cursor = link.cursor()
#command = "create database if not exists airbnb"
#cursor.execute(command)
#command = "show databases"
#cursor.execute(command)
#show(cursor)




'''
###------Create new table------###


Note, if your column name include (), e.g., gas_price(ETH), you must use `gas_price(ETH)`
when you create table.
Example:
    create table tx_info(
        block_hash varchar(100),
        `gas(ETH)` double,
        `gas_price(ETH)` double
    )



!!!! You must specify the number of character in the parenthesis when you define "varchar(n)". n is needed.
###------Import data from pandas dataframe------###

Method 1: use INSERT INTO
'''

#df = pd.read_csv('/home/synferlo/my_disk/git/data/sample_dataset/airbnb_NYC_2019.csv')[['id', 'name', 'room_type', 'price', 'number_of_reviews']]
df = pd.read_csv('/home/synferlo/my_disk/git/data/sample_dataset/airbnb_NYC_2019.csv')
df = df.replace(np.nan, '')
base_list = ['id', 'name', 'room_type', 'price', 'number_of_reviews']
room_base_info = df[base_list]
loc_list = ['id','neighbourhood_group', 'neighbourhood', 'latitude', 'longitude']
room_location = df[loc_list]
review_list = ['id', 'number_of_reviews', 'last_review', 'reviews_per_month']
room_review = df[review_list]
print(df)
for i in df.columns:
    print(i)

table = {
        "room_base_info":['id', 'name', 'room_type', 'price', 'number_of_reviews'],
        "room_location":['id','neighbourhood_group', 'neighbourhood', 'latitude', 'longitude'],
        "room_review":['id', 'number_of_reviews', 'last_review', 'reviews_per_month']
        }



sql_table = {}
sql_table['room_base_info'] = "(id varchar(20), name varchar(1000), room_type varchar(100), price int, number_of_reviews int)"

sql_table['room_location'] = "(id varchar(20), neighbourhood_group varchar(100), neighbourhood varchar(100), latitude double, longitude double)"

sql_table['room_review'] = "(id varchar(20),number_of_reviews int,last_review date, reviews_per_month int)"


link = cn.connect(
        user = usr_info['user'],
        password = usr_info['password'],
        host = usr_info['host'],
        database = 'airbnb'
        )
cursor = link.cursor()
#for i in ['room_base_info', 'room_location', 'room_review']:
for i in ['room_review']:
    cursor.execute(f"create table if not exists {i} {sql_table[i]}")
    sub_df = df[table[i]]
    for j, row in sub_df.iterrows():
        #command = f"insert into {i} values (%s, %s, %s, %s)"
        command = f"insert into {i} values ({','.join(['%s' for i in range(len(table[i]))])})"
        cursor.execute(command, tuple(row))
        link.commit()

#
#link = cn.connect(
#        user = usr_info['user'],
#        password = usr_info['password'],
#        host = usr_info['host'],
#        database = 'airbnb'
#        )
#cursor = link.cursor()
#if link.is_connected():
#    print('yes')
#cursor.execute("drop table if exists room_info")
#command = "create table if not exists room_info (name varchar(10000) not null, room_type varchar(100) not null, price int not null, number_of_reviews int not null)"
#cursor.execute(command)
#
#for i, row in df.iterrows():
#    command = "insert into room_info values (%s,%s,%s,%s)"
#    cursor.execute(command, tuple(row))
#    link.commit()




'''
###------Search data------###
select <column names> from <table name>
where <condition>

Note, in workbench, you need to specify the name of database, e.g., select * from airbnb.roo_info.   (<database name>.<table name>)

'''






