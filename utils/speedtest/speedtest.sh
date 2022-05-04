#准备好所需文件
wget -O clash.gz https://github.com/Dreamacro/clash/releases/download/v1.10.0/clash-linux-amd64-v1.10.0.gz
gunzip clash.gz
wget -O lite.gz https://github.com/alanbobs999/LiteSpeedTest/releases/download/v0.9.1/lite-linux-amd64-v0.9.1.gz
gunzip lite.gz
wget -O clash_config.yml https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/utils/speedtest/clash_config.yml
wget -O proxychains.conf https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/utils/speedtest/proxychains.conf
wget -O lite_config.json https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/utils/speedtest/lite_config.json
#初始化 Clash
chmod +x ./clash && ./clash &
#安装并配置 proxychains
sudo apt-get install proxychains
sudo chmod 777 ../../../../../etc/proxychains.conf
mv -f proxychains.conf ../../../../../etc/proxychains.conf
#开始运行 Clash
sudo pkill -f clash
./clash -f clash_config.yml &
#运行 LiteSpeedTest
chmod +x ./lite
sudo nohup proxychains ./lite --config ./lite_config.json --test https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml >speedtest.log 2>&1 &
