# A-Soul评论区信息爬取
利用python爬取A-Soul出道视频（BV1my4y167r7）评论区，并进行轻量可视化分析（个人练习python程序设计以及爬虫）

主要利用到`json`，`request`等包进行原始信息爬取。
## 功能介绍
`get_replies.py`主要获取api接口中的原始数据，并将其以`.json`格式保存，以便之后使用。本视频使用的url为`https://api.bilibili.com/x/v2/reply/main?next={:d}&type=1&oid=797915674&mode=3&plat=1`,除去了控制台中不必要的一部分片段。b站目前评论区前端为滚动加载模式，每次加载20条评论，在爬取时更改`{:d}`部分可以达到类似于翻页的效果。

咕了，剩下的回头再写
