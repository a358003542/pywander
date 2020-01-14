## json_helper
operation on json file. 

下面的操作有个约定，那就是json file 就是一个字典值，这通常够用了。

### write_json
将某个数据写入json文件中。

### get_json_file
获取json文件，如果json文件不存在，会自动创建一个包含空白字典值的json文件。

### get_json_data
获取json文件包含的数据。

### set_json_value
对某个json文件的某个key设置某个值。
```text
set_json_value(json_filename, k, v)
```
