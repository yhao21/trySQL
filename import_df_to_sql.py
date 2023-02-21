import pandas as pd
from sqlalchemy import create_engine
import json


'''
You need to install pymysql before importing sqlalchemy!

This is a fantastic function provided by pandas. You can import a dataframe to 
sql using function <df.to_sql>.

It is FASTER than inserting each row from iterrows()!!
'''



with open('/home/synferlo/mySQL/local_info.json', 'r') as f:
    data = json.load(f)
host = data['host']
database = 'eth_on_chain'
user = data['user']
password = data['password']


df = pd.read_csv(path_to_csv)

# create sql engine
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
        .format(host = host, db = database, user = user, pw = password))


# Convert dataframe to sql table                                   
# if_exists: 'append', 'replace'
df.to_sql('tx_info', engine, index=False, if_exists = 'append')
