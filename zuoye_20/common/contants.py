
""" 
定义数据源excel和配置文件的位置
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

excel_file = os.path.join(base_dir, 'data', 'cases.xlsx')
# print(excel_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
# print(test_file)
