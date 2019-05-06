
import unittest

from ddt import ddt, data

from python_study.zuoye.zuoye_22.common.do_mysql import DoMysql
from python_study.zuoye.zuoye_22.common import contants
from python_study.zuoye.zuoye_22.common import do_excel
from python_study.zuoye.zuoye_22.common.http_request import HTTPRequest2


@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'recharge')
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql = DoMysql()
    @data(*cases)
    def test_recharge(self, case):
        print(case.title)
        # 请求之前，判断是否需要执行SQL
        if case.sql:
            sql = eval(case.sql)['sql1']  #将数据库的sql转成字典，然后根据key取sql,查出需要的值进行数据库校验
            member = self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            before = member['leaveamount']

        resp = self.http_request.request(case.method, case.url, case.data) #接着请求
        try:
            self.assertEqual(case.expected, int(resp.json()['code']))
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
            # 成功之后，判断是否需要执行SQL
            if case.sql:       #数据库校验
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql) #再次查询数据库，查出请求之后的值，进行数据库校验
                print(member['leaveamount'])
                after = member['leaveamount']
                recharge_amount = int(eval(case.data)['amount'])  # 充值金额
                self.assertEqual(before + recharge_amount, after)
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
