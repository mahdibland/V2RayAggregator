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

    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%202%EF%BD%9Copenit.ml
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%204
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=edge.apple.com#%E5%85%A8%E7%90%83%E7%9B%B4%E8%BF%9E%E2%91%A2
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%204
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NCIsImFkZCI6IjE0My4xOTguMTMwLjIxIiwicG9ydCI6IjQyMzgyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzYjQ1MmE3LTkwN2ItNGY3Ny04Y2E0LTYwMjUwY2M4MzViYyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=s3.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=1&sni=us-12.hmkj9.com#%F0%9F%87%BA%F0%9F%87%B8%20US%203%EF%BD%9Copenit.ml
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E6%B2%B9%E7%AE%A1%3A%E7%A0%B4%E8%A7%A3%E8%B5%84%E6%BA%90%E5%90%9B2.0%29
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=1&sni=us-12.hmkj9.com#%F0%9F%87%BA%F0%9F%87%B8%20US%2011%EF%BD%9Copenit.ml
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=1&sni=us-12.hmkj9.com#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%EF%BD%9Copenit.ml
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=1&sni=us-12.hmkj9.com#%F0%9F%87%BA%F0%9F%87%B8%20US%201%EF%BD%9Copenit.ml
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozZjQxMWU4Ny0zZTkzLTRmMjMtYmMyMi0yNjNhNzQ4YmM4YzU@164.92.107.59:1645#%F0%9F%87%BA%F0%9F%87%B8%20US%2012
    trojan://a9f14424-7572-4fe2-bfa8-8864590ff295@cdn018.youxi.gay:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2042%EF%BD%9Copenit.ml
    ss://YWVzLTI1Ni1nY206M2Y0MTFlODctM2U5My00ZjIzLWJjMjItMjYzYTc0OGJjOGM1@164.92.99.255:4649#%F0%9F%87%BA%F0%9F%87%B8%20US%208
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozZjQxMWU4Ny0zZTkzLTRmMjMtYmMyMi0yNjNhNzQ4YmM4YzU@164.92.107.59:1645#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD11
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTozZjQxMWU4Ny0zZTkzLTRmMjMtYmMyMi0yNjNhNzQ4YmM4YzU@164.92.115.89:3125#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%207
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDMyIiwiYWRkIjoidGFvYmFvLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjM2NzEyYmU4LWYyZmYtNDg3NS04YzY3LTk1ZWZkNjZhYzk5NCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZGlkaSIsImhvc3QiOiJ0YW9iYW8uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzYiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9pbmRleCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjU3IiwiYWRkIjoiMTQzLjE5OC4xMzAuMjEiLCJwb3J0IjoiNDIzODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDNiNDUyYTctOTA3Yi00Zjc3LThjYTQtNjAyNTBjYzgzNWJjIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=0&sni=us-12.hmkj9.com#%F0%9F%87%BA%F0%9F%87%B8%20US-%E9%AB%98%E9%80%9F%E8%8A%82%E7%82%B9%E6%8E%A8%E8%8D%90%EF%BC%9Av1.mk%2Fvip
    trojan://a9f14424-7572-4fe2-bfa8-8864590ff295@cdn017.youxi.gay:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2041%EF%BD%9Copenit.ml
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20US-%E9%AB%98%E9%80%9F%E8%8A%82%E7%82%B9%E6%8E%A8%E8%8D%90%EF%BC%9Av1.mk%2Fvip
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MSIsImFkZCI6IjE1MC4yMzAuNDMuMTA2IiwicG9ydCI6IjU0ODI5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImYyYjVjM2ZmLTg2YzctNGVmYS04MzFmLWZmMGZjZDc2NTZhNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2hhcHB5IiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzUiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzUiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxOCIsImFkZCI6ImJ3ZzIuZ3VzaGlkYXdhbmcuY2MiLCJwb3J0IjoiNTc1MzkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmNmNzIwMmMtYmQxYS00NGU5LWEyNWUtYmYxNTJmNmU1YzExIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvNTNmOWFkMC8iLCJob3N0IjoiYndnMi5ndXNoaWRhd2FuZy5jYyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NyIsImFkZCI6InRhb2Jhby5iYWJhemh1amkuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIzNjcxMmJlOC1mMmZmLTQ4NzUtOGM2Ny05NWVmZDY2YWM5OTQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2RpZGkiLCJob3N0IjoidGFvYmFvLmJhYmF6aHVqaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjM4IiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3REWmNDcWMiLCJob3N0IjoiZ2NmcmVlMS5nYWxheHktY2xvdWQuaWN1IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NiIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzYiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9pbmRleCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDMiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%EF%BD%9Copenit.ml
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@97.64.31.80:247#US_63
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2021%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMzA5IiwiYWRkIjoiMTQyLjQuMTAxLjEzNyIsInBvcnQiOiIyMDU2MSIsInR5cGUiOiJub25lIiwiaWQiOiJjZjNlYjEyNi1mZmJmLTQ0NTItOTFkZS03MzkzYjYwMjg3ODIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL25tTHVNMzROLyIsImhvc3QiOiJhd2Vpa2VqaS1Zb3VUdWJlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDAiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXNmcmVlMi5qaWFudGlhbi54eXoiLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@97.64.31.80:247#US_63
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDIiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9saXZlIiwiaG9zdCI6ImNjdHYuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDQiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTQzLjE5OC4xMzAuMjEiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57mtJvmnYnnn7ZQc3ljaHogTmV0d29ya3MgMTEiLCJhZGQiOiIxMDQuMTQ5LjE1NC4xNTQiLCJwb3J0IjoiMjU5NjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2EwNmUwZjAtY2E2ZS00MThmLTgwMGQtOTdiMjNiYTUxYmNhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9WVGQ0bzNLai8iLCJob3N0IjoiYXdlaWtlamktWW91VHViZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgxMTY0IiwiYWRkIjoidjEyNS52MmRucy5iYXIiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGM2OGFmOGEtOTYxYS0zMDY1LWEzYTctMTgwMGViYzcwYmRiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92MTI1Mk45M25aZXo2UHkiLCJob3N0IjoidjEyNS52MmRucy5iYXIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjQwIiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@97.64.31.80:247#US_63
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzYiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9pbmRleCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMt6auY6YCf6IqC54K55o6o6I2Q77yadjJjcm9zcy5jb20iLCJhZGQiOiJ2MTI1LnYyZG5zLmJhciIsInBvcnQiOiI4MCIsInR5cGUiOiJub25lIiwiaWQiOiIwYzY4YWY4YS05NjFhLTMwNjUtYTNhNy0xODAwZWJjNzBiZGIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3YxMjUyTjkzblplejZQeSIsImhvc3QiOiJ2MTI1LnYyZG5zLmJhciIsInRscyI6IiJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%E7%BE%8E%E5%9B%BD%28nodefree.org%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9%E6%97%A5%E6%9B%B4%29_2
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@172.245.218.162:809#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2067
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg1MTUiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzgiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9nbyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57mtJvmnYnnn7ZQc3ljaHogTmV0d29ya3MgMTEiLCJhZGQiOiIxMDQuMTQ5LjE1NC4xNTQiLCJwb3J0IjoiMjU5NjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2EwNmUwZjAtY2E2ZS00MThmLTgwMGQtOTdiMjNiYTUxYmNhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9WVGQ0bzNLai8iLCJob3N0IjoiYXdlaWtlamktWW91VHViZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiX+ayueeuoe+8muWFqOe9keacgOW8uueZveWrliIsImFkZCI6IjEwNC4xNDkuMTU0LjE1NCIsInBvcnQiOiIyNTk2NiIsInR5cGUiOiJub25lIiwiaWQiOiJjYTA2ZTBmMC1jYTZlLTQxOGYtODAwZC05N2IyM2JhNTFiY2EiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL1ZUZDRvM0tqLyIsImhvc3QiOiJhd2Vpa2VqaS1Zb3VUdWJlIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%E7%BE%8E%E5%9B%BD%28nodefree.org%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9%E6%97%A5%E6%9B%B4%29_2
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMt6auY6YCf6IqC54K55o6o6I2Q77yadjEubWsvdmlwIiwiYWRkIjoiMTA0LjIyNC4xODguMjkiLCJwb3J0IjoiMzgyMjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI5OWZiNzgtMjkwYy00YWFkLWJlZmItMDEzMGMwNzRhNjIyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1&sni=fhcarm1.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20US%2033%EF%BD%9Copenit.ml
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMt6auY6YCf6IqC54K55o6o6I2Q77yadjEubWsvdmlwIiwiYWRkIjoidjEyNS52MmRucy5iYXIiLCJwb3J0IjoiODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiMGM2OGFmOGEtOTYxYS0zMDY1LWEzYTctMTgwMGViYzcwYmRiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92MTI1Mk45M25aZXo2UHkiLCJob3N0IjoidjEyNS52MmRucy5iYXIiLCJ0bHMiOiIifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AF%F0%9F%87%B5%20%E7%BE%8E%E5%9B%BD%28nodefree.org%E5%85%8D%E8%B4%B9%E8%8A%82%E7%82%B9%E6%97%A5%E6%9B%B4%29_2
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbveWKoOWIqeemj+WwvOS6muW3nua0m+adieeftlBzeWNoeiBOZXR3b3JrcyAxMSIsImFkZCI6IjEwNC4xNDkuMTU0LjE1NCIsInBvcnQiOiIyNTk2NiIsInR5cGUiOiJub25lIiwiaWQiOiJjYTA2ZTBmMC1jYTZlLTQxOGYtODAwZC05N2IyM2JhNTFiY2EiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL1ZUZDRvM0tqLyIsImhvc3QiOiJhd2Vpa2VqaS1Zb3VUdWJlIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTU2NTIiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTQzLjE5OC4xMzAuMjEiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjA5IiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2020%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoiX+ayueeuoe+8muWFqOe9keacgOW8uueZveWrliIsImFkZCI6IjEwNC4xNDkuMTU0LjE1NCIsInBvcnQiOiIyNTk2NiIsInR5cGUiOiJub25lIiwiaWQiOiJjYTA2ZTBmMC1jYTZlLTQxOGYtODAwZC05N2IyM2JhNTFiY2EiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL1ZUZDRvM0tqLyIsImhvc3QiOiJhd2Vpa2VqaS1Zb3VUdWJlIiwidGxzIjoiIn0=
    trojan://s6rIg1Mkke73fwZU@tx-vip-10.top:443?allowInsecure=1&sni=tx-vip-10.top#TZ%201%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDAiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXNmcmVlMi5qaWFudGlhbi54eXoiLCJ0bHMiOiIifQ==
    trojan://1ac27c98-7883-483b-b958-7d6a68b60663@us-12.hmkj9.com:54321?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%204
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDMiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjM5IiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvSDhWc3d0VUovIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzciLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9xdGhhbmciLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzciLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9xdGhhbmciLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%203%EF%BD%9Copenit.ml
    trojan://UsW3MPZ8HF@tgchannel.kxswa.tk:19021?allowInsecure=1#unknown%2010%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTUyMjI5IiwiYWRkIjoiMTQzLjE5OC4xMzAuMjEiLCJwb3J0IjoiNDIzODIiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDNiNDUyYTctOTA3Yi00Zjc3LThjYTQtNjAyNTBjYzgzNWJjIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvY2hhdCIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTU2NjEiLCJhZGQiOiI2Ny4yMS43Mi40MSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjU2NmQwMGYtMjE4Yy00OGY3LTlhMzYtMTNkM2Q2ZjFhNzI0IiwiYWlkIjoiNjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvcGF0aC8xNzM0MTgxNDExMjMiLCJob3N0Ijoid3d3LjE3MDgwMTAwLnh5eiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgxMTU1IiwiYWRkIjoiMTQyLjQuMTAxLjEzNyIsInBvcnQiOiIyMDU2MSIsInR5cGUiOiJub25lIiwiaWQiOiJjZjNlYjEyNi1mZmJmLTQ0NTItOTFkZS03MzkzYjYwMjg3ODIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL25tTHVNMzROLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MCIsImFkZCI6IjE0My4xOTguMTMwLjIxIiwicG9ydCI6IjQyMzgyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzYjQ1MmE3LTkwN2ItNGY3Ny04Y2E0LTYwMjUwY2M4MzViYyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2Rpbmd6aSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=0#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjM3IiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%201%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDAiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoidXNmcmVlMi5qaWFudGlhbi54eXoiLCJ0bHMiOiIifQ==
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2019%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggbWF0dGtheWRpYXJ5LmNvbXznvo7lm70oVVMpVVNBL1Nhbkpvc2VfMjQiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://7dafe71e-2be6-302f-bdfc-e6319a3299bc@tj-us02.yiyodns.xyz:443?allowInsecure=1&sni=tj-us02.yiyodns.xyz#%F0%9F%87%BA%F0%9F%87%B8%20US%205%EF%BD%9Copenit.ml
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1&sni=fhcamd2.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2039
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2MzMiLCJhZGQiOiIyMDguOTguNDguMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@172.245.218.162:809#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2067
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTU2NTMiLCJhZGQiOiJpZXNlaTFlaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjQwIiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2OCIsImFkZCI6IjE0My4xOTguMTMwLjIxIiwicG9ydCI6IjQyMzgyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjAzYjQ1MmE3LTkwN2ItNGY3Ny04Y2E0LTYwMjUwY2M4MzViYyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgxMjE5IiwiYWRkIjoiaWVzZWkxZWkuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTg2NDIiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9saXZlIiwiaG9zdCI6ImNjdHYuY29tIiwidGxzIjoiIn0=
    trojan://a9f14424-7572-4fe2-bfa8-8864590ff295@cdn013.youxi.gay:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2043%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjM2IiwiYWRkIjoiNjcuMjEuNzIuNDEiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3BhdGgvMTczNDE4MTQxMTIzIiwiaG9zdCI6Ind3dy4xNzA4MDEwMC54eXoiLCJ0bHMiOiJ0bHMifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2015%EF%BD%9Copenit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MTgyMjM5IiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvSDhWc3d0VUovIiwiaG9zdCI6IiIsInRscyI6IiJ9

</details>

### 所有节点
合并节点总数: `6633`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `94`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `427`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `121`
- [freefq/free](https://github.com/freefq/free), 节点数量: `47`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `115`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `75`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `121`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3436`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `135`
- [iwxf/free-v2ray](https://github.com/iwxf/free-v2ray), 节点数量: `8`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `42`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `48`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `145`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `47`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `56`
- [tomdegnan/clashrule](https://github.com/tomdegnan/clashrule), 节点数量: `214`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `47`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `195`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `43`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `29`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `48`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `115`
- [poduv/poduv](https://github.com/poduv/poduv), 节点数量: `52`
- [ok1991/v2ray](https://github.com/ok1991/v2ray), 节点数量: `39`
- [parkerpa/jsfxs](https://github.com/parkerpa/jsfxs), 节点数量: `582`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `10`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `101`

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