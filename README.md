# TopFreeProxies
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alanbobs999/topfreeproxies/sub_merge?label=sub_merge)](https://github.com/alanbobs999/TopFreeProxies/actions/workflows/sub_merge.yml) 

![Watchers](https://img.shields.io/github/watchers/alanbobs999/topfreeproxies) ![Stars](https://img.shields.io/github/stars/alanbobs999/topfreeproxies) ![Forks](https://img.shields.io/github/forks/alanbobs999/topfreeproxies) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=alanbobs999.topfreeproxies) ![LICENSE](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)

[仓库介绍](https://github.com/alanbobs999/TopFreeProxies#仓库介绍) | [使用方法](https://github.com/alanbobs999/TopFreeProxies#使用方法) | [节点信息](https://github.com/alanbobs999/TopFreeProxies#节点信息) | [软件推荐](https://github.com/alanbobs999/TopFreeProxies#客户端选择) | [机场推荐](https://github.com/alanbobs999/TopFreeProxies#机场推荐) | [仓库声明](https://github.com/alanbobs999/TopFreeProxies#仓库声明)

## 仓库介绍
本仓库自动化功能全部基于 `GitHub Actions` 实现，如果有需要可以自行 Fork 实现个性化需求。

对网络上各免费节点池及博主分享的节点进行测速筛选出较为稳定高速的节点，再导入到仓库中进行分享记录。所筛选的节点链接在仓库 `./sub/sub_list.json` 文件中，其中大部分为其他 `GitHub` 仓库链接，如果大家有好的订阅链接欢迎提交 PR ，这些链接包含的所有节点会合并在仓库 `./sub/sub_merge.txt` 中。

测速筛选后的节点订阅文件在仓库根目录 `Eterniy`(Base64) 和 `Eternity.yml`(Clash)。同时在仓库的 `./update` 中保留了原始节点链接的的记录。

测速功能使用 [LiteSpeedTest](https://github.com/xxf098/LiteSpeedTest) 在 `GitHub Actions` 环境下实现，所以美国节点较多，不能很好代表国内网络环境下节点可用性，目前正在解决这一问题。

虽然是测速筛选过后的节点，但仍然会出现部分节点不可用的情况，遇到这种情况建议选择`Clash`, `Shadowrocket`之类能自动切换低延迟节点的客户端。

## 使用方法
将以下订阅链接导入相应客户端即可。链接中大部分为 SS 协议节点，少量 Vmess, Trojan ,SSR 协议节点，建议选择协议支持完整的客户端。

- [多协议Base64编码](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity)
- [Clash](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity.yml)

另有国内加速链接：

- [多协议Base64编码](https://fastly.jsdelivr.net/gh/alanbobs999/TopFreeProxies@master/Eternity)
- [Clash](https://fastly.jsdelivr.net/gh/alanbobs999/TopFreeProxies@master/Eternity.yml)

>`Clash`链接所使用的配置在仓库`./update/provider/`中，有相应配置文件和以国家分类的`proxy-provider`。
>
>需要其它配置可使用订阅转换工具自行转换。
>自用在线订阅转换网址：[sub-web-modify](https://sub.v1.mk/)

## 节点信息
### 高速节点
高速节点数量: `99`
<details>
  <summary>展开复制节点</summary>

    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQzNSB8NjMuOTdNYiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY2MiB8MTI5LjgwTWIiLCJhZGQiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDExMiIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57mtJvmnYnnn7ZDaG9vcGHmlbDmja7kuK3lv4MgMjAiLCJhZGQiOiI0NS43Ni4xNzMuMjUwIiwicG9ydCI6IjY1MzQwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImI2MjBkNzhhLWQzYTctNDk2Zi1hZjMyLTU2NTE4NTQ3M2ViOCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvNUNpM2g2WUIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQ0NSB8MTUxLjk5TWIiLCJhZGQiOiJpZXNlaTFlaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoidGxzIn0=
    trojan://118fc04e-fb8c-4154-9092-352cf1958fcd@free.spcloud.us:21010?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40poduvjd%29
    trojan://118fc04e-fb8c-4154-9092-352cf1958fcd@free.spcloud.us:21010?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20036
    trojan://118fc04e-fb8c-4154-9092-352cf1958fcd@free.spcloud.us:21010?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2011
    trojan://118fc04e-fb8c-4154-9092-352cf1958fcd@free.spcloud.us:21010?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20JP-150.230.213.26-101
    trojan://280a1162-00cb-11ec-a8bf-f23c91cfbbc9@us2.tcpbbr.net:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E8%B4%B9%E5%88%A9%E8%92%99Linode%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2015
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV8xIiwiYWRkIjoiZG91YmFuLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbW92aWVzIiwiaG9zdCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    trojan://118fc04e-fb8c-4154-9092-352cf1958fcd@free.spcloud.us:21010?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_43
    trojan://280a1162-00cb-11ec-a8bf-f23c91cfbbc9@us2.tcpbbr.net:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_46
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMy4xMzguMzcuNjMtMTExIiwiYWRkIjoiZG91YmFuLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbW92aWVzIiwiaG9zdCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMTkyLjk2LjIwNC4yNTAtMDU5IiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMy4xMzguMzcuNjMtMTgwIiwiYWRkIjoiZG91YmFuLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbW92aWVzIiwiaG9zdCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiQ0FfMzE2IHw1Ny4xMU1iIiwiYWRkIjoidXNhLWJ1ZmZhbG8ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQxMCB8NDAuNTZNYiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpDZm9SMXlSSnByb3A@104.224.141.225:700#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20059
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQzMiB8ODcuOTRNYiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQ2NyB8NzkuOThNYiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiQ0FfMzE5IHwxNDkuNDJNYiIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://118fc04e-fb8c-4154-9092-352cf1958fcd@free.spcloud.us:21010?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG-138.2.85.75-176
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMt6auY6YCf6IqC54K55o6o6I2Q77yadjEubWsvdmlwIiwiYWRkIjoidXMuYXF2cG4ubWUiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmMxOTA1YzUtOGExOS00OTQ4LTlmMGQtZTZlNTQyN2JjNzJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXMuYXF2cG4ubWUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQyOSB8MTE2LjI5TWIiLCJhZGQiOiJ1cy5hcXZwbi5tZSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmYzE5MDVjNS04YTE5LTQ5NDgtOWYwZC1lNmU1NDI3YmM3MmYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ1cy5hcXZwbi5tZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS92MnJheWZyZWUgLSDnvo7lm70gIDE5IiwiYWRkIjoidXMuYXF2cG4ubWUiLCJwb3J0IjoiODAiLCJ0eXBlIjoiYXV0byIsImlkIjoiZmMxOTA1YzUtOGExOS00OTQ4LTlmMGQtZTZlNTQyN2JjNzJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXMuYXF2cG4ubWUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDE5IiwiYWRkIjoidXMuYXF2cG4ubWUiLCJwb3J0IjoiODAiLCJ0eXBlIjoiYXV0byIsImlkIjoiZmMxOTA1YzUtOGExOS00OTQ4LTlmMGQtZTZlNTQyN2JjNzJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXMuYXF2cG4ubWUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDE5IiwiYWRkIjoidXMuYXF2cG4ubWUiLCJwb3J0IjoiODAiLCJ0eXBlIjoiYXV0byIsImlkIjoiZmMxOTA1YzUtOGExOS00OTQ4LTlmMGQtZTZlNTQyN2JjNzJmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXMuYXF2cG4ubWUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV8yIiwiYWRkIjoiZG91YmFuLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbW92aWVzIiwiaG9zdCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzI0MjkiLCJhZGQiOiJ1cy5hcXZwbi5tZSIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiJmYzE5MDVjNS04YTE5LTQ5NDgtOWYwZC1lNmU1NDI3YmM3MmYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJ1cy5hcXZwbi5tZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMTUwLjIzMC40My42NS0xMDAiLCJhZGQiOiIxNTAuMjMwLjQzLjY1IiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjE1NTZlMDQwLTMxZDMtNGM0Ny1iMGQyLWRkZjg4ODAxMGI0ZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2hscy9jY3R2NXBoZC5tM3U4IiwiaG9zdCI6Inp6Y20wNi5iZGF0ZS54eXoiLCJ0bHMiOiIifQ==
    trojan://280a1162-00cb-11ec-a8bf-f23c91cfbbc9@us2.tcpbbr.net:443?allowInsecure=1#US_2456%20%7C54.93Mb
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY3MyB8MTUxLjUzTWIiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY0OSB8NzcuMjhNYiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://280a1162-00cb-11ec-a8bf-f23c91cfbbc9@us2.tcpbbr.net:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E8%B4%B9%E5%88%A9%E8%92%99Linode%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2015
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyMiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV8xIiwiYWRkIjoiZG91YmFuLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbW92aWVzIiwiaG9zdCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY0OSB8NzcuMjhNYiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=1#NL_1018%20%7C82.30Mb
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1&sni=fhcamd2.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2039
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US_2455%20%7C65.55Mb
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US_2700%20%7C77.61Mb
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-192.3.255.28-053
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpDZm9SMXlSSnByb3A@104.224.141.225:700#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20059
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMTA0LjIyNC4xODguMjktMTgzIiwiYWRkIjoiMTA0LjIyNC4xODguMjkiLCJwb3J0IjoiMzgyMjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI5OWZiNzgtMjkwYy00YWFkLWJlZmItMDEzMGMwNzRhNjIyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLjk4ODQ4Lnh5eiIsInRscyI6IiJ9
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#US_1223%20%7C65.56Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9ICA5IiwiYWRkIjoiMTU1LjI0OC4yMDIuMjAzIiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMGRhMzc5LWE3Y2MtNDM4OS04OGQ3LTQ1NTE0Yjg5Njg4MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJsaXZlc3RyZWFtMi50djM2MC52biIsInRscyI6IiJ9
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-208.109.189.58-052
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjciLCJhZGQiOiIxODUuMjAyLjE3Mi4yNDMiLCJwb3J0IjoiNDA5NDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDg1Mzc4MjAtMTRmMy00ZGU3LWQyNmUtYTNiODhiY2YwMTVhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57mtJvmnYnnn7ZJVDfnvZHnu5wgNyIsImFkZCI6IjEwNC4yMjQuMTg4LjI5IiwicG9ydCI6IjM4MjI2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyOTlmYjc4LTI5MGMtNGFhZC1iZWZiLTAxMzBjMDc0YTYyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-208.109.190.68-056
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US_2512%20%7C46.85Mb
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%5B05-15%5D%7Coslook%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US_2471%20%7C76.55Mb
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-208.109.189.58-034
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%5B05-14%5D%7Coslook%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQ0MiB8NTEuODFNYiIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpDZm9SMXlSSnByb3A@104.224.141.225:700#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20045
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpDZm9SMXlSSnByb3A@104.224.141.225:700#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20045
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IiwiYWRkIjoiMTU1LjI0OC4yMDIuMjAzIiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMGRhMzc5LWE3Y2MtNDM4OS04OGQ3LTQ1NTE0Yjg5Njg4MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLzM0ZmdyeWhiZ3YvIiwiaG9zdCI6ImhpbGluay52cDJwLm9ubGluZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDE2OSIsImFkZCI6IjE1NS4yNDguMjAyLjIwMyIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiI0YTBkYTM3OS1hN2NjLTQzODktODhkNy00NTUxNGI4OTY4ODMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS92MnJheWZyZWUgLSDnvo7lm70gIDEwIiwiYWRkIjoiMTg1LjIwMi4xNzIuMjQzIiwicG9ydCI6IjQwOTQxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ4NTM3ODIwLTE0ZjMtNGRlNy1kMjZlLWEzYjg4YmNmMDE1YSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxMiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-192.3.255.28-092
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtMTUwLjIzMC40My42NS0xNjYiLCJhZGQiOiIxNTAuMjMwLjQzLjY1IiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjE1NTZlMDQwLTMxZDMtNGM0Ny1iMGQyLWRkZjg4ODAxMGI0ZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJoay1jMy5teXV1dXNzcy5jb20iLCJ0bHMiOiIifQ==
    trojan://280a1162-00cb-11ec-a8bf-f23c91cfbbc9@us2.tcpbbr.net:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Fv2rayfree%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E8%B4%B9%E5%88%A9%E8%92%99Linode%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2015
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NiIsImFkZCI6IjE1MC4yMzAuNDMuNjUiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTU1NmUwNDAtMzFkMy00YzQ3LWIwZDItZGRmODg4MDEwYjRlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvMTdhZjc2ZTEtYTVkNy00MWFiLWFlODctYjQ4ZjE4NTA3NWQxLXZtZXNzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:805#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwMSIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiSUUtNTQuNzguMTM0LjExMS0wODYiLCJhZGQiOiJsbHV1Y2MzLmhlcm9rdWFwcC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdmZjNkOWM5LTIxNTMtNGQzYy05MzlkLTY5Nzg1MGM5NWIyMSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZjQ5NWJhMWYiLCJob3N0IjoibGx1dWNjMy5oZXJva3VhcHAuY29tIiwidGxzIjoidGxzIn0=
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_44
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwOSIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US-129.146.135.157-054
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyMCIsImFkZCI6Imx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJsdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6og54ix5bCU5YWwIiwiYWRkIjoibGx1dWNjMy5oZXJva3VhcHAuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmYzZDljOS0yMTUzLTRkM2MtOTM5ZC02OTc4NTBjOTViMjEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Y0OTViYTFmIiwiaG9zdCI6ImxsdXVjYzMuaGVyb2t1YXBwLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyNSIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwLTIwLjEyMy4xODcuMjEyLTA0NiIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIyMC4xMjMuMTg3LjIxMiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMtNDUuMzUuODQuMTYyLTA5MyIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIiwiYWRkIjoiMjAuMTIzLjE4Ny4yMTIiLCJwb3J0IjoiMjc5MzEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2ZWFlNDEtMGI4Zi00ZmFhLWJjZTgtNjM2NjAxMWRjMTlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIiwiYWRkIjoiMjAuMTIzLjE4Ny4yMTIiLCJwb3J0IjoiMjc5MzEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2ZWFlNDEtMGI4Zi00ZmFhLWJjZTgtNjM2NjAxMWRjMTlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiNDUuMzUuODQuMTYyIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:805#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIiwiYWRkIjoiMjAuMTIzLjE4Ny4yMTIiLCJwb3J0IjoiMjc5MzEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2ZWFlNDEtMGI4Zi00ZmFhLWJjZTgtNjM2NjAxMWRjMTlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjAwMDEudXMuZ2VuenBuLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIiwiYWRkIjoiMjAuMTIzLjE4Ny4yMTIiLCJwb3J0IjoiMjc5MzEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2ZWFlNDEtMGI4Zi00ZmFhLWJjZTgtNjM2NjAxMWRjMTlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3d3LmZhbnFpYW5ndnBuLmNvbSIsImhvc3QiOiJjbG91ZGZsYXJlLXdhcnAuZmFucWlhbmd2cG4uY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIiwiYWRkIjoiMjAuMTIzLjE4Ny4yMTIiLCJwb3J0IjoiMjc5MzEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2ZWFlNDEtMGI4Zi00ZmFhLWJjZTgtNjM2NjAxMWRjMTlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjIwLjEyMy4xODcuMjEyIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwOSIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQ0NiB8NzguOThNYiIsImFkZCI6Imx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJsdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQyNSB8NTQuNDdNYiIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://58d32c66-43b1-4561-9951-d87c9123774e@jgwld4.gaox.ml:443?allowInsecure=0#%F0%9F%87%AC%F0%9F%87%A7%20github.com%2Ffreefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Oracle%E4%BA%91%E8%AE%A1%E7%AE%97%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2030
    trojan://58d32c66-43b1-4561-9951-d87c9123774e@jgwld4.gaox.ml:443?allowInsecure=0#%F0%9F%87%AC%F0%9F%87%A7%20github.com%2Ffreefq%20-%20%E8%8B%B1%E5%9B%BD%E4%BC%A6%E6%95%A6Oracle%E4%BA%91%E8%AE%A1%E7%AE%97%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%2030
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzMxMzEiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9IDAwMSIsImFkZCI6Ijc4LjQ2LjI0NC4zNCIsInBvcnQiOiIzMzY1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiNDEzMDNiNC1lMmM4LTQ3NzEtY2I2Yy1lZjYyMjQ0YTc2MjEiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjQ3NiIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dpcyIsImhvc3QiOiJhYS5ob3VkaW5peC5zcGFjZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY2MiB8MTI5LjgwTWIiLCJhZGQiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6ogREUtNzguNDYuMjQ0LjM0LTAwMyIsImFkZCI6Ijc4LjQ2LjI0NC4zNCIsInBvcnQiOiIzMzY1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiNDEzMDNiNC1lMmM4LTQ3NzEtY2I2Yy1lZjYyMjQ0YTc2MjEiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0Ijoic3hxeGouY24iLCJ0bHMiOiIifQ==

</details>

### 所有节点
合并节点总数: `6572`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `71`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `44`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `134`
- [freefq/free](https://github.com/freefq/free), 节点数量: `50`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `277`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `51`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `114`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3344`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `184`
- [iwxf/free-v2ray](https://github.com/iwxf/free-v2ray), 节点数量: `5`
- [ldir92664/Vmess-Actions](https://github.com/ldir92664/Vmess-Actions), 节点数量: `118`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `42`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `120`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `145`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `50`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `56`
- [tomdegnan/clashrule](https://github.com/tomdegnan/clashrule), 节点数量: `214`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `23`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `203`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `120`
- [KYLELI1991/sysucc](https://github.com/KYLELI1991/sysucc), 节点数量: `0`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `29`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `50`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `0`
- [poduv/poduv](https://github.com/poduv/poduv), 节点数量: `16`
- [ok1991/v2ray](https://github.com/ok1991/v2ray), 节点数量: `127`
- [parkerpa/jsfxs](https://github.com/parkerpa/jsfxs), 节点数量: `582`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `14`
- [songkaik/Sub](https://github.com/songkaik/Sub), 节点数量: `73`
- [yosefwang/subscription](https://github.com/yosefwang/subscription), 节点数量: `17`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `58`

## 客户端选择
### 主流桌面客户端
|                            MacOS                             |                            Linux                             |                           Windows                            | 简易描述                                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :------------------------------------------------- |
| [CFW](https://github.com/Fndroid/clash_for_windows_pkg/releases) | [CFW](https://github.com/Fndroid/clash_for_windows_pkg/releases) | [CFW(Clash For Windows)](https://github.com/Fndroid/clash_for_windows_pkg/releases) | SS, SSR, Trojan, Vmess, VLESS协议支持，策略分流能力强。            |
|     [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)      |     [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)      |     [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)      | SS, SSR, Trojan, Vmess, VLESS, Trojan-Go协议支持（需安装相关插件）。 |
|                              ×                               |                              ×                               |      [V2rayN](https://github.com/2dust/v2rayN/releases)      | SS, Trojan, Vmess, VLESS协议支持，有测速，测延迟功能，支持订阅，二维码，剪贴板导入及手动配置。                 |
|                              ×                               |                              ×                               |    [WinXray](https://github.com/TheMRLL/winxray/releases)    | SS, SSR, Trojan, Vmess, VLESS协议支持，支持自动连接最快节点。            |
|                              ×                               |                              ×                               | [Shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows/releases) | SS协议支持， SS 专用客户端。                                       |
|                              ×                               |                              ×                               | [ShadowsocksR-windows](https://github.com/HMBSbige/ShadowsocksR-Windows/releases) | SSR协议支持，SSR 专用客户端。                                      |
|                [Surge](https://nssurge.com/)                 |                              ×                               |                              ×                               | SS, Trojan, Vmess协议支持，著名网络调试工具，策略分流能力强大，需付费。                        |
|   [ClashX](https://github.com/yichengchen/clashX/releases)   |                              ×                               |                              ×                               | SS, SSR, Trojan, Vmess协议支持，占用资源较少。                   |
|      [V2rayU](https://github.com/yanue/V2rayU/releases)      |                              ×                               |                              ×                               | SS, Trojan, Vmess协议支持，支持订阅，二维码，剪贴板导入，手动配置，二维码分享，与 V2RayN 类似。                        |

### 主流移动客户端
|                          iOS/iPadOS                          |                           Android                            | 简易描述                                                     |
| :----------------------------------------------------------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
| [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) | [Shadowrocket](https://play.google.com/store/apps/details?id=com.v2cross.proxy) | SS, SSR, Trojan, Vmess, VLESS协议支持，iOS端需在非国区 App Store 购买，美区售价 $2.99；安卓端非与 iOS 端同一作者，不支持 SSR 协议，免费且内置免费节点。 |
|                [Surge](https://nssurge.com/)                 |                              ×                               | SS, Trojan, Vmess协议支持，iOS 端著名网络调试工具，需付费。                                  |
| [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620) |                              ×                               | SS, SSR, Trojan, Vmess协议支持，需在非国区AppStore购买，美区售价$4.99。 |
| [Potatso Lite](https://apps.apple.com/us/app/potatso-lite/id1239860606) |                              ×                               | SS, SSR协议支持，需在非国区AppStore购买，免费。              |
|                              ×                               | [Surfboard](https://play.google.com/store/apps/details?id=com.getsurfboard) | SS, SSR, Vmess协议支持，安卓端网络调试软件，兼容 Surge 2 配置。 |
|                              ×                               | [CFA(Clash For Android)](https://github.com/Kr328/ClashForAndroid/releases) | SS, SSR, Trojan, Vmess协议支持。                             |
|                              ×                               |  [SagerNet](https://github.com/SagerNet/SagerNet/releases)   | SS, SSR, Trojan, Vmess, VLESS协议支持。                      |
|                              ×                               | [Shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android/releases) | SS协议支持，安卓专用 SS 客户端。                                                 |
|                              ×                               | [ShadowsocksR-android](https://github.com/HMBSbige/ShadowsocksR-Android/releases) | SSR协议支持，安卓专用 SSR 客户端。                                                |
|                              ×                               |     [V2rayNG](https://github.com/2dust/v2rayNG/releases)     | SS, Trojan, Vmess, VLESS协议支持，v2ray 内核。                           |

## 机场推荐
免费节点失效太快，推荐一些性价比高的机场应急使用。
- [魔戒.net](https://www.mojie.cyou/#/register?code=sAbl0qtT)
  - 按量计费机场, 1¥10G, 10¥130G
  - 所有套餐均是一样的节点与一样的服务，所有套餐流量永不过期，用完为止，不限制客户端数量，最高可提供 2Gbps 峰值。
- [大迅云](https://daxun.club/#/register?code=JPmAFPav)
  - 最低月付 5¥50G, 购买 12¥ 及以上套餐免费领取奈飞 + 迪士尼 Plus 共享号
  - 原生IP负载均衡，流媒体解锁晚高峰油管秒开，主打性价比，有试用
- [阿伟云](https://awslcn.xyz/#/register?code=8C18uZwl)
  - 最低月付 1¥ 起, 9.99¥100G
  - 无带宽速率限制，有流媒体解锁，香港 BGP 中继线路

## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

## 星标统计
[![Stargazers over time](https://starchart.cc/alanbobs999/TopFreeProxies.svg)](https://starchart.cc/alanbobs999/TopFreeProxies)