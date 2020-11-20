wget  http :// download.redis.io/redis -stable.tar.gz
tar  xvzf  redis -stable.tar.gz3
cd redis -stable

sudo apt-get install make
sudo apt-get install gcc
sudo apt-get install tcl
sudo apt-get install build-essential
sudo apt-get update

make distclean

make

redis-cli<<EOF
CONFIG SET requirepass "julian"
EOF
cd src
sudo apt-get install redis-server