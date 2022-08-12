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

    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1NSIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20026
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4NSIsImFkZCI6ImVycWkubGl2ZSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiN2NhYTI0NGYtMzdmMS00YjBjLWNjMTItMGMyZDM5MmQ0ZjZhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZXJxaS5saXZlIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20017
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIyMy4yMjcuMTk0LjE0NSIsInBvcnQiOiIzNjE5NSIsInR5cGUiOiJub25lIiwiaWQiOiJmYWU2ZWFlNS1hNWI1LTQxYmEtYjY2MC1kYzA2NzM0MDA0OGYiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMjMuMjI3LjE5NC4xNDUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA4MTAwMTMiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2014%EF%BD%9Copenit.pw
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20011
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20024
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%205%EF%BD%9Copenit.pw
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73lnKPmlq/ogIPmi4nmlq/okoLljaHlpKflraYgOCIsImFkZCI6IjE0My4xMTAuMjI0LjEyNyIsInBvcnQiOiI0ODkxOSIsInR5cGUiOiJub25lIiwiaWQiOiI1ZjU3YTkxZC1lOTRmLTRiYjctZmE4NS01NTg4NmEzZTMzODciLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1MiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjUiLCJhZGQiOiIxMzcuMTg0LjExOC40NyIsInBvcnQiOiI1MTY0OSIsInR5cGUiOiJub25lIiwiaWQiOiI1ZDBiMTcwOS01YzNjLTQwNzMtZmIzZi02NzI1MTQyNjU3MWUiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20044
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjYiLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzY1IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%209%EF%BD%9Copenit.pw
    vmess://eyJ2IjoiMiIsInBzIjoiUG9vbF/wn4e68J+HuFVTXzY5IiwiYWRkIjoiNDUuMzUuODQuMTYyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1MSIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzY1IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjYiLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20013
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwMjUiLCJhZGQiOiIyMy4yMzAuMTQ2LjI1NCIsInBvcnQiOiIxMjU4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVkZWI0MWNjLWE3NmEtNDdmMi1mYTk2LWI5MTQxZTY2YTJiMCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hazz.win:12340?allowInsecure=1&sni=s1.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20020
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20043
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjYiLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MiIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjYiLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwMTgiLCJhZGQiOiIxOTIuOS4yNDkuMjUxIiwicG9ydCI6IjIyNjE5IiwidHlwZSI6ImF1dG8iLCJpZCI6IjhkMmVlYmQzLWNkZGYtNDdmZi05ZDU0LTcwNDAxMzVkZWI1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTA3MDQiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6InhpZXhpLnRrIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MCIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDciLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4NCIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOe7v+WktOWklue9kembhuWboikoUHVibGljKSIsImFkZCI6InVzMDIuZ29nb2dvby5jeW91IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2dvIiwiaG9zdCI6InVzMDIuZ29nb2dvby5jeW91IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2OSIsImFkZCI6IjE5Mi45LjI0OS4yNTEiLCJwb3J0IjoiMjI2MTkiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGQyZWViZDMtY2RkZi00N2ZmLTlkNTQtNzA0MDEzNWRlYjUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NiIsImFkZCI6IjE5Mi4xODYuMTI5LjY2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%207%EF%BD%9Copenit.pw
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20014
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjYiLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzY1IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTA0OTIiLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MyIsImFkZCI6IjE5Mi4xODYuMTI5LjY2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2015%EF%BD%9Copenit.pw
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNTciLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0OCIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNTgiLCJhZGQiOiJlcnFpLmxpdmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdjYWEyNDRmLTM3ZjEtNGIwYy1jYzEyLTBjMmQzOTJkNGY2YSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImVycWkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNjYiLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNzEiLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDY@93.179.112.70:253#%F0%9F%87%BA%F0%9F%87%B8%20v2rayfree.eu.org%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%209
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NSIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    ssr://dXMtYW0zMi01LmVxbm9kZS5uZXQ6ODA4MTpvcmlnaW46YWVzLTI1Ni1jZmI6dGxzMS4yX3RpY2tldF9hdXRoOldVWldjbGhhWjFKdi8_Z3JvdXA9YUhSMGNITTZMeTkyTW5KaGVYTmxMbU52YlEmcmVtYXJrcz04Si1IdXZDZmg3Z2dYMVZUWC1lLWp1V2J2USZvYmZzcGFyYW09JnByb3RvcGFyYW09
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDciLCJhZGQiOiJ1c2EuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJ1c2EuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA4MTAwMTMiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwNSIsImFkZCI6IjE5Mi45LjI0OS4yNTEiLCJwb3J0IjoiMjI2MTkiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGQyZWViZDMtY2RkZi00N2ZmLTlkNTQtNzA0MDEzNWRlYjUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAxNzgwIiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MiIsImFkZCI6IjEyOS4xNDYuMTMzLjE1NyIsInBvcnQiOiI1MTAwOSIsInR5cGUiOiJub25lIiwiaWQiOiI4MTcxNGNlZi05YmRlLTRhMDgtYWE1MC1kNmJjMDE3MmQ3OGIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii9NRFZNREdKVVpJIiwiaG9zdCI6Inp6eWRuZnctdi5icDM2NS5jZiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDU3IiwiYWRkIjoidXMwMi5nb2dvZ29vLmN5b3UiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImRiNWQxYWEzLTkwOGItNDRkMS1iZTBhLTRlNmE4ZDRlNGNkYSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZ28iLCJob3N0IjoidXMwMi5nb2dvZ29vLmN5b3UiLCJ0bHMiOiJ0bHMifQ==
    trojan://dbdd4673-06e7-4a53-adb7-aa4232df529e@83.150.217.62:44612?allowInsecure=1#BG%201%EF%BD%9Copenit.pw
    trojan://dbdd4673-06e7-4a53-adb7-aa4232df529e@83.150.217.62:44612?allowInsecure=1#BG%201%EF%BD%9Copenit.pw
    trojan://dbdd4673-06e7-4a53-adb7-aa4232df529e@83.150.217.62:44612?allowInsecure=1#%F0%9F%87%B9%F0%9F%87%B7%20%E5%9C%9F%E8%80%B3%E5%85%B6%20001
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA1OSIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAwNTgiLCJhZGQiOiJlcnFpLmxpdmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdjYWEyNDRmLTM3ZjEtNGIwYy1jYzEyLTBjMmQzOTJkNGY2YSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImVycWkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NSIsImFkZCI6ImVycWkubGl2ZSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiN2NhYTI0NGYtMzdmMS00YjBjLWNjMTItMGMyZDM5MmQ0ZjZhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZXJxaS5saXZlIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTAxMjgzIiwiYWRkIjoidnVzMi4wYmFkLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTI3MDk0ZDMtZDY3OC00NzYzLTg1OTEtZTI0MGQwYmNhZTg3IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9jaGF0IiwiaG9zdCI6InZ1czIuMGJhZC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    trojan://e23f408a-012e-4030-8b31-02022031cb50@fhcamd1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%206%EF%BD%9Copenit.pw
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDY@93.179.112.70:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%B4%9B%E6%9D%89%E7%9F%B6IT7%E7%BD%91%E7%BB%9C%201
    trojan://dbdd4673-06e7-4a53-adb7-aa4232df529e@150.230.23.0:44616?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%EF%BD%9Copenit.pw
    trojan://d7fd8aaa-4581-4281-80aa-4b63e5e1f157@jgwld2.gaox.ml:443?allowInsecure=1#%F0%9F%87%AC%F0%9F%87%A7%20%E8%8B%B1%E5%9B%BD%20001
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh6cg6Iux5Zu9IDAwNyIsImFkZCI6InVrLW1hbmNoZXN0ZXIuZWl3MmVlbW8uY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVrLW1hbmNoZXN0ZXIuZWl3MmVlbW8uY29tIiwidGxzIjoidGxzIn0=
    trojan://dbdd4673-06e7-4a53-adb7-aa4232df529e@150.230.23.0:44616?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20018
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NCIsImFkZCI6IjUxLjgxLjIyMy4yOSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9XzA4MTAwMjYiLCJhZGQiOiIxNDYuMC40Mi44NyIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJnZXJtYW55LWR1c3NlbGRvcmYubWFoM0hvZXQuY29tIiwidGxzIjoidGxzIn0=
    trojan://02e653c9-7c93-46a9-999d-11834bd0c577@jgwld1.gaox.ml:443?allowInsecure=1#%F0%9F%87%AC%F0%9F%87%A7%20%E8%8B%B1%E5%9B%BD%20002
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MTA1NTgiLCJhZGQiOiJ2dXMyLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidnVzMi4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MyIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiI1MS44MS4yMjMuMjIiLCJwb3J0IjoiNDQzIiwidHlwZSI6ImF1dG8iLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiNTEuODEuMjIzLjIyIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hq/Cfh7cg5rOV5Zu9IDAwMiIsImFkZCI6Im1rZXQuc2hvb3BjaWRlci5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjYxMWJiZGJiLTExMzgtNDc5Ny04ZDlmLWY5MmY1OTViN2M3ZSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6Im1rZXQuc2hvb3BjaWRlci5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HrPCfh6cg6Iux5Zu9IDAwNiIsImFkZCI6IjE0Ni43MC40Ni42OCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1ay1tYW5jaGVzdGVyLmVpdzJlZW1vLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MiIsImFkZCI6IjUxLjgxLjIyMy4xNCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    trojan://dbf9bf9c-2c3f-474a-8031-d4c00666a989@fhcamd2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20012
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MCIsImFkZCI6InY1LnRnZmFrYS5jb20iLCJwb3J0IjoiODQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiIyMDgwZDdjYS1kNmNkLTRkMjMtYjQ2ZS0yMjUxNDgzYmQzMmMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2FwaS92My9kb3dubG9hZC5nZXRGaWxlIiwiaG9zdCI6InY1LnRnZmFrYS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MSIsImFkZCI6IjUxLjgxLjIyMy4zNiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoiVVNfNzIiLCJhZGQiOiI1MS44MS4yMjMuMTQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImMwMTU2NDUxLTRlZmItNDVlMi04NGZjLThkMzE1YzQ2NTBkYiIsImFpZCI6IjMyIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2MCIsImFkZCI6IjUxLjgxLjIyMy4zMSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYzAxNTY0NTEtNGVmYi00NWUyLTg0ZmMtOGQzMTVjNDY1MGRiIiwiYWlkIjoiMzIiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9IDAwOSIsImFkZCI6Imdlcm1hbnktZHVzc2VsZG9yZi5tYWgzSG9ldC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoiZ2VybWFueS1kdXNzZWxkb3JmLm1haDNIb2V0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+Hr/Cfh7Ug5pel5pysXzA4MTAxMjMiLCJhZGQiOiJ2anAzLjBiYWQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI5MjcwOTRkMy1kNjc4LTQ3NjMtODU5MS1lMjQwZDBiY2FlODciLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2NoYXQiLCJob3N0IjoidmpwMy4wYmFkLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HsfCfh7og5Y2i5qOu5aChXzA4MTAwMDEiLCJhZGQiOiJsc2IuamNuZi5hcHAiLCJwb3J0IjoiNDQzIiwidHlwZSI6ImF1dG8iLCJpZCI6ImM3NTNlOGE4LWUxODAtNGU3Ni1hNDg2LWM5MTcyNzNkNzE4YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvemNqZCIsImhvc3QiOiJsc2IuamNuZi5hcHAiLCJ0bHMiOiJ0bHMifQ==

</details>

### 所有节点
合并节点总数: `5459`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `93`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `448`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `169`
- [freefq/free](https://github.com/freefq/free), 节点数量: `68`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `149`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `87`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `71`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3212`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `96`
- [iwxf/free-v2ray](https://github.com/iwxf/free-v2ray), 节点数量: `39`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `1`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `61`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `58`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `68`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `56`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `5`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `296`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `4`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `65`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `59`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `15`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `48`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `0`
- [Nodefree.org](https://github.com/Fukki-Z/nodefree), 节点数量: `50`

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