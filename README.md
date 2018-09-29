# bihu

bihu通用模块，代码版权归cdwanze所有。


## 安装
```
pip install bihu
```

## 文档

<https://cdwanze.github.io/articles/bihu-module.html>




## 功能简介

1. web 里面有获取随机user-agent函数等其他辅助函数。

2. workflow里面写了一个状态控制类，在airflow调度的时候，最小的任务执行仍然有状态记录。

3. database 里面放着很多便捷的对接数据库的通用操作模式。具体请读者用心体会。

4. utils里面有很多便捷的函数支持。
  - 提升管理员权限工具
  - 日期工具
  - 日志工具
  - 路径处理工具
  - 文本处理工具
  - 注册表读写工具

5. algorithms 一些简单的算法实现，就不赘述了

5. ml 机器学习相关，特色是和pandas等工具更加紧密的集成
 - knn


## 项目配置管理

本项目开发遵循12因素应用配置管理原则：

1. .env 不进入版本库，控制整个项目的配置选择，目前选用了三个阶段： development testing production，分别对应于 本机早期开发， 实际上机测试  和 生产环境
2. .secrets.toml 里面放着一些私密的配置信息，不进入版本库
3. settings.toml 里面放着其他一些配置

使用请参看 dynaconf 模块。


## 更新说明



## TODO
