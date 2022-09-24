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

    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_09
    vmess://eyJ2IjoiMiIsInBzIjoiUmVsYXlfIHwzOC4xMk1iIiwiYWRkIjoiZGFsMi4zMzIwLnRvcCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmVmZmJjZGYtNDBkNC00OWNjLWE4ZDMtOWZhODg3MmM1MGM0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZGFsMi4zMzIwLnRvcCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDIwIiwiYWRkIjoiZGFsMi4zMzIwLnRvcCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmVmZmJjZGYtNDBkNC00OWNjLWE4ZDMtOWZhODg3MmM1MGM0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZGFsMi4zMzIwLnRvcCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvUNsb3VkRmxhcmXoioLngrkgMjAiLCJhZGQiOiJkYWwyLjMzMjAudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJmZWZmYmNkZi00MGQ0LTQ5Y2MtYThkMy05ZmE4ODcyYzUwYzQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJkYWwyLjMzMjAudG9wIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDIwIiwiYWRkIjoiZGFsMi4zMzIwLnRvcCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZmVmZmJjZGYtNDBkNC00OWNjLWE4ZDMtOWZhODg3MmM1MGM0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZGFsMi4zMzIwLnRvcCIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJkYWwyLjMzMjAudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJmZWZmYmNkZi00MGQ0LTQ5Y2MtYThkMy05ZmE4ODcyYzUwYzQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJkYWwyLjMzMjAudG9wIiwidGxzIjoidGxzIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=0#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_1306%20%7C16.27Mb
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2025%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NyIsImFkZCI6ImRhbDIuMzMyMC50b3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZlZmZiY2RmLTQwZDQtNDljYy1hOGQzLTlmYTg4NzJjNTBjNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImRhbDIuMzMyMC50b3AiLCJ0bHMiOiJ0bHMifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hass.win:12340?allowInsecure=1#mianfeifq%20295
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hass.win:12340?allowInsecure=1#%E7%99%BD%E5%AB%96-074
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#mianfeifq%20354
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2010%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hazz.win:12340?allowInsecure=1#aaa%20177
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@165.232.140.49:12340?allowInsecure=1#mianfeifq%20%7CUS_165.232.140.49_0924d110-71
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%208%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@165.232.137.2:12340?allowInsecure=1#US_165.232.137.2_0924d110-62
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hazz.win:12340?allowInsecure=1&sni=s4.hazz.win#%F0%9F%87%A9%F0%9F%87%AA%20DE%2027
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2012%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMjEt5LuY6LS55o6o6I2QOnN1by55dC9zc3JzdWIiLCJhZGQiOiI2OC4xODMuMTI5LjE5NyIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiNjguMTgzLjEyOS4xOTciLCJ0bHMiOiIifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#mianfeifq%20%7C3.26%7CUSwmt92135
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hazz.win:12340?allowInsecure=1#mianfeifq%20246
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hazz.win:12340?allowInsecure=1&sni=s2.hazz.win#%F0%9F%87%A9%F0%9F%87%AA%20DE%2022
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9LXRn6aKR6YGTOkBicGp6eDItNDMiLCJhZGQiOiI2OC4xODMuMTI5LjE5NyIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiNjguMTgzLjEyOS4xOTciLCJ0bHMiOiIifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2020%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDQ3IiwiYWRkIjoiYXJtLnB0dXUuZ3EiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk4MjFiODE3LTVjYjAtNGFmMy1hM2UzLTdjMTM3ODUwOTM1ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImFybS5wdHV1LmdxIiwidGxzIjoidGxzIn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2020%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwMjMiLCJhZGQiOiJkYWwyLjMzMjAudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJmZWZmYmNkZi00MGQ0LTQ5Y2MtYThkMy05ZmE4ODcyYzUwYzQiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJkYWwyLjMzMjAudG9wIiwidGxzIjoidGxzIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@143.198.61.45:12340?allowInsecure=1#mianfeifq%20%7CUS_143.198.61.45_0924d110-55
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJmcm0xLjMzMjAudG9wIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIxNWViZjgyYS1kZDNhLTQ1MTktOWE4OS00ZTYwODU4ZDQ3YWIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJmcm0xLjMzMjAudG9wIiwidGxzIjoidGxzIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%207%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMjEt5LuY6LS55o6o6I2QOnN1by55dC9zc3JzdWIiLCJhZGQiOiI2OC4xODMuMTI5LjE5NyIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiNjguMTgzLjEyOS4xOTciLCJ0bHMiOiIifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=s3.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%20%E7%BE%8E%E5%9B%BD_118%20%7C16.22Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgfDM3LjEyTWIiLCJhZGQiOiIyMy4yMzAuMTQ2LjI1NCIsInBvcnQiOiIxMjU4IiwidHlwZSI6ImF1dG8iLCJpZCI6ImVkZWI0MWNjLWE3NmEtNDdmMi1mYTk2LWI5MTQxZTY2YTJiMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=0#Relay_%20%7C15.97Mb
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2012%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMgMjE0IiwiYWRkIjoiMTU4LjEwMS4xOS4xNzIiLCJwb3J0IjoiMTA5MTAiLCJ0eXBlIjoiaHR0cCIsImlkIjoiMjQxNjQ1ZjUtMzE5MC00MjliLWI1MTMtNTI2NWEyNDJkZmUxIiwiYWlkIjoiMCIsIm5ldCI6Imh0dHAiLCJwYXRoIjoiLyIsImhvc3QiOiIxNTguMTAxLjE5LjE3MiIsInRscyI6IiJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hass.win:12340?allowInsecure=1&sni=s2.hass.win#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNjMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2035%20%E2%86%92%20openitsub.com
    trojan://8c836caa-3d53-4829-bcfb-cbe0aa453a57@23.94.103.146:443?allowInsecure=1#mianfeifq%20321
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%201
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MjIwMDUiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hass.win:12340?allowInsecure=1#%E7%99%BD%E5%AB%96-130
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%208%20%E2%86%92%20v2cross.com
    vmess://eyJ2IjoiMiIsInBzIjoiUmVsYXlfIHwxMS4yMk1iIiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%203%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNjMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwMyIsImFkZCI6ImZybTEuMzMyMC50b3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjE1ZWJmODJhLWRkM2EtNDUxOS05YTg5LTRlNjA4NThkNDdhYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImZybTEuMzMyMC50b3AiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%207
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiI2OC4xODMuMTI5LjE5NyIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiNjguMTgzLjEyOS4xOTciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvUNsb3VkRmxhcmXlhazlj7hDRE7oioLngrkgNDciLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@144.126.211.35:12340?allowInsecure=1#mianfeifq%20%7CUS_144.126.211.35_0924d110-63
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAxMSIsImFkZCI6ImRhbDIuMzMyMC50b3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImZlZmZiY2RmLTQwZDQtNDljYy1hOGQzLTlmYTg4NzJjNTBjNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImRhbDIuMzMyMC50b3AiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzNSIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoiUG9vbF8gfDEwLjY1TWIiLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%207
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hass.win:12340?allowInsecure=1#%E7%99%BD%E5%AB%96-069
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73nur3nuqbluIJEaWdpdGFsT2NlYW7kupHlhazlj7ggMTEiLCJhZGQiOiIxMzguMTk3LjE2NS4zMSIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiMTM4LjE5Ny4xNjUuMzEiLCJ0bHMiOiIifQ==
    trojan://iyinglong@54.245.213.176:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2024%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNjYiLCJhZGQiOiJ1c2FybS5wdHV1LmNmIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJjMTliMTM4Yy02ZTMwLTQzYjQtZjY2ZC1hOTRjNmU4NjlkMTIiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL3JheSIsImhvc3QiOiJ1c2FybS5wdHV1LmNmIiwidGxzIjoidGxzIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%201
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KFRH6aKR6YGTOkBreHN3YSkiLCJhZGQiOiI2OC4xODMuMTI5LjE5NyIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiNjguMTgzLjEyOS4xOTciLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDQ3IiwiYWRkIjoiYXJtLnB0dXUuZ3EiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk4MjFiODE3LTVjYjAtNGFmMy1hM2UzLTdjMTM3ODUwOTM1ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImFybS5wdHV1LmdxIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNjgiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiI2OC4xODMuMTI5LjE5NyIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiNjguMTgzLjEyOS4xOTciLCJ0bHMiOiIifQ==
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@34.220.146.25:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-34.220.146.25%3A443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvee6vee6puW4gkRpZ2l0YWxPY2VhbuS6keWFrOWPuCAxMSIsImFkZCI6IjEzOC4xOTcuMTY1LjMxIiwicG9ydCI6IjgwODAiLCJ0eXBlIjoibm9uZSIsImlkIjoiZTRlNDYyMzMtMzc2Yy00OWJlLWIzMDItM2ZmNmZjZTdhOGZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jY3R2MTMvaGQubTN1OCIsImhvc3QiOiIxMzguMTk3LjE2NS4zMSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNzAiLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6Yg5Yqg5ou/5aSnKFRH6aKR6YGTOkBreHN3YSkiLCJhZGQiOiIxMzguMTk3LjE2NS4zMSIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiMTM4LjE5Ny4xNjUuMzEiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-156.146.38.163%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    ss://YWVzLTI1Ni1jZmI6YW1hem9uc2tyMDU@34.220.146.25:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-34.220.146.25%3A443-%E8%A2%AB%E5%A2%99-%E7%9B%B4%E8%BF%9E-%E8%A7%A3%E9%94%81%E7%BE%8E%E5%9B%BD%E5%9C%B0%E5%8C%BANF%E9%9D%9E%E8%87%AA%E5%88%B6%E5%89%A7
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20029
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hass.win:12340?allowInsecure=1&sni=s2.hass.win#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73nur3nuqbluIJEaWdpdGFsT2NlYW7kupHlhazlj7ggMTEiLCJhZGQiOiIxMzguMTk3LjE2NS4zMSIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiMTM4LjE5Ny4xNjUuMzEiLCJ0bHMiOiIifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-156.146.38.163%3A443-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqPCfh6Yg5Yqg5ou/5aSnXzA5MjIwMTYiLCJhZGQiOiIxMzguMTk3LjE2NS4zMSIsInBvcnQiOiI4MDgwIiwidHlwZSI6Im5vbmUiLCJpZCI6ImU0ZTQ2MjMzLTM3NmMtNDliZS1iMzAyLTNmZjZmY2U3YThmYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvY2N0djEzL2hkLm0zdTgiLCJob3N0IjoiMTM4LjE5Ny4xNjUuMzEiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDQ3IiwiYWRkIjoiYXJtLnB0dXUuZ3EiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk4MjFiODE3LTVjYjAtNGFmMy1hM2UzLTdjMTM3ODUwOTM1ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImFybS5wdHV1LmdxIiwidGxzIjoidGxzIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20025
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%201
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjI5MjIiLCJhZGQiOiIyMy4yMzAuMTQ2LjI1NCIsInBvcnQiOiIxMjU4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVkZWI0MWNjLWE3NmEtNDdmMi1mYTk2LWI5MTQxZTY2YTJiMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NCIsImFkZCI6ImZybTEuMzMyMC50b3AiLCJwb3J0IjoiNDQzIiwidHlwZSI6ImF1dG8iLCJpZCI6IjE1ZWJmODJhLWRkM2EtNDUxOS05YTg5LTRlNjA4NThkNDdhYiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImZybTEuMzMyMC50b3AiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%20%207
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_13
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_13
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2034%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2023%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hass.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2018%20%E2%86%92%20openitsub.com
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%207
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDQ3IiwiYWRkIjoiYXJtLnB0dXUuZ3EiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk4MjFiODE3LTVjYjAtNGFmMy1hM2UzLTdjMTM3ODUwOTM1ZCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvMTIzIiwiaG9zdCI6ImFybS5wdHV1LmdxIiwidGxzIjoidGxzIn0=
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#US_13
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%20%201
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNzciLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MjIwNjIiLCJhZGQiOiJhcm0ucHR1dS5ncSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTgyMWI4MTctNWNiMC00YWYzLWEzZTMtN2MxMzc4NTA5MzVkIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8xMjMiLCJob3N0IjoiYXJtLnB0dXUuZ3EiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggVVMg576O5Zu9KHlvdXR1YmXpmL/kvJ/np5HmioApIiwiYWRkIjoiNjcuMjEuNzIuNDQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI1NjZkMDBmLTIxOGMtNDhmNy05YTM2LTEzZDNkNmYxYTcyNCIsImFpZCI6IjY0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3BhdGgvMTIwMjA4MzAxNDIyIiwiaG9zdCI6Ind3dy40ODgxNjYyNi54eXoiLCJ0bHMiOiJ0bHMifQ==
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20026
    ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20026
    vmess://eyJ2IjoiMiIsInBzIjoiUmVsYXlfIHwxOC45OE1iIiwiYWRkIjoiZnJtMS4zMzIwLnRvcCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMTVlYmY4MmEtZGQzYS00NTE5LTlhODktNGU2MDg1OGQ0N2FiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZnJtMS4zMzIwLnRvcCIsInRscyI6InRscyJ9

</details>

### 所有节点
合并节点总数: `5742`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `91`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `171`
- [freefq/free](https://github.com/freefq/free), 节点数量: `48`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `103`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `21`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `40`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3557`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `209`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `80`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `29`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `48`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `63`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `137`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `163`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `44`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `49`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `27`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `57`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`
- [Rokate/Proxy-Sub](https://github.com/Rokate/Proxy-Sub), 节点数量: `298`
- [mianfeifq/share](https://github.com/mianfeifq/share), 节点数量: `216`

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