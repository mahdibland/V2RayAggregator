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

    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA5OCIsImFkZCI6ImFhLmtheWFsby5jb20iLCJwb3J0IjoiMjYyNjciLCJ0eXBlIjoibm9uZSIsImlkIjoiOTc1N2NkYmEtYzc1Yi00Yjk0LTllMzEtNzk1NmRjN2Q4NTJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii93aXMiLCJob3N0IjoiYWEua2F5YWxvLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiYWEua2F5YWxvLmNvbSIsInBvcnQiOiIyNjI2NyIsInR5cGUiOiJub25lIiwiaWQiOiI5NzU3Y2RiYS1jNzViLTRiOTQtOWUzMS03OTU2ZGM3ZDg1MmEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3dpcyIsImhvc3QiOiJhYS5rYXlhbG8uY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU2MSB8NjkuNjhNYiIsImFkZCI6ImFhLmtheWFsby5jb20iLCJwb3J0IjoiMjYyNjciLCJ0eXBlIjoibm9uZSIsImlkIjoiOTc1N2NkYmEtYzc1Yi00Yjk0LTllMzEtNzk1NmRjN2Q4NTJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii93aXMiLCJob3N0IjoiYWEua2F5YWxvLmNvbSIsInRscyI6IiJ9
    trojan://e5d46365e25e31d94279c2bcf93390a2@usa-sr-105.mitoption.com:443?allowInsecure=0#github.com%2Fv2rayfree%20-%20%E7%BE%8E%E5%9B%BD%E4%BA%9A%E5%88%A9%E6%A1%91%E9%82%A3%E5%B7%9E%E6%96%AF%E7%A7%91%E8%8C%A8%E4%BB%A3%E5%B0%94%E5%B8%82Go%20Daddy%E9%9B%86%E5%9B%A2%E5%85%AC%E5%8F%B8%2019
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA2MiIsImFkZCI6ImFhLmtheWFsby5jb20iLCJwb3J0IjoiMjYyNjciLCJ0eXBlIjoibm9uZSIsImlkIjoiOTc1N2NkYmEtYzc1Yi00Yjk0LTllMzEtNzk1NmRjN2Q4NTJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii93aXMiLCJob3N0IjoiYWEua2F5YWxvLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiX0hLX+mmmea4r184IiwiYWRkIjoidXMxLmxvbHZwcy54eXoiLCJwb3J0IjoiNjAwNjAiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU4ODZjNzYtOTIwNy00OGJkLTllNjQtZDE0MjJlNzVhZDg5IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9BWTkyMFVNUiIsImhvc3QiOiJ1czEubG9sdnBzLnh5eiIsInRscyI6InRscyJ9
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US-Openit.ml
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US_2590%20%7C87.73Mb
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU5MyB8MzIuMjNNYiIsImFkZCI6ImFhLmtheWFsby5jb20iLCJwb3J0IjoiMjYyNjciLCJ0eXBlIjoibm9uZSIsImlkIjoiOTc1N2NkYmEtYzc1Yi00Yjk0LTllMzEtNzk1NmRjN2Q4NTJhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii93aXMiLCJob3N0IjoiYWEua2F5YWxvLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzM0MjciLCJhZGQiOiJhYS5rYXlhbG8uY29tIiwicG9ydCI6IjI2MjY3IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk3NTdjZGJhLWM3NWItNGI5NC05ZTMxLTc5NTZkYzdkODUyYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd2lzIiwiaG9zdCI6ImFhLmtheWFsby5jb20iLCJ0bHMiOiIifQ==
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US_2619%20%7C60.00Mb
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu95Yqg5Yip56aP5bC85Lqa5bee5rSb5p2J55+2SVQ3572R57ucIDciLCJhZGQiOiIxNDQuMTY4LjU2LjQ5IiwicG9ydCI6IjUwMzc3IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg0ZTM5ZThjLWNiZmMtNDFlMS1iYzVjLTdlZjE0NDEyZGFlMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InN4cXhqLmNuIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IiwiYWRkIjoiMTQ0LjE2OC41Ni40OSIsInBvcnQiOiI1MDM3NyIsInR5cGUiOiJub25lIiwiaWQiOiI4NGUzOWU4Yy1jYmZjLTQxZTEtYmM1Yy03ZWYxNDQxMmRhZTIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTQ0LjE2OC41Ni40OSIsInRscyI6IiJ9
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US-Openit.ml
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=0#Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_80
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=0#Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_85
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@172.245.218.162:809#%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2067
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US-Openit.ml
    trojan://e5d46365e25e31d94279c2bcf93390a2@o7cx6bd6t4yjiqsm.xiongsonglin.com:443?allowInsecure=1#US-Openit.ml
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US_2581%20%7C75.68Mb
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%209
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%209
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzUxIiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU1MyB8NDAuNTJNYiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_75
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY2MiB8MTI5LjgwTWIiLCJhZGQiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#github.com%2Fv2rayfree%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%209
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=0#github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2039
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#US_2639%20%7C78.19Mb
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#US-Openit.ml
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#US-Openit.ml
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDM@104.243.25.95:253#github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%209
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%2019
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiMTU1LjI0OC4yMDIuMjAzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY0OSB8NzcuMjhNYiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=1#NL_1072%20%7C40.13Mb
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiMTUwLjIzMC40My42NSIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiIxNTU2ZTA0MC0zMWQzLTRjNDctYjBkMi1kZGY4ODgwMTBiNGUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU2NyB8MTI0LjQ1TWIiLCJhZGQiOiJpZXNlaTFlaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoidGxzIn0=
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US_2700%20%7C77.61Mb
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiaWVzZWkxZWkuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9ICAzMCIsImFkZCI6IjE1NS4yNDguMjAyLjIwMyIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiI0YTBkYTM3OS1hN2NjLTQzODktODhkNy00NTUxNGI4OTY4ODMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJ2MnJheS43ODg2NDQueHl6IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiZ2l0aHViLmNvbS92MnJheWZyZWUgLSDnvo7lm73liqDliKnnpo/lsLzkuprlt57mtJvmnYnnn7ZJVDfnvZHnu5wgNyIsImFkZCI6IjE0NC4xNjguNTYuNDkiLCJwb3J0IjoiNTAzNzciLCJ0eXBlIjoibm9uZSIsImlkIjoiODRlMzllOGMtY2JmYy00MWUxLWJjNWMtN2VmMTQ0MTJkYWUyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIva0ZiNG53WFUiLCJob3N0IjoiMTA3LjE3NC4xNzIuMTU0IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY2MiB8MTI5LjgwTWIiLCJhZGQiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiMTUwLjIzMC40My42NSIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiIxNTU2ZTA0MC0zMWQzLTRjNDctYjBkMi1kZGY4ODgwMTBiNGUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii85UTJvZ2tPSy8iLCJob3N0IjoiNDUuMzIuNzcuMTAzIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IiwiYWRkIjoiMTU1LjI0OC4yMDIuMjAzIiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMGRhMzc5LWE3Y2MtNDM4OS04OGQ3LTQ1NTE0Yjg5Njg4MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIxNTUuMjQ4LjIwMi4yMDMiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiMTUwLjIzMC40My42NSIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiIxNTU2ZTA0MC0zMWQzLTRjNDctYjBkMi1kZGY4ODgwMTBiNGUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTA0LjE2OC4xMy44IiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJiYWktcGlhby13YW5nLXpoZS1pcGxjLjk4ODQ4Lnh5eiIsInBvcnQiOiIxMTQ1OSIsInR5cGUiOiJub25lIiwiaWQiOiI3ZWYxNTlhNy0yYzE1LTQ1Y2EtZjVjMy1iOTc5ODE0M2FmYWEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2JpdC5seS8zNmI2aUpoIiwiaG9zdCI6ImJhaS1waWFvLXdhbmctemhlLWlwbGMuOTg4NDgueHl6IiwidGxzIjoiIn0=
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1&sni=fhcamd2.gaox.ml#%28Youtube%E6%8A%80%E6%9C%AF%E5%88%86%E4%BA%AB%E5%AE%A4%29%F0%9F%87%BA%F0%9F%87%B8%E7%BE%8E%E5%9B%BD%2039
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA0MiIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVMt6auY6YCf6IqC54K56LSt5Lmw77yadjEubWsvdmlw77yI5rWP6KeI5Zmo5omT5byA77yJIiwiYWRkIjoiZG91YmFuLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvbW92aWVzIiwiaG9zdCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US-Openit.ml
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiMTg1LjIwMi4xNzIuMjQzIiwicG9ydCI6IjQwOTQxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ4NTM3ODIwLTE0ZjMtNGRlNy1kMjZlLWEzYjg4YmNmMDE1YSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6IjE1NC45NC4yMTQuMiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY3MyIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDEzMSIsImFkZCI6IjE1NS4yNDguMjAyLjIwMyIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiI0YTBkYTM3OS1hN2NjLTQzODktODhkNy00NTUxNGI4OTY4ODMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDExMiIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiQ0FfMzYxIHwxMjYuODhNYiIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiQ0FfMzE5IHwxNDkuNDJNYiIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVk4tT3Blbml0Lm1sIiwiYWRkIjoidXNhLWJ1ZmZhbG8ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU2MiB8MTA1LjMwTWIiLCJhZGQiOiIxODUuMjAyLjE3Mi4yNDMiLCJwb3J0IjoiNDA5NDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDg1Mzc4MjAtMTRmMy00ZGU3LWQyNmUtYTNiODhiY2YwMTVhIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd2lzIiwiaG9zdCI6ImFhLmtheWFsby5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA0NSIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=0#Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_97
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9XzI1NjYiLCJhZGQiOiIxNDQuMTY4LjU2LjQ5IiwicG9ydCI6IjUwMzc3IiwidHlwZSI6Im5vbmUiLCJpZCI6Ijg0ZTM5ZThjLWNiZmMtNDFlMS1iYzVjLTdlZjE0NDEyZGFlMiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU2OSB8MTA3Ljc2TWIiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVMiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjYxLjIyMi4yMDIuMTQwIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDE0MyIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoiMTg1LjIwMi4xNzIuMjQzIiwicG9ydCI6IjQwOTQxIiwidHlwZSI6Im5vbmUiLCJpZCI6IjQ4NTM3ODIwLTE0ZjMtNGRlNy1kMjZlLWEzYjg4YmNmMDE1YSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3F3ZSIsImhvc3QiOiI4LmV6eWRmZGQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzM0MzYiLCJhZGQiOiJpZXNlaTFlaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoiVVMiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiMTA0LjE2Ni4xMzUuMTAiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVMtT3Blbml0Lm1sIiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA3NiIsImFkZCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyNzg0ODczOS03ZTYyLTQxMzgtOWZkMy0wOThhNjM5NjRiNmIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL21vdmllcyIsImhvc3QiOiJkb3ViYW4uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDIxNiIsImFkZCI6IjE0NC4xNjguNTYuNDkiLCJwb3J0IjoiNTAzNzciLCJ0eXBlIjoibm9uZSIsImlkIjoiODRlMzllOGMtY2JmYy00MWUxLWJjNWMtN2VmMTQ0MTJkYWUyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA4NSIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY3MyB8MTUxLjUzTWIiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA5MiIsImFkZCI6IjE1NC45NC4yMTQuMiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJsdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjU3MCB8NTUuODNNYiIsImFkZCI6Imx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJsdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://sharecentre@ussc.scsevers.cf:443?allowInsecure=1#US-Openit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDA2NSIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAzOSIsImFkZCI6IjE5Mi4xODYuMTI5LjY2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9XzM0MTMiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiQ0FfMzQ5IHwxMTcuMzBNYiIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfMjY3MyIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDAzOCIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiWzA1LTA4XXxvc2xvb2t8576O5Zu9IiwiYWRkIjoiMTU1LjI0OC4yMDIuMjAzIiwicG9ydCI6IjE0NTY0IiwidHlwZSI6Im5vbmUiLCJpZCI6IjRhMGRhMzc5LWE3Y2MtNDM4OS04OGQ3LTQ1NTE0Yjg5Njg4MyIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3JheSIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5qyn5rSyIiwiYWRkIjoidXMtbnktcm4ubGljb20uZ2EiLCJwb3J0IjoiNjIwMDgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjgxZTk5MGUtMTI4My00OGY5LTllZmYtYWNhY2FkNmZiNjYxIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoidXMtbnktcm4ubGljb20uZ2EiLCJ0bHMiOiJ0bHMifQ==
    trojan://316b40c0-0dab-4ea1-9666-ac1658b033b2@s3.upyun.online:12340?allowInsecure=1#JP-Openit.ml
    trojan://316b40c0-0dab-4ea1-9666-ac1658b033b2@s3.upyun.online:12340?allowInsecure=0&sni=free.upyun.online#%E2%99%A5%EF%B8%8FYouTube%E6%A2%A6%E6%AD%8C%E2%99%A5%EF%B8%8F_8
    vmess://eyJ2IjoiMiIsInBzIjoiX1VTX+e+juWbvV8yMCIsImFkZCI6ImRvdWJhbi5iYWJhemh1amkuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyNzg0ODczOS03ZTYyLTQxMzgtOWZkMy0wOThhNjM5NjRiNmIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL21vdmllcyIsImhvc3QiOiJkb3ViYW4uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    trojan://f727337d-52af-4cf9-b260-26ac9a23ddc2@aling.gq:443?allowInsecure=0#Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_79
    vmess://eyJ2IjoiMiIsInBzIjoiZ2l0aHViLmNvbS92MnJheWZyZWUgLSDnvo7lm70gIDYzIiwiYWRkIjoiMTUwLjIzMC45Ni4xMDYiLCJwb3J0IjoiNTcyMzkiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRmMTU1YjgtMTBlMC00YTQ4LThiZmMtNmNlMmQ5ZjNmZjcyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://f727337d-52af-4cf9-b260-26ac9a23ddc2@aling.gq:443?allowInsecure=1#JP-Openit.ml
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIxNTUuMjQ4LjIwMi4yMDMiLCJwb3J0IjoiMTQ1NjQiLCJ0eXBlIjoibm9uZSIsImlkIjoiNGEwZGEzNzktYTdjYy00Mzg5LTg4ZDctNDU1MTRiODk2ODgzIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiMTU1LjI0OC4yMDIuMjAzIiwidGxzIjoiIn0=
    trojan://d06a3f01-1ff0-4792-9b8e-a5a604bc74a2@jgwdb4.gaox.ml:443?allowInsecure=1#AU_95%20%7C32.46Mb
    vmess://eyJ2IjoiMiIsInBzIjoi576O5Zu9IDEzOCIsImFkZCI6IjE1NS4yNDguMjAyLjIwMyIsInBvcnQiOiIxNDU2NCIsInR5cGUiOiJub25lIiwiaWQiOiI0YTBkYTM3OS1hN2NjLTQzODktODhkNy00NTUxNGI4OTY4ODMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii90bHMiLCJob3N0IjoiIiwidGxzIjoiIn0=

</details>

### 所有节点
合并节点总数: `7124`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `47`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `284`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `157`
- [freefq/free](https://github.com/freefq/free), 节点数量: `63`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `181`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `92`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `44`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `2962`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `430`
- [alanbobs999/TopFreeProxies](https://github.com/alanbobs999/TopFreeProxies), 节点数量: `99`
- [ldir92664/Vmess-Actions](https://github.com/ldir92664/Vmess-Actions), 节点数量: `144`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `42`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `139`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `145`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `63`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `153`
- [tomdegnan/clashrule](https://github.com/tomdegnan/clashrule), 节点数量: `214`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `69`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `197`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `274`
- [KYLELI1991/subscription_vless](https://github.com/KYLELI1991/subscription_vless), 节点数量: `0`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `38`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `63`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `32`
- [poduv/poduv](https://github.com/poduv/poduv), 节点数量: `47`
- [ok1991/v2ray](https://github.com/ok1991/v2ray), 节点数量: `134`
- [parkerpa/jsfxs](https://github.com/parkerpa/jsfxs), 节点数量: `582`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `28`
- [songkaik/Sub](https://github.com/songkaik/Sub), 节点数量: `104`
- [yosefwang/subscription](https://github.com/yosefwang/subscription), 节点数量: `17`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `127`

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