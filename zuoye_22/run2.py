
import HTMLTestRunnerNew
import sys
import unittest

sys.path.append('././././')


from python_study.zuoye.zuoye_22.common import contants

discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")


with open(contants.report_dir+ '/report.html', 'wb+') as file:
  runner=HTMLTestRunnerNew.HTMLTestRunner( stream=file,verbosity=1,title='接口请求测试报告',description='接口用例',tester='老王')
  runner.run(discover)

