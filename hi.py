import pandas as pd
import mysql.connector as cn
from sqlalchemy import create_engine
import json



def load_to_sql(df, host, user, password, database, table_name):
    engine = create_engine('mysql+pymysql://{my_user}:{my_pw}@{my_host}/{my_db}'
            .format(my_user = user, my_pw = password, my_host = host, my_db = database))
    df.to_sql(table_name, engine, index = False, if_exists = 'replace')


with open('/home/synferlo/mySQL/mydesktop_info.json', 'r') as f:
    info = json.load(f)

host, user, password, database = info['host'], info['user'], info['password'], 'airbnb'

df = pd.read_csv('/home/synferlo/my_disk/git/data/sample_dataset/airbnb_NYC_2019.csv')
room_info = df[['id','name', 'host_id', 'room_type', 'price', 'minimum_nights', 'availability_365']]
room_location = df[['id', 'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude']]
room_host = df[['host_id', 'host_name', 'calculated_host_listings_count']]
room_review = df[['id', 'number_of_reviews', 'last_review', 'reviews_per_month']]

load_to_sql(room_info, host, user, password, database, 'room_info')
load_to_sql(room_location, host, user, password, database, 'room_location')
load_to_sql(room_host, host, user, password, database, 'room_host')
load_to_sql(room_review, host, user, password, database, 'room_review')
'''
id x
name x
host_id x
host_name x
neighbourhood_group x
neighbourhood x
latitude x
longitude x
room_type x
price x
minimum_nights x
number_of_reviews
last_review
reviews_per_month
calculated_host_listings_count x
availability_365 x
'''
