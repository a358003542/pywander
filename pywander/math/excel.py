from datetime import datetime

try:
    import numpy as np
except ImportError as e:
    raise ImportError("请运行: pip install pywander[math]") from e



def to_excel_int_time(dt):
    """
    接受datetime对象，将其转成excel内部存储的整数。
    """
    excel_date_modify_factor = datetime(1900, 1, 1).toordinal() - 2
    excel_int_time = dt.toordinal() - excel_date_modify_factor
    return excel_int_time

to_excel_int_time_v = np.vectorize(to_excel_int_time)


