
import re
from python_study.zuoye.zuoye_20.common.config import doconfig
# 数据从excel传到替换方法替换成配置文件的数据
def replace(data):  #查找替换类
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        # print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        v = doconfig.get('data', g)  # 根据KEY取配置文件里面的值
        # print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)  # 查找替换,count查找替换的次数

    return data
# data='{"mobilephone":"#login_user#","pwd":"#login_pwd#"}'
# newdata=replace(data)
# print(newdata)
