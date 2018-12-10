# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 10:29
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: bmkstest.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

import time
from utils.mytestcase import MyTestCase
from utils.screenshort import get_screenshort


class Nanny(MyTestCase):
    """保姆注册测试集"""

    def test_nanny(self):
        """保姆快速注册测试"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"保姆快速注册\"]").click()
        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        """选择保姆注册"""
        # self.driver.find_element_by_id("com.dream.ipm:id/cb_product_detail_option").click()
        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_detail_order").click()

        """确认订单填写信息"""
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()

        """确认支付"""
        total_price = str(self.driver.find_element_by_id("com.dream.ipm:id/tv_order_pay_total_price_bottom").text).replace("¥", "")
        print("应付总额:" + total_price)
        self.assertEqual(total_price, str(600.0), "金额异常请检查!")
        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        get_screenshort(self.driver, "test_nanny.png")
        print("保姆注册测试通过!")
