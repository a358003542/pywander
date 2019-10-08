## text_helper

### int_number
类似于 int_zhnumber ，不过增加了数字字符串的支持。

### guess_chapter_id
如果字符串里面有 第十一章 这样的文字，将返回 11 ，否则将抛出 GuessFailed 异常

### guess_volume_id
如果字符串里面有 第二卷 这样的文字，将返回 2，否则将抛出 GuessFailed 异常。