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

    vmess://eyJ2IjoiMiIsInBzIjoiQ0FfMzEyIHw1MS4xM01iIiwiYWRkIjoidXNhLWJ1ZmZhbG8ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MSIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MiIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MyIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5NiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpDZm9SMXlSSnByb3A@104.224.141.225:700#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20045
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDExMiIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2022
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzMxMzUiLCJhZGQiOiI0NS4zMi45NC4yNDkiLCJwb3J0IjoiMjk1ODkiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjNkYjA0NWMtZDkyMS00NjgzLWEwNjMtZDNjYjNhMTZhMWIwIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9hM2RIeE5pUy8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxYzBlNGExOC00ZDdhLTQyMzEtYTU1ZC0xZGVlMGZlNjczMmE@164.92.121.170:61598#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20036
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.107.59:16455#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20006
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%5B05-20%5D%7Coslook%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNToxYzBlNGExOC00ZDdhLTQyMzEtYTU1ZC0xZGVlMGZlNjczMmE@164.92.121.170:61598#DigitalOcean%204%7C0.7x
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%5B05-21%5D%7Coslook%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%5B05-20%5D%7Coslook%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-106.mitoption.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_42
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20mattkaydiary.com%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-106.mitoption.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_68
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_33
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.107.59:16455#TG%E9%A2%91%E9%81%93%40iosfulishare%20%F0%9F%87%BA%F0%9F%87%B8%20DigitalOcean%206%7C0.7x
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.107.59:16455#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20067
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-106.mitoption.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_33
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.115.89:31254#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20066
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.115.63:43371#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Fv2rayfree%20-%20%E7%BE%8E%E5%9B%BD%20%2010
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%5B05-20%5D%7Coslook%7C%E7%BE%8E%E5%9B%BD%28US%29USA%2FScottsdale_12
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.107.59:16455#YouTube%E6%A2%A6%E6%AD%8C%7CNetflix_50
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.115.63:43371#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MSIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDExMiIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.115.63:43371#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2010
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.107.59:16455#YouTube%E6%A2%A6%E6%AD%8C%7CNetflix_50
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-106.mitoption.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_43
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-106.mitoption.com:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_55
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.115.63:43371#YouTube%E6%A2%A6%E6%AD%8C%7CNetflix_37
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1NGRmMWFkNS0xMzIzLTRkZDctYjdhMS1hNTMyMDIzNDc1MjY@164.92.115.63:43371#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDExOCIsImFkZCI6IjE1NS4yNDguMjAyLjIwMyIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiI0YTBkYTM3OS1hN2NjLTQzODktODhkNy00NTUxNGI4OTY4ODMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9pbmRleCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiMTU1LjI0OC4yMDIuMjAzIiwidGxzIjoiIn0=
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_46
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjE1NS4yNDguMjAyLjIwMyIsInRscyI6IiJ9
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_51
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hp/Cfh6og5q+U5Yip5pe2IiwiYWRkIjoiMTk4LjIuMjAwLjExNiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDE4MDQ4YWYtYTI5My00Yjk5LTliMGMtOThjYTM1ODBkZDI0IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcGF0aC8xODEwMTIxMjM0MzMiLCJob3N0Ijoid3d3LjY4NDc4NTIwLnh5eiIsInRscyI6InRscyJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:805#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:803#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A803-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    trojan://ae71ffdc-3206-3b4d-3f4e-e3b63684a556@lsj03.wangxd.life:3052?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_53
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@54.213.84.59:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20019
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:802#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@51.161.118.38:805#%F0%9F%87%A8%F0%9F%87%A6%20CA%E5%8A%A0%E6%8B%BF%E5%A4%A7%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:803#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A803-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:805#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@54.213.84.59:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-54.213.84.59%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%BB%85%E6%94%AF%E6%8C%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpZYk9FNk8xdXdiVXY@37.218.247.88:443#%F0%9F%87%B3%F0%9F%87%B1%20%3A%E8%8D%B7%E5%85%B0-ss-37.218.247.88%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%BB%85%E6%94%AF%E6%8C%81%E8%8D%B7%E5%85%B0%E5%9C%B0%E5%8C%BANF%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:802#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpZYk9FNk8xdXdiVXY@37.218.247.88:443#%F0%9F%87%B3%F0%9F%87%B1%20%3A%E8%8D%B7%E5%85%B0-ss-37.218.247.88%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%BB%85%E6%94%AF%E6%8C%81%E8%8D%B7%E5%85%B0%E5%9C%B0%E5%8C%BANF%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@51.161.118.38:805#%F0%9F%87%A8%F0%9F%87%A6%20CA%E5%8A%A0%E6%8B%BF%E5%A4%A7%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1MCIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2luZGV4IiwiaG9zdCI6ImhrYXoxLnhtcnRoLW5vZGUueHl6IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@54.213.84.59:443#%F0%9F%87%BA%F0%9F%87%B8%20TG%E9%A2%91%E9%81%93%40iosfulishare%E7%BE%8E%E5%9B%BD5
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MiIsImFkZCI6IjIwLjEyMy4xODcuMjEyIiwicG9ydCI6IjI3OTMxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NmVhZTQxLTBiOGYtNGZhYS1iY2U4LTYzNjYwMTFkYzE5ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2luZGV4IiwiaG9zdCI6Ind3dy5iYWlkdS5jb20iLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@35.166.114.193:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20065
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpZYk9FNk8xdXdiVXY@37.218.247.88:443#%F0%9F%87%B3%F0%9F%87%B1%20%3A%E8%8D%B7%E5%85%B0-ss-37.218.247.88%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%BB%85%E6%94%AF%E6%8C%81%E8%8D%B7%E5%85%B0%E5%9C%B0%E5%8C%BANF%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@35.166.114.193:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20042
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:802#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1nY206NTRkZjFhZDUtMTMyMy00ZGQ3LWI3YTEtYTUzMjAyMzQ3NTI2@164.92.99.255:46499#DigitalOcean%203%7C0.7x
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:802#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A802-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:803#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A803-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:805#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.197:805#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.197%3A805-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIiwiYWRkIjoiMjAuMTIzLjE4Ny4yMTIiLCJwb3J0IjoiMjc5MzEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2ZWFlNDEtMGI4Zi00ZmFhLWJjZTgtNjM2NjAxMWRjMTlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjAwMDEudXMuZ2VuenBuLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6og54ix5bCU5YWwIiwiYWRkIjoibGx1dWNjMy5oZXJva3VhcHAuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmYzZDljOS0yMTUzLTRkM2MtOTM5ZC02OTc4NTBjOTViMjEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Y0OTViYTFmIiwiaG9zdCI6ImxsdXVjYzMuaGVyb2t1YXBwLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:803#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A803-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E5%8A%A0%E6%8B%BF%E5%A4%A7%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@35.166.114.193:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-35.166.114.193%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrvCfh6og54ix5bCU5YWwIiwiYWRkIjoibGx1dWNjMy5oZXJva3VhcHAuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI3ZmYzZDljOS0yMTUzLTRkM2MtOTM5ZC02OTc4NTBjOTViMjEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2Y0OTViYTFmIiwiaG9zdCI6ImxsdXVjYzMuaGVyb2t1YXBwLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9IDAwMSIsImFkZCI6Ijc4LjQ2LjI0NC4zNCIsInBvcnQiOiIzMzY1NSIsInR5cGUiOiJub25lIiwiaWQiOiJiNDEzMDNiNC1lMmM4LTQ3NzEtY2I2Yy1lZjYyMjQ0YTc2MjEiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImRvdXlpbmNkbi5jb20iLCJ0bHMiOiIifQ==

</details>

### 所有节点
合并节点总数: `5957`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `70`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `231`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `155`
- [freefq/free](https://github.com/freefq/free), 节点数量: `44`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `291`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `66`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `57`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3128`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `43`
- [iwxf/free-v2ray](https://github.com/iwxf/free-v2ray), 节点数量: `6`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `42`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `66`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `145`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `44`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `56`
- [tomdegnan/clashrule](https://github.com/tomdegnan/clashrule), 节点数量: `214`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `27`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `211`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `39`
- [KYLELI1991/sysucc](https://github.com/KYLELI1991/sysucc), 节点数量: `0`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `33`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `44`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `9`
- [poduv/poduv](https://github.com/poduv/poduv), 节点数量: `24`
- [ok1991/v2ray](https://github.com/ok1991/v2ray), 节点数量: `0`
- [parkerpa/jsfxs](https://github.com/parkerpa/jsfxs), 节点数量: `582`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `12`
- [songkaik/Sub](https://github.com/songkaik/Sub), 节点数量: `43`
- [yosefwang/subscription](https://github.com/yosefwang/subscription), 节点数量: `0`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `34`

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
  - 所有套餐均是一样的节点与一样的服务，所有套餐流量永不过期，用完为止，不限制客户端数量，最高可提供 2Gbps 峰值
- [大迅云](https://daxun.club/#/register?code=JPmAFPav)
  - 最低月付 5¥50G, 12¥200G, 购买 12¥ 及以上套餐免费领取奈飞 + 迪士尼 Plus 共享号
  - 原生IP负载均衡，流媒体解锁晚高峰油管秒开，主打性价比，有试用
- [阿伟云](https://awslcn.xyz/#/register?code=8C18uZwl)
  - 最低月付 1¥ 起, 9.99¥100G
  - 无带宽速率限制，有流媒体解锁，香港 BGP 中继线路

## 仓库声明
订阅节点仅作学习交流使用，只是对网络上节点的优选排序，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。

## 星标统计
[![Star History Chart](https://api.star-history.com/svg?repos=alanbobs999/TopFreeProxies&type=Date)](https://star-history.com/#alanbobs999/TopFreeProxies&Date)