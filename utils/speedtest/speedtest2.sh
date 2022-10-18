wget -O lite-linux-amd64 https://github.com/mahdibland/SSAggregator/releases/download/1.0.0/lite-linux-amd64
wget -O proxychains.conf https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/utils/speedtest/proxychains.conf
wget -O lite_config.json https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/utils/speedtest/lite_config.json
# proxychains
sudo apt-get install proxychains
sudo chmod 777 ../../../../../../etc/proxychains.conf
mv -f proxychains.conf ../../../../../../etc/proxychains.conf
#运行 LiteSpeedTest
chmod +x ./lite-linux-amd64
sudo nohub proxychains ./lite-linux-amd64 --config ./lite_config.json --test https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity >speedtest.log 2>&1 &
