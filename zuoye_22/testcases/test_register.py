
import random
import unittest

from ddt import ddt, data

from python_study.zuoye import get_logger
from python_study.zuoye.zuoye_22.common import contants
from python_study.zuoye.zuoye_22.common import do_excel
from python_study.zuoye.zuoye_22.common import do_mysql
from python_study.zuoye.zuoye_22.common.http_request import HTTPRequest2


@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'register')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
    @data(*cases)
    def test_register(self, case):
        get_logger('CASE').info('测试标题:{}'.format(case.title))
        if case.sql:
            sql = eval(case.sql)['sql1']
            max_phone = self.mysql.fetch_one(sql)['max(mobilephone)'] # 查询最大手机号码
            print(max_phone)
            register_phone=int(max_phone)-random.randint(1,1000)
            case.data = case.data.replace('register_mobile', str(register_phone))
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
          if resp.json()['msg']=='手机号码已被注册':
            print('上诉校验成功')
          self.assertEqual(case.expected, resp.text)
          self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
          self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
          get_logger('CASE').error("报错了，{0}".format(e))
          raise e
    get_logger('CASE').info('测试后置处理')
    @classmethod
    def tearDownClass(cls):

        cls.http_request.close()
        cls.mysql.close()
