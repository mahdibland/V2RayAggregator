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

    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIxNDMuMTk4LjEzMC4yMSIsInBvcnQiOiI0MjM4MiIsInR5cGUiOiJub25lIiwiaWQiOiIwM2I0NTJhNy05MDdiLTRmNzctOGNhNC02MDI1MGNjODM1YmMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTQzLjE5OC4xMzAuMjEiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NCIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiIxMjgyNCIsInR5cGUiOiJub25lIiwiaWQiOiJjZTQ5YjAzYS1lYzM2LTRhZmQtZDZmMS1mNjc4YWQzN2NiYjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii94eFgxIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV85IiwiYWRkIjoiMTQzLjExMC4xNDUuMzMiLCJwb3J0IjoiMTIzMTUiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjMyOTdjMzktM2U2OS00ZmQwLTg2MzItZGE0YzcwOGYxMzlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDAiLCJhZGQiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJwb3J0IjoiMzE5NjEiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTQzMTFlNzEtOTEyNS00YmQxLWZhYTItNTE1YTg2NjdjNDg2IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii95b3V0dWJ0QOeZveWrlueOi+iAhSIsImhvc3QiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDgxMDI3IiwiYWRkIjoiMTQzLjExMC4xNDUuMzMiLCJwb3J0IjoiMTIzMTUiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjMyOTdjMzktM2U2OS00ZmQwLTg2MzItZGE0YzcwOGYxMzlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYxMTA0IiwiYWRkIjoiYmFpLXBpYW8td2FuZy16aGUtaXBsYzYuOTg4NDgueHl6IiwicG9ydCI6IjMxOTYxIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk0MzExZTcxLTkxMjUtNGJkMS1mYWEyLTUxNWE4NjY3YzQ4NiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIveW91dHVidEDnmb3lq5bnjovogIUiLCJob3N0IjoiYmFpLXBpYW8td2FuZy16aGUtaXBsYzYuOTg4NDgueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDY2NjYiLCJhZGQiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJwb3J0IjoiMzE5NjEiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTQzMTFlNzEtOTEyNS00YmQxLWZhYTItNTE1YTg2NjdjNDg2IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii95b3V0dWJ0QOeZveWrlueOi+iAhSIsImhvc3QiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5OSIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiIxMjgyNCIsInR5cGUiOiJub25lIiwiaWQiOiJjZTQ5YjAzYS1lYzM2LTRhZmQtZDZmMS1mNjc4YWQzN2NiYjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii95b3V0dWJ0QOeZveWrlueOi+iAhSIsImhvc3QiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NiIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiIzMTk2MSIsInR5cGUiOiJub25lIiwiaWQiOiI5NDMxMWU3MS05MTI1LTRiZDEtZmFhMi01MTVhODY2N2M0ODYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3lvdXR1YnRA55m95auW546L6ICFIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NSIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiI1OTk1OSIsInR5cGUiOiJub25lIiwiaWQiOiJmN2QyNmI1ZS04ZDc4LTQxNTQtODViNi1kNjllYThkZWEwZWEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3lvdXR1YnRA55m95auW546L6ICFIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5OCIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiI1OTk1OSIsInR5cGUiOiJub25lIiwiaWQiOiJmN2QyNmI1ZS04ZDc4LTQxNTQtODViNi1kNjllYThkZWEwZWEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3lvdXR1YnRA55m95auW546L6ICFIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYxMTA0IiwiYWRkIjoiYmFpLXBpYW8td2FuZy16aGUtaXBsYzYuOTg4NDgueHl6IiwicG9ydCI6IjMxOTYxIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk0MzExZTcxLTkxMjUtNGJkMS1mYWEyLTUxNWE4NjY3YzQ4NiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIveW91dHVidEDnmb3lq5bnjovogIUiLCJob3N0IjoiYmFpLXBpYW8td2FuZy16aGUtaXBsYzYuOTg4NDgueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDY2NjYiLCJhZGQiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJwb3J0IjoiMzE5NjEiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTQzMTFlNzEtOTEyNS00YmQxLWZhYTItNTE1YTg2NjdjNDg2IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii95b3V0dWJ0QOeZveWrlueOi+iAhSIsImhvc3QiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hs/Cfh7Eg6I235YWwIDAwMiIsImFkZCI6IjQ1LjE1MC4xNjUuOTciLCJwb3J0IjoiMjAwODMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEyOGMxMjEtN2I1Yi00MWJjLThhNjYtMTJmM2ZhOGNlNDIyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDExNCIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiIxMjgyNCIsInR5cGUiOiJub25lIiwiaWQiOiJjZTQ5YjAzYS1lYzM2LTRhZmQtZDZmMS1mNjc4YWQzN2NiYjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDkiLCJhZGQiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJwb3J0IjoiMTI4MjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2U0OWIwM2EtZWMzNi00YWZkLWQ2ZjEtZjY3OGFkMzdjYmI3IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1MCIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzOSIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20US-%E9%AB%98%E9%80%9F%E8%8A%82%E7%82%B9%E6%8E%A8%E8%8D%90%EF%BC%9Av1.mk%2Fvip
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NjEiLCJhZGQiOiIxNTAuMjMwLjQzLjEwNiIsInBvcnQiOiI1NDgyOSIsInR5cGUiOiJub25lIiwiaWQiOiJmMmI1YzNmZi04NmM3LTRlZmEtODMxZi1mZjBmY2Q3NjU2YTUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTUwLjIzMC40My4xMDYiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDExNyIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiIxMjgyNCIsInR5cGUiOiJub25lIiwiaWQiOiJjZTQ5YjAzYS1lYzM2LTRhZmQtZDZmMS1mNjc4YWQzN2NiYjciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii95b3V0dWJ0QOeZveWrlueOi+iAhSIsImhvc3QiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjNi45ODg0OC54eXoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDgiLCJhZGQiOiI0NS4xNTAuMTY1Ljk3IiwicG9ydCI6IjIwMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMjhjMTIxLTdiNWItNDFiYy04YTY2LTEyZjNmYThjZTQyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg5OTYiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20US-%E9%AB%98%E9%80%9F%E8%8A%82%E7%82%B9%E6%8E%A8%E8%8D%90%EF%BC%9Av1.mk%2Fvip
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDYiLCJhZGQiOiJ1czIuYXNhc2FzLnRvcCIsInBvcnQiOiIxODExNyIsInR5cGUiOiJub25lIiwiaWQiOiI4MGVmYTcxYi1hMTY0LTMwNTctYmRmZC1lZDI4NTIxMjU2ZmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3YycmF5IiwiaG9zdCI6InVzMi5hc2FzYXMudG9wIiwidGxzIjoidGxzIn0=
    trojan://8e4f0531-7a90-4429-b048-67a19c010c40@45.88.148.234:38443?allowInsecure=0&sni=huayun.xyz#%F0%9F%87%BA%F0%9F%87%B8%20US-%E9%AB%98%E9%80%9F%E8%8A%82%E7%82%B9%E6%8E%A8%E8%8D%90%EF%BC%9Av1.mk%2Fvip
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzMyIsImFkZCI6InVzMi5hc2FzYXMudG9wIiwicG9ydCI6IjE4MTE3IiwidHlwZSI6Im5vbmUiLCJpZCI6IjgwZWZhNzFiLWExNjQtMzA1Ny1iZGZkLWVkMjg1MjEyNTZmZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdjJyYXkiLCJob3N0IjoidXMyLmFzYXNhcy50b3AiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5NyIsImFkZCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInBvcnQiOiIzMTk2MSIsInR5cGUiOiJub25lIiwiaWQiOiI5NDMxMWU3MS05MTI1LTRiZDEtZmFhMi01MTVhODY2N2M0ODYiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3lvdXR1YnRA55m95auW546L6ICFIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGM2Ljk4ODQ4Lnh5eiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3OCIsImFkZCI6IjE1MC4yMzAuNDMuMTA2IiwicG9ydCI6IjU0ODI5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImYyYjVjM2ZmLTg2YzctNGVmYS04MzFmLWZmMGZjZDc2NTZhNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3lvdXR1YnRA55m95auW546L6ICFIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NTgiLCJhZGQiOiIxNTAuMjMwLjQzLjEwNiIsInBvcnQiOiI1NDgyOSIsInR5cGUiOiJub25lIiwiaWQiOiJmMmI1YzNmZi04NmM3LTRlZmEtODMxZi1mZjBmY2Q3NjU2YTUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9IOFZzd3RVSi8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDgwNTAiLCJhZGQiOiI0NS4xNTAuMTY1Ljk3IiwicG9ydCI6IjIwMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMjhjMTIxLTdiNWItNDFiYy04YTY2LTEyZjNmYThjZTQyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDQiLCJhZGQiOiIyMDguOTguNDguMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MSIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2MzUiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDgxNzIwIiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIveW91dHVidEDnmb3lq5bnjovogIUiLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDMiLCJhZGQiOiJpZXNlaTFlaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoidGxzIn0=
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1&sni=fhcamd2.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2039
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggWzA2LTA4XXxvc2xvb2t8576O5Zu9KFVTKVVTQS9TYW5Kb3NlXzEzIiwiYWRkIjoiMTU1LjI0OC4yMDIuMjAzIiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMGRhMzc5LWE3Y2MtNDM4OS04OGQ3LTQ1NTE0Yjg5Njg4MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyMSIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NTIiLCJhZGQiOiI0NS4xNTAuMTY1Ljk3IiwicG9ydCI6IjIwMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMjhjMTIxLTdiNWItNDFiYy04YTY2LTEyZjNmYThjZTQyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL2t2dzA4NzBoLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDciLCJhZGQiOiIxNTAuMjMwLjQzLjEwNiIsInBvcnQiOiI1NDgyOSIsInR5cGUiOiJub25lIiwiaWQiOiJmMmI1YzNmZi04NmM3LTRlZmEtODMxZi1mZjBmY2Q3NjU2YTUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NTQiLCJhZGQiOiI0NS4xNTAuMTY1Ljk3IiwicG9ydCI6IjIwMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMjhjMTIxLTdiNWItNDFiYy04YTY2LTEyZjNmYThjZTQyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3YycmF5IiwiaG9zdCI6InJ1MS5saXhpYW9sb25nLmJ1enoiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbveWKoOWIqeemj+WwvOS6muW3nua0m+adieeftkRNSVTmlbDmja7kuK3lv4MgMTAiLCJhZGQiOiJ1czIuYXNhc2FzLnRvcCIsInBvcnQiOiIxODExNyIsInR5cGUiOiJub25lIiwiaWQiOiI4MGVmYTcxYi1hMTY0LTMwNTctYmRmZC1lZDI4NTIxMjU2ZmUiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3YycmF5IiwiaG9zdCI6InVzMi5hc2FzYXMudG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NTEiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4NSIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MSIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NTMiLCJhZGQiOiI0NS4xNTAuMTY1Ljk3IiwicG9ydCI6IjIwMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMjhjMTIxLTdiNWItNDFiYy04YTY2LTEyZjNmYThjZTQyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLzE3YWY3NmUxLWE1ZDctNDFhYi1hZTg3LWI0OGYxODUwNzVkMS12bWVzcyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYwNTEiLCJhZGQiOiI0NS4xNTAuMTY1Ljk3IiwicG9ydCI6IjIwMDgzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMjhjMTIxLTdiNWItNDFiYy04YTY2LTEyZjNmYThjZTQyMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NTUiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDY3MjkiLCJhZGQiOiIxNTAuMjMwLjQzLjEwNiIsInBvcnQiOiI1NDgyOSIsInR5cGUiOiJub25lIiwiaWQiOiJmMmI1YzNmZi04NmM3LTRlZmEtODMxZi1mZjBmY2Q3NjU2YTUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp4Q2pteEd6clVvQkE@37.218.241.43:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-37.218.241.43%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%BB%85%E6%94%AF%E6%8C%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDg2NDUiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzNSIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggWzA2LTA4XXxvc2xvb2t8576O5Zu9KFVTKVVTQS9TYW5Kb3NlXzI0IiwiYWRkIjoiMTU1LjI0OC4yMDIuMjAzIiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMGRhMzc5LWE3Y2MtNDM4OS04OGQ3LTQ1NTE0Yjg5Njg4MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwMCIsImFkZCI6IjE1MC4yMzAuNDMuMTA2IiwicG9ydCI6IjU0ODI5IiwidHlwZSI6Im5vbmUiLCJpZCI6ImYyYjVjM2ZmLTg2YzctNGVmYS04MzFmLWZmMGZjZDc2NTZhNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3lvdXR1YnRA55m95auW546L6ICFIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggbWF0dGtheWRpYXJ5LmNvbXznvo7lm70oVVMpVVNBL1Nhbkpvc2VfMTMiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyMCIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2MCIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAyMyIsImFkZCI6InU0LmFubXUub25lIiwicG9ydCI6IjE2MTk5IiwidHlwZSI6Im5vbmUiLCJpZCI6IjA3ZWM1OWRhLTE4YWQtNDIyNC04YWQ5LWM1YTY2YjE0NDdhOSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIzNC4yMTUuMTMwLjE4NiIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MCIsImFkZCI6InUyLmFubXUub25lIiwicG9ydCI6IjE2MTYxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkxOWFjODE1LTE3NzYtNDdmZS04YjU0LTUwOGVmNGYzOTQyMSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYxNzU1IiwiYWRkIjoiNDUuMTUwLjE2NS45NyIsInBvcnQiOiIyMDA4MyIsInR5cGUiOiJub25lIiwiaWQiOiI0YTI4YzEyMS03YjViLTQxYmMtOGE2Ni0xMmYzZmE4Y2U0MjIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii92MnJheSIsImhvc3QiOiJydTEubGl4aWFvbG9uZy5idXp6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJraXJha2lyYXNldmVubmluZS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY3MDY4ODEyLTBmNmMtNDM3ZS1hYjEzLWY0ODBmMjNiZjAwNCIsImFpZCI6IjEzIiwibmV0Ijoid3MiLCJwYXRoIjoiLzlmMjEvIiwiaG9zdCI6ImtpcmFraXJhc2V2ZW5uaW5lLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysIDAwOCIsImFkZCI6IjEzOS4xNjIuMTIyLjI0MCIsInBvcnQiOiI2NjE3IiwidHlwZSI6Im5vbmUiLCJpZCI6IjBkN2NmNWJmLWNiZGUtNDBiNC1hYTk0LWY5MjdlMTFkMjgzZiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEzOS4xNjIuMTIyLjI0MCIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysIDAxMiIsImFkZCI6ImtpcmFraXJhc2V2ZW5uaW5lLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNjcwNjg4MTItMGY2Yy00MzdlLWFiMTMtZjQ4MGYyM2JmMDA0IiwiYWlkIjoiMTMiLCJuZXQiOiJ3cyIsInBhdGgiOiIvOWYyMS8iLCJob3N0Ijoia2lyYWtpcmFzZXZlbm5pbmUuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgzMTIiLCJhZGQiOiIxMzkuMTYyLjEyMi4yNDAiLCJwb3J0IjoiNjYxNyIsInR5cGUiOiJub25lIiwiaWQiOiIwZDdjZjViZi1jYmRlLTQwYjQtYWE5NC1mOTI3ZTExZDI4M2YiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiIxMzkuMTYyLjEyMi4yNDAiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgwNjYiLCJhZGQiOiJraXJha2lyYXNldmVubmluZS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjY3MDY4ODEyLTBmNmMtNDM3ZS1hYjEzLWY0ODBmMjNiZjAwNCIsImFpZCI6IjEzIiwibmV0Ijoid3MiLCJwYXRoIjoiLzlmMjEvIiwiaG9zdCI6ImtpcmFraXJhc2V2ZW5uaW5lLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NCIsImFkZCI6InVzMi5hc2FzYXMudG9wIiwicG9ydCI6IjE4MTE3IiwidHlwZSI6Im5vbmUiLCJpZCI6IjgwZWZhNzFiLWExNjQtMzA1Ny1iZGZkLWVkMjg1MjEyNTZmZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdjJyYXkiLCJob3N0IjoidXMyLmFzYXNhcy50b3AiLCJ0bHMiOiJ0bHMifQ==
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1&sni=fhcamd2.gaox.ml#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2039
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@172.245.218.162:809#%F0%9F%87%BA%F0%9F%87%B8%20%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2067
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDgxMjIyIiwiYWRkIjoiNzIuNDQuNjkuNzMiLCJwb3J0IjoiNTA2NTYiLCJ0eXBlIjoibm9uZSIsImlkIjoiMmMyNjk3NzgtMDg4NC0xMWVjLWFmNzctMDAxNjNjOTdjZGU4IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9wb09YZm1rOC8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysIDAwMSIsImFkZCI6InZqcDMuMGJhZC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjkyNzA5NGQzLWQ2NzgtNDc2My04NTkxLWUyNDBkMGJjYWU4NyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2hhdCIsImhvc3QiOiJ2anAzLjBiYWQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysKOayueeuoTrnoLTop6PotYTmupDlkJsyLjApIiwiYWRkIjoidmpwMy4wYmFkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZqcDMuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://e1cb3dc5-4855-44e9-ae18-647dc443674e@vesta.jp.v4.hdsky.org:443?allowInsecure=0&sni=vesta.jp.v4.e1dns.com#JP3
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp4Q2pteEd6clVvQkE@37.218.241.43:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-37.218.241.43%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%BB%85%E6%94%AF%E6%8C%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYxMzA5IiwiYWRkIjoidTQuYW5tdS5vbmUiLCJwb3J0IjoiMTYxOTkiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDdlYzU5ZGEtMThhZC00MjI0LThhZDktYzVhNjZiMTQ0N2E5IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidTQuYW5tdS5vbmUiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysLTE1Ljg5TUIvcyhZb3V0dWJlOuS4jeiJr+aelykiLCJhZGQiOiJ2anAxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmpwMS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJ2anAxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmpwMS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgwNzIiLCJhZGQiOiJ2anAxLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmpwMS4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgxNTEiLCJhZGQiOiJ2anAzLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmpwMy4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDgxNjg0IiwiYWRkIjoidnVzMi4wYmFkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZ1czIuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDgxMTc1IiwiYWRkIjoidnVzMy4wYmFkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZ1czMuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgxNjQiLCJhZGQiOiIxNTUuMjQ4LjE2Mi4yMSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQ1NDA5N2YtMTVmYi00NGJiLTllNTktZTFmZGQxYWMwM2E1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDY3ODAiLCJhZGQiOiIxNTAuMjMwLjQzLjEwNiIsInBvcnQiOiI1NDgyOSIsInR5cGUiOiJub25lIiwiaWQiOiJmMmI1YzNmZi04NmM3LTRlZmEtODMxZi1mZjBmY2Q3NjU2YTUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTUwLjIzMC40My4xMDYiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgzMjgiLCJhZGQiOiIxNTUuMjQ4LjE2Mi4yMSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQ1NDA5N2YtMTVmYi00NGJiLTllNTktZTFmZGQxYWMwM2E1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvaW5kZXgiLCJob3N0Ijoid3d3LmJhaWR1LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvV8xIiwiYWRkIjoidXMyLmFzYXNhcy50b3AiLCJwb3J0IjoiMTgxMTciLCJ0eXBlIjoibm9uZSIsImlkIjoiODBlZmE3MWItYTE2NC0zMDU3LWJkZmQtZWQyODUyMTI1NmZlIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii92MnJheSIsImhvc3QiOiJ1czIuYXNhc2FzLnRvcCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MyIsImFkZCI6IjE1NS4yNDguMTYyLjIxIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI3NDU0MDk3Zi0xNWZiLTQ0YmItOWU1OS1lMWZkZDFhYzAzYTUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgwNTIiLCJhZGQiOiIxNTUuMjQ4LjE2Mi4yMSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQ1NDA5N2YtMTVmYi00NGJiLTllNTktZTFmZGQxYWMwM2E1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgyOTUiLCJhZGQiOiIxNTUuMjQ4LjE2Mi4yMSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNzQ1NDA5N2YtMTVmYi00NGJiLTllNTktZTFmZGQxYWMwM2E1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvbWciLCJob3N0IjoiL3QubWUvbmZlbmc2IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NCIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYxMjUxIiwiYWRkIjoiNDUuMTUwLjE2NS45NyIsInBvcnQiOiIyMDA4MyIsInR5cGUiOiJub25lIiwiaWQiOiI0YTI4YzEyMS03YjViLTQxYmMtOGE2Ni0xMmYzZmE4Y2U0MjIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA2MDYxMTg5IiwiYWRkIjoiMTUwLjIzMC40My4xMDYiLCJwb3J0IjoiNTQ4MjkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjJiNWMzZmYtODZjNy00ZWZhLTgzMWYtZmYwZmNkNzY1NmE1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgzMjUiLCJhZGQiOiIxNTIuNzAuODcuMTgxIiwicG9ydCI6IjU5NDM4IiwidHlwZSI6Im5vbmUiLCJpZCI6IjI4Mzk5MTM5LWExOGQtNGI4Ny1iMTI3LWFjNGRmMWE5ODZjYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjE1Mi43MC44Ny4xODEiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzNCIsImFkZCI6IjE1Mi43MC44Ny4xODEiLCJwb3J0IjoiNTk0MzgiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjgzOTkxMzktYTE4ZC00Yjg3LWIxMjctYWM0ZGYxYTk4NmNiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTUyLjcwLjg3LjE4MSIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@78.129.253.9:809#%F0%9F%87%AC%F0%9F%87%A7%20GB%E8%8B%B1%E5%9B%BD%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%2016
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@78.129.253.9:809#%F0%9F%87%AC%F0%9F%87%A7%20GB%E8%8B%B1%E5%9B%BD%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%2016
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgyOTgiLCJhZGQiOiIxNTAuMjMwLjIwOS4xMzgiLCJwb3J0IjoiMTg3NTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiMzA2ODExNTAtNGIyMi00ODA5LTlmZDktMmZlMjg5YTljZDlmIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgwNTQiLCJhZGQiOiIxNTIuNzAuODcuMTgxIiwicG9ydCI6IjU5NDM4IiwidHlwZSI6Im5vbmUiLCJpZCI6IjI4Mzk5MTM5LWExOGQtNGI4Ny1iMTI3LWFjNGRmMWE5ODZjYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA2MDgzMjciLCJhZGQiOiIxMzguMi4xNS4yMyIsInBvcnQiOiI0NjM3MCIsInR5cGUiOiJub25lIiwiaWQiOiI5OTgxNTFlNS0wYmM1LTQzNzctZTM5MC1jNDFiYjI2ZmRkMGMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9pbmRleCIsImhvc3QiOiJ3d3cuYmFpZHUuY29tIiwidGxzIjoiIn0=

</details>

### 所有节点
合并节点总数: `5536`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `48`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `174`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `130`
- [freefq/free](https://github.com/freefq/free), 节点数量: `25`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `60`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `11`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `57`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `2757`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `99`
- [iwxf/free-v2ray](https://github.com/iwxf/free-v2ray), 节点数量: `8`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `42`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `48`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `145`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `25`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `56`
- [tomdegnan/clashrule](https://github.com/tomdegnan/clashrule), 节点数量: `214`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `87`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `167`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `50`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `18`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `26`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `172`
- [poduv/poduv](https://github.com/poduv/poduv), 节点数量: `148`
- [ok1991/v2ray](https://github.com/ok1991/v2ray), 节点数量: `39`
- [parkerpa/jsfxs](https://github.com/parkerpa/jsfxs), 节点数量: `582`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `6`
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