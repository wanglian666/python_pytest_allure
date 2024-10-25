# 存放被测项目基本信息，如URL地址等

import os

# 获取项目根路径
current_file_name = __file__;
BASE_PATH = os.path.dirname(current_file_name)
print('BASE_PATH:', BASE_PATH)

# 设置项目环境域名
BASE_URL = "http://kdtx-test.itheima.net"