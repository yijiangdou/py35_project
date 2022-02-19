import unittest

from register import register


class TestRegister(unittest.TestCase):
    def test_register(self):
        """正常注册"""
        # 第一步：准备用例数据
        # 预期结果：
        excepted = {"code":1,"msg":"注册成功"}
        # 参数：data
        data = ('python35','123456','123456')
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        # 第三步：断言
        self.assertEqual(excepted,res)