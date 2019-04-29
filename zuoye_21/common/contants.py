
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
# print(case_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
# print(test_file)
testreport_file=os.path.join(base_dir, 'reports', 'testreport.html')
# print(testreport_file)