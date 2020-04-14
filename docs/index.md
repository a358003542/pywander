# my_python_module
a general purpose python module.

## algorithms算法部分
个人学习算法的一些积累 没有太大实用价值 可做学习时的参考

## compat
python2和python3兼容性模块 历史原因保留在这里 并没怎么用了 


### utils部分
utils里面有很多便捷的函数支持。 

TODO utils文件夹里面的部分重要性偏低一点。

#### admin_utils
提升管理员权限工具 admin_utils 用于在windows下提升脚本运行权限

- is_admin 判断是否是管理员权限
- run_as_admin 已管理员方式运行本脚本


- airflow_utils 对最小时间片的单个任务提供额外的运行状态记录支持


#### dll_utils
介绍了如何利用python对接dll文件

#### encrypt_utils
加密解密

- pbkdf2_sha256 加密
- encrypt_message 加密某个信息
- decrypt_message 解密某个信息


#### file_utils
- bigfile_read 大文件读写模式


#### id_utils

- build_query_id
唯一id生成 
根据关键和某个字典参数 生成 唯一的文件名或者唯一的id等等


