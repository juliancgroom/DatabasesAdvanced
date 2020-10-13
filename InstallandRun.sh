bash InstallMongoDB.sh

pip install bs4
pip install selenium
pip install pymongo
pip install pandas

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
