
import unittest

from ddt import ddt, data

from python_study.zuoye import Context
from python_study.zuoye import context
from python_study.zuoye.zuoye_22.common import contants
from python_study.zuoye.zuoye_22.common import do_excel
from python_study.zuoye.zuoye_22.common import do_mysql
from python_study.zuoye.zuoye_22.common.http_request import HTTPRequest2


@ddt
class InvestTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'invest')
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
    @data(*cases)
    def test_invest(self, case):
        print('测试标题:',case.title)
        if case.sql:
            sql = eval(case.sql)['sql1']  # 将数据库的sql转成字典，然后根据key取sql,查出需要的值进行数据库校验
            member = self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            before = member['leaveamount']
            print('投资前金额',before)
            before=int(before)
        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
            # 判断加标成功之后，查询数据库，取到loan_id
            if resp.json()['msg'] == "加标成功":
                sql = "select id from future.loan where memberid = 1008 order by id desc limit 1"
                loan_id = self.mysql.fetch_one(sql)['id']
                print('标的ID：', loan_id)
                # 保存到类属性里面
                setattr(Context, "loan_id", str(loan_id))  #反射
            if case.sql:       #数据库校验
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql) #再次查询数据库，查出请求之后的值，进行数据库校验
                print(member['leaveamount'])
                after = member['leaveamount']
                print('投资后金额',after)
                invest_amount = int(eval(case.data)['amount'])  # 投资金额
                self.assertEqual(before - invest_amount, after)
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
