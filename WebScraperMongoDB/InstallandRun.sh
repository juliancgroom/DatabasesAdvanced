bash InstallMongoDB.sh

sudo apt-get python3
sudo apt-get install python3-pip

pip3 install bs4
pip3 install selenium
pip3 install pymongo
pip3 install pandas

mongo<<EOF
use admin;
db.createUser(
    {
        user: "webscraper",
        pwd: "password",
        roles: ["readWrite", "dbAdmin"]
    }
);
EOF

python3 BlockChainScraperMongoDB.py

echo "webscraper started"
