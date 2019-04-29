# -*- coding:utf-8 _*-
""" 

"""
import unittest
from ddt import ddt, data
from python_study.zuoye.zuoye_20.common import contants #导入获取文件位置类
from python_study.zuoye.zuoye_20.common import do_excel  #导入获取excel数据类
from python_study.zuoye.zuoye_20.common.config import doconfig #导入获取配置文件数据类
from python_study.zuoye.zuoye_20.common import context #导入替换类
from python_study.zuoye.zuoye_20.common.http_request import HTTPRequest2 #导入请求接口类

@ddt
class AddTest(unittest.TestCase): #添加标的类
    excel = do_excel.DoExcel(contants.excel_file, 'add')
    datas = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
    @data(*datas)
    def test_add(self, case):
        case.data = context.replace(case.data)    #添加标的测试类是 ,把excel的数据替换成配置文件里面的数据
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_result(case.case_id + 1, resp.json()['code'], 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.json()['code'], 'FAIL')
            raise e
        return resp
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
