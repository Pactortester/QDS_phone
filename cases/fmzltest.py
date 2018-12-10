# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 9:18
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: fmzltest.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

import time
from utils.mytestcase import MyTestCase
from utils.screenshort import get_screenshort


class Patent(MyTestCase):
    """发明专利测试集"""

    def test_invention_patent_bz_1(self):
        """发明专利标准_单个人"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利标准申请\"]").click()

        """选择标准"""
        # 默认标准申请
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"单个申请人减缓\"]").click()

        """打印费用"""
        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        # 点击立即办理
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_product_detail_order\"]").click()

        """确认订单填写信息"""
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        total_price_1 = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text
        total_price = str(
            self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text).replace("￥", "")

        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()

        """确认支付"""

        print("应付总额:" + total_price)
        self.assertEqual(total_price, str(4559.0), "金额异常请检查!")

        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_order_pay_total_price_bottom\"]").text
        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        time.sleep(2)
        get_screenshort(self.driver, "test_invention_patent_bz_1.png")

        self.assertEqual(total_price_1, price, "金额异常请检查!")
        print("发明专利标准_单个人申请测试通过!")

    def test_invention_patent_bz_2(self):
        """发明专利标准_多个人"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利标准申请\"]").click()

        """选择标准"""
        # 默认标准申请
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"多个申请人减缓\"]").click()

        """打印费用"""
        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        # 点击立即办理
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_product_detail_order\"]").click()

        # """确认订单填写信息"""
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")
        #
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")
        #
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")
        #
        # self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        total_price_1 = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text

        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()

        """确认支付"""

        print("应付总额:" + total_price_1)

        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_order_pay_total_price_bottom\"]").text

        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        get_screenshort(self.driver, "test_invention_patent_bz_2.png")

        self.assertEqual(total_price_1, price, "金额异常请检查!")
        print("发明专利标准_多个人申请测试通过!")

    def test_invention_patent_bz_3(self):
        """发明专利标准_不减缓"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利标准申请\"]").click()

        """选择标准"""
        # 默认标准申请
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"不减缓\"]").click()

        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        # 点击立即办理
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_product_detail_order\"]").click()

        """确认订单填写信息"""
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        total_price_1 = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text
        total_price = str(
            self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text).replace("￥", "")

        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()

        """确认支付"""

        print("应付总额:" + total_price)
        self.assertEqual(total_price, str(7449.0), "金额异常请检查!")

        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_order_pay_total_price_bottom\"]").text

        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        get_screenshort(self.driver, "test_invention_patent_bz_3.png")

        self.assertEqual(total_price_1, price, "金额异常请检查!")
        print("发明专利标准_不减缓申请测试通过!")

    def test_invention_patent_db_1(self):
        """发明专利标准_单个人"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利标准申请\"]").click()

        """选择标准"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利担保申请\"]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"单个申请人减缓\"]").click()

        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        # 点击立即办理
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_product_detail_order\"]").click()

        """确认订单填写信息"""
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        total_price_1 = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text
        total_price = str(
            self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text).replace("￥", "")

        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()

        """确认支付"""

        print("应付总额:" + total_price)
        self.assertEqual(total_price, str(9559.0), "金额异常请检查!")
        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_order_pay_total_price_bottom\"]").text

        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        get_screenshort(self.driver, "test_invention_patent_db_1.png")

        self.assertEqual(total_price_1, price, "金额异常请检查!")
        print("发明专利担保_单个人申请测试通过!")

    def test_invention_patent_db_2(self):
        """发明专利标准_多个人"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利标准申请\"]").click()

        """选择标准"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利担保申请\"]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"多个申请人减缓\"]").click()

        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        # 点击立即办理
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_product_detail_order\"]").click()

        """确认订单填写信息"""
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        total_price_1 = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text
        total_price = str(
            self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text).replace("￥", "")

        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()
        time.sleep(5)
        """确认支付"""

        print("应付总额:" + total_price)
        self.assertEqual(total_price, str(10069.0), "金额异常请检查!")
        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_order_pay_total_price_bottom\"]").text

        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        get_screenshort(self.driver, "test_invention_patent_bd_2.png")

        self.assertEqual(total_price_1, price, "金额异常请检查!")
        print("发明专利担保_多个人申请测试通过!")

    def test_invention_patent_db_3(self):
        """发明专利标准_不减缓"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利标准申请\"]").click()

        """选择标准"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"发明专利担保申请\"]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"不减缓\"]").click()

        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        # 点击立即办理
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_product_detail_order\"]").click()

        """确认订单填写信息"""
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_name").send_keys("test")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_tel").send_keys("15624992498")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").clear()
        self.driver.find_element_by_id("com.dream.ipm:id/et_product_contact_email").send_keys("url@email.com")

        self.driver.find_element_by_id("com.dream.ipm:id/et_product_confirm_message").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        total_price_1 = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text
        total_price = str(
            self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_total_price").text).replace("￥", "")

        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_confirm_submit").click()

        """确认支付"""

        print("应付总额:" + total_price)
        self.assertEqual(total_price, str(12449.0), "金额异常请检查!")
        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_order_pay_total_price_bottom\"]").text

        self.driver.find_element_by_id("com.dream.ipm:id/bt_order_pay_submit").click()
        get_screenshort(self.driver, "test_invention_patent_db_3.png")

        self.assertEqual(total_price_1, price, "金额异常请检查!")
        print("发明专利担保_不减缓申请测试通过!")
