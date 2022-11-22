#准备好所需文件
wget -O lite-linux-amd64.zip https://github.com/xxf098/LiteSpeedTest/releases/download/v0.13.1/lite-linux-amd64-v0.13.1.gz
gzip -d lite-linux-amd64-v0.13.1.gz
wget -O lite_config.json https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/utils/speedtest/lite_config_yaml.json
#运行 LiteSpeedTest
chmod +x ./lite-linux-amd64
sudo nohup ./lite-linux-amd64 --config ./lite_config.json --test subs >speedtest.log 2>&1 &
