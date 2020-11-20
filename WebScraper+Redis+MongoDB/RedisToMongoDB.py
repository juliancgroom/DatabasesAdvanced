from pymongo import MongoClient
import urllib.parse
import pandas
import time
import redis
import json

username = urllib.parse.quote_plus('webscraper')
password = urllib.parse.quote_plus('password')
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

Blockchain_DB = client["Blockchain_DB"]
Col_TopTransactions = Blockchain_DB["col_TopTransactions"]

r=redis.Redis(
    host='localhost',
    port=6379,
    password='julian'
)

while True:

    Data = pandas.read_json(r.get('tx'))
    
    top_tx = Data.sort_values(by=["Amount (BTC)"], ascending=False).head(1).iloc[0]

    Col_TopTransactions.insert_one(top_tx.to_dict())
    print("Added to database")

    time.sleep(60)
