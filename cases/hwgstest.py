# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 18:31
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: hwgstest.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

import random
import time
from utils.mytestcase import MyTestCase
from utils.random import unicode
from utils.screenshort import get_screenshort


class Overseas(MyTestCase):
    """海外智能注册测试集"""

    def test_overseas(self):
        """海外智能推荐测试"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"智能自助注册\"]").click()
        service_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_service_price").text
        print("服务费:" + service_price)
        official_price = self.driver.find_element_by_id("com.dream.ipm:id/tv_product_official_price").text
        print("服务费:" + official_price)

        """"海外智能注册"""
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/cb_product_detail_option\" and @text=\"智能自助注册\"]").click()
        self.driver.find_element_by_id("com.dream.ipm:id/tv_product_detail_order").click()
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id=\"com.dream.ipm:id/rb_tm_apply_foreign_type\"]").click()

        """填写信息"""
        brand = unicode()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\"com.dream.ipm:id/et_tm_apply_name\"]").send_keys(brand)
        print("商标名称:" + brand)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_tm_apply_images\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/text\" and @text=\"自动生成\"]").click()
        time.sleep(5)

        """选择智能推荐尼斯分类"""
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@resource-id=\"com.dream.ipm:id/rb_tm_apply_smart\"]").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_smart_apply_lingyu\"]").click()
        lingyu = random.randint(1, 11)
        selected = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[{}]/android.widget.TextView[1]".format(lingyu)).text
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.dream.ipm:id/lv_smart_apply_lingyu\"]/android.widget.LinearLayout[{}]".format(lingyu)).click()
        print("选择领域:" + selected)
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_smart_apply_hangye\"]").click()
        hangye = self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.dream.ipm:id/lv_smart_apply_hangye\"]/android.widget.LinearLayout[1]").click()
        print("选择行业:" + hangye)
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id=\"com.dream.ipm:id/bt_smart_apply_get_goods\"]").click()

        zongji = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_agent_apply_total_nice_price\"]").text
        print("合计:" + zongji)
        num = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_agent_apply_total_nice_num\"]").text
        print("已选择{}个商品小项".format(num))
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id=\"com.dream.ipm:id/bt_agent_apply_nice_next_step\"]").click()

        """确认订单"""
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"常用申请人\"]").click()
        # time.sleep(10)
        get_screenshort(self.driver, "test_overseas.png")

        """向下滑动屏幕"""

        # print(self.driver.get_window_size())
        # 滑动方向是相反的
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width / 2, height * 6 / 8, width / 2, height * 1 / 8, 1000)

        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\"com.dream.ipm:id/et_confirm_tm_order_notes\"]").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
        self.driver.find_element_by_xpath("//android.widget.CheckBox[@resource-id=\"com.dream.ipm:id/cb_tm_apply_document\"]").click()
        price = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.dream.ipm:id/tv_confirm_tm_order_total_price\"]").text
        print(price)
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id=\"com.dream.ipm:id/bt_confirm_tm_order_submit\"]").click()

        print("海外注册智能推荐测试通过!")