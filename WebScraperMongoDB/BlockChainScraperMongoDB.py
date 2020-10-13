from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
import urllib.parse
import pandas
import time

url = "https://www.blockchain.com/btc/unconfirmed-transactions"
wd = webdriver.Firefox()
wd.get(url)

username = urllib.parse.quote_plus('webscraper')
password = urllib.parse.quote_plus('password')
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

Blockchain_DB = client["Blockchain_DB"]
Col_TopTransactions = Blockchain_DB["col_TopTransactions"]

while True:

    html_doc = wd.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    list_of_values = []
    Hashes = []
    Times = []
    BTCs = []
    USDs = []

    for value in soup.find_all("div", attrs={"class": "sc-6nt7oh-0 kduRNF"}):
        list_of_values.append(value.get_text())

    for i in range(len(list_of_values)):
        if i % 4 == 0:
            Hashes.append(list_of_values[i])

        elif i % 4 == 1:
            Times.append(list_of_values[i])

        elif i % 4 == 2:
            BTCs.append(list_of_values[i][0:len(list_of_values[i]) - 4])

        elif i % 4 == 3:
            USDs.append(list_of_values[i][1:])

    Data = pandas.DataFrame(list(zip(Hashes, Times, BTCs, USDs)),
                            columns=["Hash", "Time", "Amount (BTC)", "Amount (USD)"])

    Data["Amount (BTC)"] = Data["Amount (BTC)"].astype(float)

    top_tx = Data.sort_values(by=["Amount (BTC)"], ascending=False).head(1).iloc[0]

    Col_TopTransactions.insert_one(top_tx.to_dict())

    print(top_tx.to_dict())

    time.sleep(60)
