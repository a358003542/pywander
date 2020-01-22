## zhnumber

### zhnumber
输入一个数字转成一百零一这样的表达：

```text
assert zhnumber(0) == '零'
assert zhnumber(1) == '一'
assert zhnumber(15156) == '一万五千一百五十六'
assert zhnumber(101) == '一百零一'
assert zhnumber(1001) == '一千零一'
assert zhnumber(10000001) == '一千万零一'
```


### int_zhnumber
将 一百一 或者 一百零一 这样的表达 转换称为 数字

```text
assert int_zhnumber('十一') == 11
assert int_zhnumber('二十二') == 22
assert int_zhnumber('一百零三') == 103
assert int_zhnumber('三百四十五') == 345

assert int_zhnumber('1万6千') == 16000
```