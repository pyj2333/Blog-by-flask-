# 提供插件

# 1. 处理时间格式

from datetime import datetime


def init_time(time):
    """
    :return: 经过格式化的时间，2019-3-23-4:54
    """
    return time.strftime("%Y-%m-%d-%H:%M:%S")
