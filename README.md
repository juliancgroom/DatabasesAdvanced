# DatabasesAdvanced

## WebScraper

### Prerequisits:
- Firefox needs to be installed
- Python needs to be installed (3.0 +)
- Python Libraries: selenium, bs4, pandas
- Geckodriver

### User Guide:
Running the python script writes (overwrites) a log.txt file. While it is running, every minute a line is added to the log with the transaction information of the highest value transaction listed on https://www.blockchain.com/btc/unconfirmed-transactions. The transaction information recorded is "Hash", "Time", "Amount (BTC)", "Amount (USD)". The values are seperated by ";".
