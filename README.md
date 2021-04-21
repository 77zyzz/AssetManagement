目前市面上优秀的资产探测软件众多，但个人在资产管理或挖掘src漏洞时候，不同资产探测软件的探测结果通常用excel或txt来将进行汇总，比较麻烦。
本资产管理系统，专注且只专注于资产管理，并包含一些便于资产整理的小工具（txt去重、ip段ip互转等），不会包括资产资产发掘模块，摆脱用excel整理资产的困境（excel plus）。


主要技术
django+simpleui+pandas


数据库字段名
主机资产表host_assets

| 厂商 | company |
| --- | --- |
| IP | ip |
| 端口 | port |
| 服务 | service |
| banner | banner |
| 描述 | describe |

web资产表web_assets

| 厂商 | company |
| --- | --- |
| URL | url |
| 系统名称 | webtitle |
| 指纹 | finger |
| 描述 | describe |

todo:
数据批量导入模块
优化小工具ui
ip段ip互转小工具

