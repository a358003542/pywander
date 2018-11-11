# bihu

bihu通用模块，代码版权归cdwanze所有。



## 安装
```
pip install bihu
```



## TODO
- 移除dynaconf强制依赖，不再考虑数据库实际连接参数，只接受一个sqlalchemy的通用url表示了。

- 算法等各个问题继续丰富

- ml机器学习部分 在编写的时候，一方面要考虑轻耦合，各个接口各个层次都是开放的，可用的，另一方面考虑 pandas matplotlib keras等等工具更紧密的继承。

- plot_utils 绘图功能


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



## 更新说明



## TODO
