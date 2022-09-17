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

    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#mianfeifq%20%7C3.04%7CUSwmt915a11
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20042
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=s3.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%20%E7%BE%8E%E5%9B%BD_118%20%7C16.22Mb
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hass.win:12340?allowInsecure=1#2.24%7CUSwmt915a9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV8xNF8xMUAyNyIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoiYXV0byIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@35.92.36.222:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BDMerit%E7%BD%91%E7%BB%9C%E5%85%AC%E5%8F%B8%2032
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20026
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwMzQiLCJhZGQiOiJ2MjkuaGVkdWlhbi5vbmxpbmUiLCJwb3J0IjoiMzA4NjYiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2JiM2Y4NzctZDFmYi0zNDRjLTg3YTktZDE1M2JmZmQ1NDg0IiwiYWlkIjoiMiIsIm5ldCI6IndzIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6InYyOS5oZWR1aWFuLm9ubGluZSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiYWFhIDEzOSIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJhdXRvIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MTQwMDYiLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzQiLCJhZGQiOiJ3ZWl4aW4uYmFiYXpodWppLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjc4NDg3MzktN2U2Mi00MTM4LTlmZDMtMDk4YTYzOTY0YjZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii90ZWNoIiwiaG9zdCI6IndlaXhpbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hass.win:12340?allowInsecure=1&sni=s3.hass.win#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20027
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@144.168.58.170:254#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MTQwMDYiLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-156.146.38.163%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%201
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%202
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%202
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%2027%20%E2%86%92%20TG%40SCINV
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_13
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%202
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwiYWRkIjoid2VpeGluLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdGVjaCIsImhvc3QiOiJ3ZWl4aW4uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hass.win:12340?allowInsecure=1&sni=s3.hass.win#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MiIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9vb29vIiwiaG9zdCI6ImJhaWR1LmNvbSIsInRscyI6IiJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1#mianfeifq%20%7C1.62%7CUS395
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbveWKoOWIqeemj+WwvOS6muW3nua0m+adieeftklUN+e9kee7nCAzMyIsImFkZCI6ImJ3ZzIuZ3VzaGlkYXdhbmcuY2MiLCJwb3J0IjoiNTc1MzkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmNmNzIwMmMtYmQxYS00NGU5LWEyNWUtYmYxNTJmNmU1YzExIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiYndnMi5ndXNoaWRhd2FuZy5jYyIsInRscyI6IiJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20010
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1&sni=s1.hass.win#%F0%9F%87%BA%F0%9F%87%B8%20US%2036%20%E2%86%92%20TG%40SCINV
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%201%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoifDI1LjAzTWIiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MTQwMDciLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20TG%40SCINV
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20025
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2035%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MTQwMDYiLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-156.146.38.163%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hazz.win:12340?allowInsecure=1#aaa%20203
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%201
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20024
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDExIiwiYWRkIjoidXMwMi5nb2dvZ29vLmN5b3UiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZ28iLCJob3N0IjoidXMwMi5nb2dvZ29vLmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDExIiwiYWRkIjoidXMwMi5nb2dvZ29vLmN5b3UiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZ28iLCJob3N0IjoidXMwMi5nb2dvZ29vLmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2018%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzgiLCJhZGQiOiIyMy4yMzAuMTQ2LjI1NCIsInBvcnQiOiIxMjU4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVkZWI0MWNjLWE3NmEtNDdmMi1mYTk2LWI5MTQxZTY2YTJiMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imx2dWZ0LmNvbSIsInRscyI6IiJ9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS13ZWl4aW4uYmFiYXpodWppLmNvbSIsImFkZCI6IndlaXhpbi5iYWJhemh1amkuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJ2bWVzcyIsImlkIjoiMjc4NDg3MzktN2U2Mi00MTM4LTlmZDMtMDk4YTYzOTY0YjZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii90ZWNoIiwiaG9zdCI6IndlaXhpbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%206
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%203%20%E2%86%92%20TG%40SCINV
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%204
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1&sni=static.dingtalk.com#%F0%9F%87%BA%F0%9F%87%B8%20US%2037%20%E2%86%92%20TG%40SCINV
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@144.168.58.170:254#US_11
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%2027%20%E2%86%92%20TG%40SCINV
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hass.win:12340?allowInsecure=1&sni=s3.hass.win#%F0%9F%87%BA%F0%9F%87%B8%20US%2038%20%E2%86%92%20TG%40SCINV
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20018
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggLee+juWbvS0xNTAuMjMwLjQxLjkiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoidm1lc3MiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ3d3cuZmxpZXN3aW1pbmcudGsiLCJ0bHMiOiIifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=0#%7C23.78Mb
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#%7C23.90Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#aaa%20190
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#aaa%20351
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20042
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_08
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%201
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#aaa%20190
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzciLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzciLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%201
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MiIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@144.168.58.170:254#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20050
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%204
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvUNsb3VkRmxhcmXoioLngrkgMTEiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2OSIsImFkZCI6InY0LmhlZHVpYW4ub25saW5lIiwicG9ydCI6IjMwODY2IiwidHlwZSI6Im5vbmUiLCJpZCI6ImNiYjNmODc3LWQxZmItMzQ0Yy04N2E5LWQxNTNiZmZkNTQ4NCIsImFpZCI6IjIiLCJuZXQiOiJ3cyIsInBhdGgiOiIvb29vbyIsImhvc3QiOiJiYWlkdS5jb20iLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%201
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%204
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20US%E3%80%90%E4%BB%98%E8%B4%B9%E6%8E%A8%E8%8D%90%EF%BC%9Agvip.gq%E3%80%91
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MCIsImFkZCI6InYyOS5oZWR1aWFuLm9ubGluZSIsInBvcnQiOiIzMDg2NiIsInR5cGUiOiJub25lIiwiaWQiOiJjYmIzZjg3Ny1kMWZiLTM0NGMtODdhOS1kMTUzYmZmZDU0ODQiLCJhaWQiOiIyIiwibmV0Ijoid3MiLCJwYXRoIjoiL29vb28iLCJob3N0IjoiYmFpZHUuY29tIiwidGxzIjoiIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_08
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%205%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzYiLCJhZGQiOiIyMy4yMzAuMTQ2LjI1NCIsInBvcnQiOiIxMjU4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVkZWI0MWNjLWE3NmEtNDdmMi1mYTk2LWI5MTQxZTY2YTJiMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3BhdGgvMjczMjEzMDcwOTMzIiwiaG9zdCI6IjUxLjE5NS4zNS4xMzQiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20_US_%E7%BE%8E%E5%9B%BD
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%205%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3REWmNDcWMiLCJob3N0IjoiZ2NmcmVlMS5nYWxheHktY2xvdWQuaWN1IiwidGxzIjoiIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hazz.win:12340?allowInsecure=1#aaa%20203
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NiIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvcGF0aC8xNzM0MTgxNDExMjMiLCJob3N0Ijoid3d3LjE3MDgwMTAwLnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MTQwNzMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-156.146.38.163%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20025
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=0#Relay_%20%7C22.77Mb

</details>

### 所有节点
合并节点总数: `6176`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `150`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `127`
- [freefq/free](https://github.com/freefq/free), 节点数量: `34`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `193`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `183`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3293`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `121`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `21`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `18`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `34`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `39`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `212`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `75`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `29`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `35`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `637`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `10`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `29`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub - SSR](https://github.com/Rokate/Proxy-Sub), 节点数量: `436`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `169`

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