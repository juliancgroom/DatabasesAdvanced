## WebScraperMongoDB

### Prerequisits:
- Firefox
- Python (3.0 +)
- Python Libraries: selenium, bs4, pandas
- Geckodriver
- Ubuntu

### User Guide:

Run the <b>InstallandRun.sh</b> bash script from the WebScraperMongoDB folder. This will run the InstallMongoDB.sh and lockChainScraperMongoDB.py scripts.

### InstallMongoDB.sh

Installs MongoDB and creates a user "webscraper" with password "password".

### InstallandRun.sh

Runs InstallMongoDB then installs necessary python libraries if not already installed. Then it starts BlockChainScraperMongoDB.py.

### BlockChainScraperMongoDB.py

Creates and writes to a MongoDB database. While it is running, every minute a line is added to the log with the transaction information of the highest value transaction listed on https://www.blockchain.com/btc/unconfirmed-transactions. The transaction information recorded is "Hash", "Time", "Amount (BTC)", "Amount (USD)". The records are stored as json objects.
