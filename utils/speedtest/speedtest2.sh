wget -O lite-linux-amd64 https://github.com/mahdibland/SSAggregator/releases/download/1.0.0/lite-linux-
wget -O proxychains.conf https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/utils/speedtest/proxychains.conf
wget -O lite_config.json https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/utils/speedtest/lite_config.json
###################
#运行 LiteSpeedTest
chmod +x ./lite-linux-amd64
sudo ./lite-linux-amd64 --config ./lite_config.json --test https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity >speedtest.log 2>&1 &
