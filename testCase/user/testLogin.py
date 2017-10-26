# encoding=utf-8
import unittest
import paramunittest
from common import common
from common import configDE
from common.Log import Log as Log
from pageobjects.LoginIn_homepage import HomePage

log = Log(logger="testLogin")
login_xls = common.get_xls("userCase.xlsx", "login")


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):

    def setParameters(self, case_name):
        self.case_name = str(case_name)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        log.build_start_line(self.case_name)
        self.browse = configDE.DriverEngine()
        self.driver = self.browse.open_driver()

    def testLogin(self):
        # 这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        self.homepage = HomePage(self.driver)
        self.homepage.send_number1()  # 调用页面对象中的方法
        self.homepage.send_number2()
        self.homepage.sleep(2)

    def tearDown(self):
        self.driver.quit()
        log.build_end_line(self.case_name)
