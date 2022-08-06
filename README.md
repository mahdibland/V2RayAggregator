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

    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5NyIsImFkZCI6ImVycWkubGl2ZSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiN2NhYTI0NGYtMzdmMS00YjBjLWNjMTItMGMyZDM5MmQ0ZjZhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiZXJxaS5saXZlIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDQiLCJhZGQiOiJlcnFpLmxpdmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdjYWEyNDRmLTM3ZjEtNGIwYy1jYzEyLTBjMmQzOTJkNGY2YSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImVycWkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5OSIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwMiIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwMCIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NSIsImFkZCI6IjE5Mi4xODYuMTI5LjY2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwMiIsImFkZCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5OSIsImFkZCI6Imllc2VpMWVpLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJpZXNlaTFlaS5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NCIsImFkZCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtYnVmZmFsby5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxODA4IiwiYWRkIjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggdjJyYXlmcmVlLmV1Lm9yZyAtIOe+juWbvUNsb3VkRmxhcmXlhazlj7hDRE7oioLngrkgNTgiLCJhZGQiOiJlcnFpLmxpdmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdjYWEyNDRmLTM3ZjEtNGIwYy1jYzEyLTBjMmQzOTJkNGY2YSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImVycWkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4NyIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4NyIsImFkZCI6IjE5Mi45Ni4yMDQuMjUwIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS13YXNoaW5ndG9uLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3OCIsImFkZCI6IjEwNy4xNzMuMjUwLjk0IiwicG9ydCI6IjI1MzE4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVkMjkzNDExLWFiNTMtNGViYy1mMGFiLTM0ZDc4ZmExZjVjZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJsYy1rcjAyLWRpcmVjdDAxLmxjLWtyMDIubGMtbm9kZS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3OCIsImFkZCI6IjEwNy4xNzMuMjUwLjk0IiwicG9ydCI6IjI1MzE4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImVkMjkzNDExLWFiNTMtNGViYy1mMGFiLTM0ZDc4ZmExZjVjZSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJsYy1rcjAyLWRpcmVjdDAxLmxjLWtyMDIubGMtbm9kZS5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA2NiIsImFkZCI6IjE5Mi4xODYuMTI5LjY2IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1idWZmYWxvLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4OSIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA3MSIsImFkZCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwMCIsImFkZCI6IjIwOC45OC40OC4yIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imllc2VpMWVpLmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoiUG9vbF/wn4e68J+HuFVTXzY5IiwiYWRkIjoiNDUuMzUuODQuMTYyIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJhYmE1MGRkNC01NDg0LTNiMDUtYjE0YS00NjYxY2FmODYyZDUiLCJhaWQiOiI0IiwibmV0Ijoid3MiLCJwYXRoIjoiL3dzIiwiaG9zdCI6InVzYS1kYWxsYXMubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi6L+Z5Lqb6IqC54K55Y+q6IO95aSH55So5oiW6ICF6Ziy5q2i5aSx6IGU77yM6Jm954S26LSo6YeP5bm25LiN5piv5b6I5aW977yM5Lmf6K+35L2O6LCD5L2/55SoOikiLCJhZGQiOiJlcnFpLmxpdmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdjYWEyNDRmLTM3ZjEtNGIwYy1jYzEyLTBjMmQzOTJkNGY2YSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImVycWkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggX1VTX+e+juWbvSIsImFkZCI6IjIzLjIyNy4xOTQuMTQ1IiwicG9ydCI6IjM2MTk1IiwidHlwZSI6Im5vbmUiLCJpZCI6ImZhZTZlYWU1LWE1YjUtNDFiYS1iNjYwLWRjMDY3MzQwMDQ4ZiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    trojan://2Q74kEsaZq@209.209.9.149:46539?allowInsecure=1#RW%201%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMTAiLCJhZGQiOiIxOTIuOTYuMjA0LjI1MCIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    trojan://2Q74kEsaZq@209.209.9.149:46539?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20008
    trojan://2Q74kEsaZq@209.209.9.149:46539?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20009
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMzM0IiwiYWRkIjoiMTA3LjE3My4yNTAuOTQiLCJwb3J0IjoiMjUzMTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWQyOTM0MTEtYWI1My00ZWJjLWYwYWItMzRkNzhmYTFmNWNlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6ImxjLWtyMDItZGlyZWN0MDEubGMta3IwMi5sYy1ub2RlLmNvbSIsInRscyI6IiJ9
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MyIsImFkZCI6IjQ1LjM1Ljg0LjE2MiIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiYWJhNTBkZDQtNTQ4NC0zYjA1LWIxNGEtNDY2MWNhZjg2MmQ1IiwiYWlkIjoiNCIsIm5ldCI6IndzIiwicGF0aCI6Ii93cyIsImhvc3QiOiJ1c2EtZGFsbGFzLmx2dWZ0LmNvbSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA4MDYwMTIiLCJhZGQiOiJ3d3cuZGlnaXRhbG9jZWFuLmNvbSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiM2RmNjYxMzctYTQyOC00MjljLWE4NTgtOGIxNTA3MjFiMzU0IiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii95b3V0YnVlQGJhaS1waWFvLXdhbmctemhlX3Z3cyIsImhvc3QiOiJ1czIzLjU2NzU2OC5tbCIsInRscyI6InRscyJ9
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1&sni=us.bw7.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20024
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20014
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1&sni=us.bw7.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20US%2028%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1&sni=us.bw7.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20016
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1&sni=us.bw7.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20024
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMzQ3IiwiYWRkIjoiOTguMTQyLjEzNy4yMSIsInBvcnQiOiI0NzM4NSIsInR5cGUiOiJub25lIiwiaWQiOiIzNDI5MzdiYi1hZDUxLTQwZWQtY2IyMi1mZjVlYjBmN2VjNjMiLCJhaWQiOiI2NCIsIm5ldCI6InRjcCIsInBhdGgiOiIvc3Nob2NlYW4iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2026%20%E2%86%92%20TG%40SCINV
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20016
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm71DbG91ZEZsYXJl5YWs5Y+4Q0RO6IqC54K5IDU4IiwiYWRkIjoiZXJxaS5saXZlIiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiI3Y2FhMjQ0Zi0zN2YxLTRiMGMtY2MxMi0wYzJkMzkyZDRmNmEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiJlcnFpLmxpdmUiLCJ0bHMiOiJ0bHMifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20_CA_%E5%8A%A0%E6%8B%BF%E5%A4%A7
    trojan://ad9ee6b5-4707-478a-ba5c-0fc7a4b0314c@199.19.109.30:50330?allowInsecure=1&sni=us.bw7.hyperlinkvpn.xyz#%F0%9F%87%BA%F0%9F%87%B8%20US%2031%20%E2%86%92%20TG%40SCINV
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2016%20%E2%86%92%20TG%40SCINV
    trojan://3a2c0c6c-9ee5-c05f-c951-fcd73831983e@lsj02.wangxd.life:3052?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20012
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2017%20%E2%86%92%20TG%40SCINV
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2012%20%E2%86%92%20TG%40SCINV
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%28%E7%BB%BF%E5%A4%B4%E5%A4%96%E7%BD%91%E9%9B%86%E5%9B%A2%29%28Public%29
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2014%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDMiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20011
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20014
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2014%20%E2%86%92%20TG%40SCINV
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://05742120-ce23-4cc8-88f5-6d221ce45bf4@fhcarm1.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20005
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2012%20%E2%86%92%20TG%40SCINV
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2039
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:810#%F0%9F%87%A8%F0%9F%87%A6%20v2rayfree.eu.org%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2028
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@97.64.122.63:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A%E6%B4%9B%E6%9D%89%E7%9F%B6%2043
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMTciLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDEwNyIsImFkZCI6IjY0LjExMi40MS4xNSIsInBvcnQiOiIyMzc1NyIsInR5cGUiOiJub25lIiwiaWQiOiJkNjMwZDg0Ni1iMjMwLTQzMmUtOTdkNC1kODVjODIyOTMzNmMiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsImhvc3QiOiI2NC4xMTIuNDEuMTUiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA4MDIwMTUiLCJhZGQiOiJlcnFpLmxpdmUiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjdjYWEyNDRmLTM3ZjEtNGIwYy1jYzEyLTBjMmQzOTJkNGY2YSIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6ImVycWkubGl2ZSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggUmVsYXlf8J+HuvCfh7hVUy3wn4e68J+HuFVTXzY1IiwiYWRkIjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLWRhbGxhcy5sdnVmdC5jb20iLCJ0bHMiOiJ0bHMifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9KOe7v+WktOWklue9kembhuWboikoUHVibGljKSIsImFkZCI6InVzMDIuZ29nb2dvby5jeW91IiwicG9ydCI6IjQ0MyIsInR5cGUiOiJub25lIiwiaWQiOiJkYjVkMWFhMy05MDhiLTQ0ZDEtYmUwYS00ZTZhOGQ0ZTRjZGEiLCJhaWQiOiIwIiwibmV0Ijoid3MiLCJwYXRoIjoiL2dvIiwiaG9zdCI6InVzMDIuZ29nb2dvby5jeW91IiwidGxzIjoidGxzIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2039
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMDkiLCJhZGQiOiJ1c2Etd2FzaGluZ3Rvbi5sdnVmdC5jb20iLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6ImFiYTUwZGQ0LTU0ODQtM2IwNS1iMTRhLTQ2NjFjYWY4NjJkNSIsImFpZCI6IjQiLCJuZXQiOiJ3cyIsInBhdGgiOiIvd3MiLCJob3N0IjoidXNhLXdhc2hpbmd0b24ubHZ1ZnQuY29tIiwidGxzIjoidGxzIn0=
    trojan://srGSKqR5Fv@104.168.144.215:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20%E7%BE%8E%E5%9B%BD%20028
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxNzExIiwiYWRkIjoiMTA3LjE3My4yNTAuOTQiLCJwb3J0IjoiMjUzMTgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZWQyOTM0MTEtYWI1My00ZWJjLWYwYWItMzRkNzhmYTFmNWNlIiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HqfCfh6og5b635Zu9IDAwNSIsImFkZCI6IjQ1LjExLjkyLjM2IiwicG9ydCI6IjMwNDA4IiwidHlwZSI6Im5vbmUiLCJpZCI6ImYzOTdjNzcxLTlhZGYtNDg4MC04NjExLThhYzhiOWNlMjRmNSIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imdlcm1hbnktZHVzc2VsZG9yZi5tYWgzSG9ldC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxNzE1IiwiYWRkIjoiNDUuMTEuOTIuMzYiLCJwb3J0IjoiMzA0MDgiLCJ0eXBlIjoibm9uZSIsImlkIjoiZjM5N2M3NzEtOWFkZi00ODgwLTg2MTEtOGFjOGI5Y2UyNGY1IiwiYWlkIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%5B08-06%5D-%F0%9F%87%A8%F0%9F%87%A6-%E5%8A%A0%E6%8B%BF%E5%A4%A7-003-72.140.224.195
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%AE%BE%E5%A4%95%E6%B3%95%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%8B%89%E5%85%8B%E4%B8%87%E7%BA%B3%E5%8E%BF%E5%85%8B%E6%8B%89%E5%85%8B%E6%96%AF%E8%90%A8%E5%AF%86%E7%89%B9%E8%87%AA%E6%B2%BB%E5%8C%BAVolumeDrive%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%204
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MiIsImFkZCI6IjEwNC4xNTYuMjI5LjE0OCIsInBvcnQiOiIzNjc4OCIsInR5cGUiOiJub25lIiwiaWQiOiI5ZmVlNzI0OS02OWZiLTQ5MGQtZTYxNy1jZmI1NGEyNDk5MzIiLCJhaWQiOiI2MCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiMTA0LjE1Ni4yMjkuMTQ4IiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:803#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A803-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:810#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDE1NyIsImFkZCI6IjIxNi4yNC4yNDguMTA0IiwicG9ydCI6IjI5ODYyIiwidHlwZSI6Im5vbmUiLCJpZCI6IjI4MWYzNDVmLWRhOTYtNDg1Yi05YWEzLTRiYzUzMGYyZmZhMiIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvZmRzZmEiLCJob3N0IjoiIiwidGxzIjoiIn0=
    trojan://f39bd244-f5fe-415c-8b98-a1e5250bf178@fhcarm2.gaox.ml:443?allowInsecure=1#%F0%9F%87%BA%F0%9F%87%B8%20US%2012%20%E2%86%92%20TG%40SCINV
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20%3A%E5%8A%A0%E6%8B%BF%E5%A4%A7-ss-72.140.224.195%3A800-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:810#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2028
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA4MSIsImFkZCI6IjEyOS4xNDYuMTMzLjE1NyIsInBvcnQiOiI1MTAwOSIsInR5cGUiOiJub25lIiwiaWQiOiI4MTcxNGNlZi05YmRlLTRhMDgtYWE1MC1kNmJjMDE3MmQ3OGIiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoieGlleGkudGsiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7ggZ2l0aHViLmNvbS9mcmVlZnEgLSDnvo7lm73liqDlt54gMjQiLCJhZGQiOiI2NC4xMTIuNDEuMTUiLCJwb3J0IjoiMjM3NTciLCJ0eXBlIjoibm9uZSIsImlkIjoiZDYzMGQ4NDYtYjIzMC00MzJlLTk3ZDQtZDg1YzgyMjkzMzZjIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMzM2IiwiYWRkIjoiMTI5LjE0Ni4xMzMuMTU3IiwicG9ydCI6IjUxMDA5IiwidHlwZSI6Im5vbmUiLCJpZCI6IjgxNzE0Y2VmLTliZGUtNGEwOC1hYTUwLWQ2YmMwMTcyZDc4YiIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiJ4aWV4aS50ayIsInRscyI6IiJ9
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:810#%E8%BF%99%E4%BA%9B%E8%8A%82%E7%82%B9%E5%8F%AA%E8%83%BD%E5%A4%87%E7%94%A8%E6%88%96%E8%80%85%E9%98%B2%E6%AD%A2%E5%A4%B1%E8%81%94%EF%BC%8C%E8%99%BD%E7%84%B6%E8%B4%A8%E9%87%8F%E5%B9%B6%E4%B8%8D%E6%98%AF%E5%BE%88%E5%A5%BD%EF%BC%8C%E4%B9%9F%E8%AF%B7%E4%BD%8E%E8%B0%83%E4%BD%BF%E7%94%A8%3A%29
    vmess://eyJ2IjoiMiIsInBzIjoi5pyq55+lXzA4MDIwMTYiLCJhZGQiOiJ1czAyLmdvZ29nb28uY3lvdSIsInBvcnQiOiI0NDMiLCJ0eXBlIjoibm9uZSIsImlkIjoiZGI1ZDFhYTMtOTA4Yi00NGQxLWJlMGEtNGU2YThkNGU0Y2RhIiwiYWlkIjoiMCIsIm5ldCI6IndzIiwicGF0aCI6Ii9nbyIsImhvc3QiOiJ1czAyLmdvZ29nb28uY3lvdSIsInRscyI6InRscyJ9
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxNzM5IiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiLyIsImhvc3QiOiIiLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDIwMzQiLCJhZGQiOiIxNTguMTAxLjE5LjE3MiIsInBvcnQiOiIxMDkxMCIsInR5cGUiOiJodHRwIiwiaWQiOiIyNDE2NDVmNS0zMTkwLTQyOWItYjUxMy01MjY1YTI0MmRmZTEiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii8iLCJob3N0IjoiIiwidGxzIjoiIn0=
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:800#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2039
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MiIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJsdnVmdC5jb20iLCJ0bHMiOiIifQ==
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9IDA5MiIsImFkZCI6IjE1MC4yMzAuNDEuOSIsInBvcnQiOiIyMzI5MiIsInR5cGUiOiJub25lIiwiaWQiOiI5NTZjNmMyZi1iZjU0LTRiODctZmFmZC00Yjc2N2NhMTI3NTAiLCJhaWQiOiIwIiwibmV0IjoidGNwIiwicGF0aCI6Ii93cyIsImhvc3QiOiJsdnVmdC5jb20iLCJ0bHMiOiIifQ==
    ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpHIXlCd1BXSDNWYW8@72.140.224.195:810#%F0%9F%87%A8%F0%9F%87%A6%20github.com%2Ffreefq%20-%20%E5%8A%A0%E6%8B%BF%E5%A4%A7%20%2028
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20github.com%2Ffreefq%20-%20%E7%BE%8E%E5%9B%BD%E5%AE%BE%E5%A4%95%E6%B3%95%E5%B0%BC%E4%BA%9A%E5%B7%9E%E6%8B%89%E5%85%8B%E4%B8%87%E7%BA%B3%E5%8E%BF%E5%85%8B%E6%8B%89%E5%85%8B%E6%96%AF%E8%90%A8%E5%AF%86%E7%89%B9%E8%87%AA%E6%B2%BB%E5%8C%BAVolumeDrive%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%204
    ss://YWVzLTI1Ni1jZmI6Yndoc2tyc2tyMDU@199.115.228.30:253#%F0%9F%87%BA%F0%9F%87%B8%20%3A%E7%BE%8E%E5%9B%BD-ss-199.115.228.30%3A253-%E5%8F%AF%E7%94%A8-%E7%9B%B4%E8%BF%9E-%E4%B8%8D%E6%94%AF%E6%8C%81Netflix
    trojan://71b55a84-3fac-4458-abff-eaad79219c91@jgwld3.gaox.ml:443?allowInsecure=1#%F0%9F%87%AC%F0%9F%87%A7%20%5B08-06%5D%7Coslook%7C%E8%8B%B1%E5%9B%BD%28GB%29United%2BKiongdom%2FSlough_27
    vmess://eyJ2IjoiMiIsInBzIjoi8J+HuvCfh7gg576O5Zu9XzA4MDYxMzQxIiwiYWRkIjoiMTUwLjIzMC40MS45IiwicG9ydCI6IjIzMjkyIiwidHlwZSI6Im5vbmUiLCJpZCI6Ijk1NmM2YzJmLWJmNTQtNGI4Ny1mYWZkLTRiNzY3Y2ExMjc1MCIsImFpZCI6IjAiLCJuZXQiOiJ0Y3AiLCJwYXRoIjoiL3dzIiwiaG9zdCI6Imx2dWZ0LmNvbSIsInRscyI6IiJ9

</details>

### 所有节点
合并节点总数: `5595`
[节点链接](https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/sub/sub_merge.txt)

### 节点来源
- [pojiezhiyuanjun/freev2](https://github.com/pojiezhiyuanjun/freev2), 节点数量: `114`
- [chfchf0306/clash](https://github.com/chfchf0306/clash), 节点数量: `448`
- [xiyaowong/freeFQ](https://github.com/xiyaowong/freeFQ), 节点数量: `177`
- [freefq/free](https://github.com/freefq/free), 节点数量: `52`
- [learnhard-cn/free_proxy_ss](https://github.com/learnhard-cn/free_proxy_ss), 节点数量: `99`
- [vpei/Free-Node-Merge](https://github.com/vpei/Free-Node-Merge), 节点数量: `100`
- [colatiger/v2ray-nodes](https://github.com/colatiger/v2ray-nodes), 节点数量: `87`
- [oslook/clash-freenode](https://github.com/oslook/clash-freenode), 节点数量: `42`
- [ssrsub/ssr](https://github.com/ssrsub/ssr), 节点数量: `71`
- [Leon406/SubCrawler](https://github.com/Leon406/SubCrawler), 节点数量: `3108`
- [yu-steven/openit](https://github.com/yu-steven/openit), 节点数量: `96`
- [iwxf/free-v2ray](https://github.com/iwxf/free-v2ray), 节点数量: `39`
- [gooooooooooooogle/Clash-Config](https://github.com/gooooooooooooogle/Clash-Config), 节点数量: `1`
- [Jsnzkpg/Jsnzkpg](https://github.com/Jsnzkpg/Jsnzkpg), 节点数量: `60`
- [ermaozi/get_subscribe](https://github.com/ermaozi/get_subscribe), 节点数量: `40`
- [wrfree/free](https://github.com/wrfree/free), 节点数量: `52`
- [GreenFishStudio/GreenFish](https://github.com/GreenFishStudio/GreenFish), 节点数量: `56`
- [changfengoss](https://github.com/ronghuaxueleng/get_v2), 节点数量: `0`
- [anaer/Sub](https://github.com/anaer/Sub), 节点数量: `239`
- [xrayfree/free-ssr-ss-v2ray-vpn-clash](https://github.com/xrayfree/free-ssr-ss-v2ray-vpn-clash), 节点数量: `4`
- [mhmhone/shadowrocket-free-subscribe](https://github.com/mhmhone/shadowrocket-free-subscribe), 节点数量: `46`
- [aiboboxx/v2rayfree](https://github.com/aiboboxx/v2rayfree), 节点数量: `53`
- [moneyfly1/sublist](https://github.com/moneyfly1/sublist), 节点数量: `435`
- [Pawdroid/Free-servers](https://github.com/Pawdroid/Free-servers), 节点数量: `27`
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