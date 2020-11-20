from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
import pandas
import time
import redis
import json

r=redis.Redis(
    host='localhost',
    port=6379,
    password='julian'
)

url = "https://www.blockchain.com/btc/unconfirmed-transactions"
wd = webdriver.Firefox()
wd.get(url)

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
    
    print("hello")

    print(Data.to_json())
    r.set('tx', Data.to_json())
    r.expire('tx', 60)

    time.sleep(60)
