import unittest
from unittestreport import ddt,list_data
from common.handle_data import HandleExcel
from login_func import login_check
from register import register


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel(r"D:\pythonProject\py35_project\data\cases.xlsx", 'login')
    cases = excel.read_data()
    @list_data(cases)
    def test_login(self,item):
        expected = eval(item["expected"])
        params = eval(item["data"])
        row = item['case_id']+1
        res = login_check(**params)
        try:
            self.assertEqual(expected,res)
        except AssertionError as e:
            print("用例执行未通过 ")
            # 把测试结果回写道excel
            self.excel.write_data(row=row,column=5,value='未通过')
            #为了让unit test识别这条未通过的用例，咱们捕获异常之后，主动把异常抛出来
            raise e
        else:
            print("执行用例通过")
            self.excel.write_data(row=row,column=5,value='通过')

@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(r"D:\pythonProject\py35_project\data\cases.xlsx", 'register')
    cases = excel.read_data()
    @list_data(cases)
    def test_register(self,item):
        """正常注册"""
        expected = eval(item["expected"])
        params = eval(item["data"])
        row = item['case_id'] + 1
        res = login_check(*params)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print("用例执行未通过 ")
            # 把测试结果回写道excel
            self.excel.write_data(row=row, column=5, value='未通过')
            # 为了让unit test识别这条未通过的用例，咱们捕获异常之后，主动把异常抛出来
            raise e
        else:
            print("执行用例通过")
            self.excel.write_data(row=row,column=5,value='通过')
