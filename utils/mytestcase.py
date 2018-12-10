# coding=utf-8
import time
import unittest
import warnings

from utils.log import Log
from appium import webdriver
from utils.pyselenium import logger


class MyTestCase(unittest.TestCase):
    """
    The base class is for all test cases. This is a father .
    """
    success = "SUCCESS   "
    fail = "FAIL   "
    logger = Log()

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        desired_caps = {'platformName': 'Android', 'deviceName': '3HX0217415018921', 'platformVersion': '8.0',
                        'appPackage': 'com.dream.ipm', 'appActivity': 'com.dream.ipm.startup.StartupActivity',
                        'unicodeKeyboard': 'True', 'resetKeyboard': 'True'}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.logger.info('###############################  END  ###############################')

    @staticmethod
    def my_print(msg):
        logger.info(msg)
