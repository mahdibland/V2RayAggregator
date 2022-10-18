#准备好所需文件
wget -O lite-linux-amd64 https://github.com/mahdibland/SSAggregator/releases/download/1.0.0/lite-linux-amd64
wget -O lite_config.json https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/utils/speedtest/lite_config.json
#运行 LiteSpeedTest
chmod +x ./lite-linux-amd64
sudo nohup ./lite-linux-amd64 --config ./lite_config.json --test subs >speedtest.log 2>&1 &

