from sqlalchemy import create_engine
import pandas as pd
import mysql.connector as cn
import json


with open('/home/synferlo/mySQL/local_info.json', 'r') as f:
    info = json.load(f)

link = cn.connect(
        user = info['user'],
        password = info['password'],
        host = info['host'],
        database = 'eth_on_chain'
        )



df = pd.read_csv('/home/synferlo/my_disk/git/data/sample_dataset/sample_eth_blocks_tx.csv')
time_format = '%Y-%m-%d %H:%M:%S'
df['block_time'] = pd.to_datetime(df['block_time'], format = time_format)
df['tx_value'] = df['tx_value'].astype(float)
df1 = df.head(2000)
print(df1)


with open('/home/synferlo/mySQL/local_info.json', 'r') as f:
    data = json.load(f)
host = data['host']
database = 'eth_on_chain'
user = data['user']
password = data['password']

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=host, db=database, user=user, pw=password))

# Convert dataframe to sql table                                   
# if_exists: 'append', 'replace'
df.to_sql('tx_info', engine, index=False, if_exists = 'append')






