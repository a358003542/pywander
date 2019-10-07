## common

### humanize_bytes

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