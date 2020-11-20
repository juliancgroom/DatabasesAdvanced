bash InstallMongoDB.sh
bash InstallRedis.sh

sudo apt-get python3
sudo apt-get install python3-pip

pip3 install bs4
pip3 install selenium
pip3 install pymongo
pip3 install pandas
pip3 install redis

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

python3 BlockChainScraperToRedis.py
python3 RedisToMongoDB.py

echo "webscraper started"
