
import  unittest
import HTMLTestRunnerNew
suite=unittest.TestSuite()
from python_study.zuoye.zuoye_21.common import contants
from python_study.zuoye.zuoye_21.testcases import test1_register
from python_study.zuoye.zuoye_21.testcases import test_recharge
from python_study.zuoye.zuoye_21.testcases import test_invest
import time
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test1_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_invest))

curTime = time.strftime("%Y-%m-%d", time.localtime())
file1= contants.testreport_file.format(curTime)
print(file1)

with open(file1,'wb+'):
  runner=HTMLTestRunnerNew.HTMLTestRunner( stream=file1,verbosity=1,title='接口请求测试报告',description='接口用例',tester='老王')
  runner.run(suite)

