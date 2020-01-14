# my_python_module


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

#### df_utils
pandas的DataFrame对象的一些便捷操作函数

- change_df_type     
输入 df column_name type

将df的某个列的类型更改为某个type 比如float等

- rename_df_columns 重新设置列名    

- rename_df_column_by_index 将index column 名字修改为 to

- rename_df_column_by_name 将某个column 名字修改为 to

- get_all_column 获取一列所有的值 默认去重

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


#### path_utils
路径处理工具

- get_project_path 返回my_python_module存放的根目录
- normalized_path 输入路径规范化 支持 '.' '~' 表达

- etc... 


