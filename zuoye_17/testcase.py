import unittest
from ddt import ddt, data
from python_study.zuoye.zuoye_17.zuoye_doexcel_17 import DoExcel
from python_study.zuoye.zuoye_17.zuoye_request_17 import HttpRequest
@ddt
class LoginTest(unittest.TestCase):
    excel = DoExcel('testcases.xlsx', 'login')
    datas = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
    @data(*datas)
    def test_login(self, case):
        print(case.title)
        resp = self.http_request.Request(case.method, case.url, eval(case.data))
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'pass')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'fail')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
