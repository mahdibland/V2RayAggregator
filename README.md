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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzE2NiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    ss://YWVzLTEyOC1nY206NjFlMmQwMjQtMzFhYy00YzhhLThjYTgtNmVhODVhZTc5NDFi@155.94.239.243:20001#%F0%9F%87%BA%F0%9F%87%B8%20%E5%A4%A7%E8%90%9D%E5%8D%9C%E9%B8%A1%E6%B4%9B%E6%9D%89%E7%9F%B6
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIxMjMiLCJhZGQiOiIxNDQuMTI2LjIyMy4yNTAiLCJwb3J0IjoiMTgwNTciLCJ0eXBlIjoibm9uZSIsImlkIjoiZTE3OGNkYWEtOWRmYi00MzUwLWQyMzUtYTFlZGIxOGU5YmQxIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hazz.win:12340?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hazz.win:12340?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://gkjpxNwC7x@173.82.248.109:11687?allowInsecure=1#TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%201100%20%7C%206.25Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNjUiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MCIsImFkZCI6IjIzLjIzNC4yMTUuMzIiLCJwb3J0IjoiMjUxMDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDcwMDBkNzktMmYwZS00YmNhLWE0ZmQtNGI4MDFhOGI2YTljIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidmlpYmFoNnUuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzE2NiIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=s3.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%20%E7%BE%8E%E5%9B%BD_118%20%7C16.22Mb
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA4MzAwMDciLCJhZGQiOiJ1czAzLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAzLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20012
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NiIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4OSIsImFkZCI6IjIzLjIzNC4yMTUuMzIiLCJwb3J0IjoiMjUxMDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDcwMDBkNzktMmYwZS00YmNhLWE0ZmQtNGI4MDFhOGI2YTljIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidmlpYmFoNnUuY29tIiwidGxzIjoiIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20002
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwNjkiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=s3.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%20%E7%BE%8E%E5%9B%BD_118%20%7C16.22Mb
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MjYwODgiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIxMDYxIiwiYWRkIjoiMTM3LjE4NC4xMTguNDciLCJwb3J0IjoiNTE2NDkiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWQwYjE3MDktNWMzYy00MDczLWZiM2YtNjcyNTE0MjY1NzFlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoiaWVzZWkxZWkuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0OCIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%206%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s2.hazz.win:12340?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNjUiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s4.hazz.win:12340?allowInsecure=1#%F0%9F%87%B8%F0%9F%87%AC%20SG%201%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s1.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%202%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIxNDQ0IiwiYWRkIjoiMTM3LjE4NC4xMTguNDciLCJwb3J0IjoiNTE2NDkiLCJ0eXBlIjoibm9uZSIsImlkIjoiNWQwYjE3MDktNWMzYy00MDczLWZiM2YtNjcyNTE0MjY1NzFlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImxjLWtyMDItZGlyZWN0MDEubGMta3IwMi5sYy1ub2RlLmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNzYiLCJhZGQiOiJ3ZWl4aW4uYmFiYXpodWppLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjc4NDg3MzktN2U2Mi00MTM4LTlmZDMtMDk4YTYzOTY0YjZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii90ZWNoIiwiaG9zdCI6IndlaXhpbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%201%20%E2%86%92%20openitsub.com
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2026%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDEzIiwiYWRkIjoid2VpeGluLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdGVjaCIsImhvc3QiOiJ3ZWl4aW4uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2MCIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwMjIiLCJhZGQiOiJ3ZWl4aW4uYmFiYXpodWppLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiMjc4NDg3MzktN2U2Mi00MTM4LTlmZDMtMDk4YTYzOTY0YjZiIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii90ZWNoIiwiaG9zdCI6IndlaXhpbi5iYWJhemh1amkuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA5MDIwMDciLCJhZGQiOiJ1czAzLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAzLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%204%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoiQFNTUlNVQi1WMDQt5LuY6LS55o6o6I2QOnN1by55dC9zc3JzdWIiLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwNjYiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%AE%BE%E5%A4%95%E6%B3%95%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%8B%89%E5%85%8B%E4%B8%87%E7%BA%B3%E5%8E%BF%E5%85%8B%E6%8B%89%E5%85%8B%E6%96%AF%E8%90%A8%E5%AF%86%E7%89%B9%E8%87%AA%E6%B2%BB%E5%8C%BAVolumeDrive%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%207
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDljJfnvo7lnLDljLogIDQ5IiwiYWRkIjoiMTA3LjE3My44My4yMTQiLCJwb3J0IjoiMzc1NDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWY1OWE1ODYtMDUzMi00NzYzLWYzNTMtOTQ4ZWI0MTNmMDBkIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidmlpYmFoNnUuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIxOTg2IiwiYWRkIjoiMTA3LjE3My4yNTAuMTI5IiwicG9ydCI6IjE1Njg2IiwidHlwZSI6Im5vbmUiLCJpZCI6IjY2NWM5YzRlLWIyNmQtNDlhYS1hNzViLTUyMGQ1Mzk0OGRkOCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20004
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvSIsImFkZCI6IjEwNy4xNzMuMjUwLjEyOSIsInBvcnQiOiIyNTg4MSIsInR5cGUiOiJub25lIiwiaWQiOiI2OGY4ZWQ5Yy05YWMzLTQyN2EtYjE2Yy02ZjFkN2ZiN2YxMmQiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MjYwODgiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwNiIsImFkZCI6IjIxNi4xMjcuMTY5LjIxMSIsInBvcnQiOiI1MDQzOCIsInR5cGUiOiJub25lIiwiaWQiOiI5ZTk4MGNlNi02YjFjLTQ5YzYtZDBiZS02YTBmN2FiOTYxZTMiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiMTguMTY3Ljk0LjI0MyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzMSIsImFkZCI6IjIzLjIzNC4yMTUuMzIiLCJwb3J0IjoiMjUxMDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDcwMDBkNzktMmYwZS00YmNhLWE0ZmQtNGI4MDFhOGI2YTljIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6Imd1aWJpLm1sIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzMyIsImFkZCI6IjEwNy4xNzMuMTUzLjE0NyIsInBvcnQiOiI4NzY1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImQ1MThkZWMzLWY4MDEtNDZmNi1iMjk1LTYzZjRiZjE2ZmUxMiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IjEwNy4xNzMuMTUzLjE0NyIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MCIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3NiIsImFkZCI6IjIzLjIzMC4xNDYuMjU0IiwicG9ydCI6IjEyNTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWRlYjQxY2MtYTc2YS00N2YyLWZhOTYtYjkxNDFlNjZhMmIwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm70gIDEzIiwiYWRkIjoid2VpeGluLmJhYmF6aHVqaS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI3ODQ4NzM5LTdlNjItNDEzOC05ZmQzLTA5OGE2Mzk2NGI2YiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdGVjaCIsImhvc3QiOiJ3ZWl4aW4uYmFiYXpodWppLmNvbSIsInRscyI6InRscyJ9
    trojan://2Q74kEsaZq@209.209.9.149:46539?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20001
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzE2OCIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://2Q74kEsaZq@209.209.9.149:46539?allowInsecure=1#RW%201%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwODEiLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDI0ODgiLCJhZGQiOiJzMi41MjBndWdlLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiY2YxODE5YzgtZTUzMC00NjI2LWFlYzAtODdhYzA0MjAwMzg1IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9oYXBweSIsImhvc3QiOiJzMi41MjBndWdlLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MiIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2010%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAzMSIsImFkZCI6IjIzLjIzNC4yMTUuMzIiLCJwb3J0IjoiMjUxMDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiMDcwMDBkNzktMmYwZS00YmNhLWE0ZmQtNGI4MDFhOGI2YTljIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6Imd1aWJpLm1sIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20010
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwMjAiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiUG9vbF/wn4e68J+HuFVTXzE2OSIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    trojan://VjXDl4Gf5j@8.9.30.35:8080?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28TG%E9%A2%91%E9%81%93%3A%40kxswa%29%207
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20015
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwODMiLCJhZGQiOiIxMDcuMTczLjI1MC45NCIsInBvcnQiOiI0NjU0NyIsInR5cGUiOiJub25lIiwiaWQiOiIwM2Q4ODgwOS1jZWRkLTQxY2UtZTEwNy03YjFjMGJmMzY0MjAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDAwOCIsImFkZCI6IjIzLjk1LjIxNS4xNCIsInBvcnQiOiIzNTAxMCIsInR5cGUiOiJub25lIiwiaWQiOiI0OGRlMzg1ZC1jODA5LTRhMGEtOGVmNS1iYmJjN2VhOTg2ZTIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0Ijoid3d3LmZsaWVzd2ltaW5nLnRrIiwidGxzIjoiIn0=
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDY@95.169.4.174:254#US_822
    trojan://2Q74kEsaZq@209.209.9.149:46539?allowInsecure=1#RW%201%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwODMiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20014
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwNjQiLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDYiLCJhZGQiOiJqaXh1Mi5xaXFpcy5tbCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiOGZmMzMyMWEtNjNjNS00OGE1LWE0NjktZjMzNDc4OTEwMmZmIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9lYjExZmQwMy8iLCJob3N0Ijoiaml4dTIucWlxaXMubWwiLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5NjgyZWRkNi04OWU2LTRlNmEtYjMxZC0yNzEwODk3NzFkODc@do.cloudorg.uk:10365#%F0%9F%87%BA%F0%9F%87%B8%20Relay_%F0%9F%87%BA%F0%9F%87%B8US-%F0%9F%87%BA%F0%9F%87%B8US_32
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDljJfnvo7lnLDljLogIDQ5IiwiYWRkIjoiMTA3LjE3My44My4yMTQiLCJwb3J0IjoiMzc1NDEiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWY1OWE1ODYtMDUzMi00NzYzLWYzNTMtOTQ4ZWI0MTNmMDBkIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidmlpYmFoNnUuY29tIiwidGxzIjoiIn0=
    trojan://gkjpxNwC7x@173.82.248.109:11687?allowInsecure=1#TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%201100%20%7C%206.25Mb
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%209%20%E2%86%92%20openitsub.com
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1&sni=s3.hazz.win#%F0%9F%87%BA%F0%9F%87%B8%20TG%40https%3A%2F%2Ft.me%2Fmoneyfly2022%20%20%20%20%20%20%E7%BE%8E%E5%9B%BD_118%20%7C16.22Mb
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20034
    trojan://vZ2Oh0BipB@qcjs.cc.freedl.heinu.cc:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%207%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNjUiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20019
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNjUiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NiIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0MyIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwODMiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0OSIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNjUiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwNzMiLCJhZGQiOiIyMy45NS4yMTUuMTQiLCJwb3J0IjoiMzUwMTAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDhkZTM4NWQtYzgwOS00YTBhLThlZjUtYmJiYzdlYTk4NmUyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIxNDAiLCJhZGQiOiJmcmVlLnVzMi5lY3lkeS5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6ImF1dG8iLCJpZCI6ImM0ODMxNTc0LTZiODYtMzMyZS1hMjI5LTRkNDc4MTJiMGJiNCIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZWN5IiwiaG9zdCI6ImZyZWUudXMyLmVjeWR5LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0NCIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDIwNzEiLCJhZGQiOiIyMy45NS4yMTUuMTQiLCJwb3J0IjoiMzUwMTAiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDhkZTM4NWQtYzgwOS00YTBhLThlZjUtYmJiYzdlYTk4NmUyIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6Ind3dy5mbGllc3dpbWluZy50ayIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo5NjgyZWRkNi04OWU2LTRlNmEtYjMxZC0yNzEwODk3NzFkODc@137.184.93.209:10365#US_24
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAxNDcyIiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6IjE1MC4yMzAuNDEuOSIsInRscyI6IiJ9
    trojan://dfbf0d67-f03d-4184-a224-c2d64a571f99@s3.hazz.win:12340?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%201%20%E2%86%92%20openitsub.com
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiIxMDcuMTczLjI1MC4xMjkiLCJwb3J0IjoiNDI3MTMiLCJ0eXBlIjoibm9uZSIsImlkIjoiNDAxMmQ5MzItOTNmZS00ODI4LWRjYzktMzMxYzg3MTQ5MGM2IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IjEwNy4xNzMuMjUwLjEyOSIsInRscyI6IiJ9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%AE%BE%E5%A4%95%E6%B3%95%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%8B%89%E5%85%8B%E4%B8%87%E7%BA%B3%E5%8E%BF%E5%85%8B%E6%8B%89%E5%85%8B%E6%96%AF%E8%90%A8%E5%AF%86%E7%89%B9%E8%87%AA%E6%B2%BB%E5%8C%BAVolumeDrive%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%207
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA0OSIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%AE%BE%E5%A4%95%E6%B3%95%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%8B%89%E5%85%8B%E4%B8%87%E7%BA%B3%E5%8E%BF%E5%85%8B%E6%8B%89%E5%85%8B%E6%96%AF%E8%90%A8%E5%AF%86%E7%89%B9%E8%87%AA%E6%B2%BB%E5%8C%BAVolumeDrive%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%207
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl6IqC54K5IDkiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MjYwODgiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MzAwNjUiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA5MDI0ODkiLCJhZGQiOiIxNTAuMjMwLjQxLjkiLCJwb3J0IjoiMjMyOTIiLCJ0eXBlIjoibm9uZSIsImlkIjoiOTU2YzZjMmYtYmY1NC00Yjg3LWZhZmQtNGI3NjdjYTEyNzUwIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9

</details>

### 所有节点
合并节点总数: `5392`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `120`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `176`
- [freefq/free](https://github.com/freefq/free), 节点数量: `50`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `139`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `1`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `183`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `59`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3169`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `125`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `69`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `50`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `50`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `28`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `173`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `49`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `46`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `0`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `637`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `27`
- [kxswa/k](https://github.com/kxswa/k), 节点数量: `50`
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