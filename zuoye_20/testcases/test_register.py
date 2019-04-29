
# 参数化的过程主要分为三步：
#
# >> 在Excel中将需要进行参数化的值改成一个参数值，主要起一个标识的作用
#
# >> 在用例中，请求之前判断请求Data中是否有参数化的标识，如果有，就进去下一步替换，如果没有，就不需要替换
#
# >> 将参数值替换成数据库/配置文件里面取到的值
#
#
#
# 1，练习掌握pymsql的使用，（与数据库进行交互的7步）
#
# 2，编写一个Do_Mysql的类来完成，数据库建立连接，查询，和关闭连接。其中连接参数，从配置文件里面读取！！！
#
# 3，完成成功注册手机号码参数化的过程。
import unittest
from ddt import ddt, data
from python_study.zuoye.zuoye_20.common import contants #导入获取文件位置类
from python_study.zuoye.zuoye_20.common import do_excel  #导入获取excel数据类
# from python_study.zuoye.zuoye_20.common.config import doconfig #导入获取配置文件数据类
from python_study.zuoye.zuoye_20.common import context #导入替换类
from python_study.zuoye.zuoye_20.common.http_request import HTTPRequest2 #导入请求接口类
from python_study.zuoye.zuoye_20.common import do_mysql

@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.excel_file, 'register')
    datas = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
    @data(*datas)
    def test_register(self, case):
        if case.data.find('register_mobile') > -1:  # 判断参数化的标识
            sql = 'select min(mobilephone) from future.member'
            max_phone = self.mysql.fetch_one(sql)[0]  # 查询最大手机号码
            # 最大手机号码+1
            print(max_phone)
            max_phone = int(max_phone) + 111111
            print('最大手机号码', max_phone)
            print(type(case.data))
            # replace方法是特换之后重新返回一个新的字符串，所以需要使用case.data重新接收
            case.data = case.data.replace('register_mobile', str(max_phone))  # 特换参数值
#注册测试类 ,是把数据库查找到的数据加一替换成excel里面的数据
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
















