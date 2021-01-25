## datetime_helper
need the `dateutil` module.

- is_same_year 输入两个datetime 对象，判断是否是同一年
- is_same_month  判断两个datetime对象是否是同一月
- is_same_day 判断两个datetime对象是否是同一天
- is_same_hour 判断两个datetime对象是否是同一时
- round_to_day     datetime对象round到天，其他归零
- round_to_hour datetime对象round到小时，更小的刻度归零
- round_to_minute  datetime对象round到分钟
- round_to_second datetime对象round到秒

- get_date_range 返回一个时间片列表，以当前时间为终点，向前数几个月
```
from utils.date_utils import get_date_range
get_date_range(5)
Out[3]:
[datetime.datetime(2018, 10, 7, 2, 7, 1),
 datetime.datetime(2018, 11, 7, 2, 7, 1),
 datetime.datetime(2018, 12, 7, 2, 7, 1),
 datetime.datetime(2019, 1, 7, 2, 7, 1),
 datetime.datetime(2019, 2, 7, 2, 7, 1),
 datetime.datetime(2019, 3, 7, 2, 7, 1)]
```

- normal_format_now  标准格式 now '2018-12-21 15:39:20'

- normal_format_utcnow

- get_timestamp 获得当前的timestamp

- get_dt_fromtimestamp 根据timestamp获得对应的datetime对象







