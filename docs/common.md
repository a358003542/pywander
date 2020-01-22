## common

### humanize_bytes
make the bytes more human readable.
```text
>>> humanize_bytes(1)
'1 B'
>>> humanize_bytes(1024)
'1.0 KiB'
>>> humanize_bytes(1024 * 123)
'123.0 KiB'
>>> humanize_bytes(1024 * 12342)
'12.1 MiB'
```

### beep
make a sound, first arg is frequency, and the second arg is duration.

```text
beep(300,1)
```

### str2pyobj
use ast module convert some string to python object. this is a safe solution, do not use the eval.

```
x = str2pyobj('{"a":1}')
assert isinstance(x, dict)
```

### str2num
a very old school conversion, but in some case maybe it is useful.

```text
>>> str2num('565')
565
>>> str2num('565.55')
565.55
>>> str2num('565.55a')
raise ValueError
```