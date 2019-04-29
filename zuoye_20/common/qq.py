
# import re
# from python_study.zuoye.zuoye_20.common import config
# from python_study.zuoye.zuoye_20.common.config import doconfig
# p = "#(.*?)#"
# data='{"mobilephone":"#login_user#","pwd":"#login_pwd#"}'
# while re.search(p, data):
#     m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object对象, 如果没有找None
#     # print(m.group())
#     # print(m.group(1))
#     # print(type(m.group(0)))
#     # print(type(m.group(1)))
#     g=m.group(1)
#     x=config.doconfig.get('data',g)
#     data=re.sub(p,x,data,count=1)
#     # print(n)
# print(data)

s='{"mobilephone": "register_mobile", "pwd": "register_pwd"}'
s=s.replace(',', '123')
print(s)

s='Hello'
s=s.replace('H','w')
print(s)