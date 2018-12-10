# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 16:41
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

# com.dream.ipm
# com.dream.ipm.startup.StartupActivity
# 3HX0217415018921
# com.dream.ipm
# com.dream.ipm.startup.StartupActivity
# 3HX0217415018921
# appium 环境搭建  https://www.cnblogs.com/yoyoketang/p/6128735.html ; https://www.cnblogs.com/ydnice/p/5787800.html
# http://www.cnblogs.com/puresoul/p/4597211.html ; http://www.androiddevtools.cn/

# appium android 8.0报错修复 https://blog.csdn.net/pjl6523853/article/details/72886048
import time
from utils.mytestcase import MyTestCase
from utils.screenshort import get_screenshort


class A_Login(MyTestCase):
    
    def test_login(self):
        self.driver.find_element_by_id("com.dream.ipm:id/maintab_mycenter").click()
        dl = self.driver.find_element_by_id("com.dream.ipm:id/mycenter_text_authorize_agent").text
        print(dl)
        if dl == "切换合伙人":
            print("app已经登录成!")
        else:
            time.sleep(2)
            self.driver.find_element_by_id("com.dream.ipm:id/mycenter_img_head").click()
            time.sleep(2)
            self.driver.find_element_by_id("com.dream.ipm:id/et_normal_login_user").clear()
            self.driver.find_element_by_id("com.dream.ipm:id/et_normal_login_user").send_keys("15624992422")
            time.sleep(2)
            self.driver.find_element_by_id("com.dream.ipm:id/et_normal_login_password").clear()
            self.driver.find_element_by_id("com.dream.ipm:id/et_normal_login_password").send_keys("123456")
            time.sleep(2)
            # self.driver.hide_keyboard()
            self.driver.find_element_by_id("com.dream.ipm:id/et_normal_login_user").click()
            time.sleep(2)
            self.driver.find_element_by_id("com.dream.ipm:id/tv_normal_login_confirm").click()
            time.sleep(2)
            name = self.driver.find_element_by_id("com.dream.ipm:id/mycenter_text_username").text
            self.assertEqual(name, "ljw", "登陆失败!请检查网络或密码!")
            print("登陆成功!")
        get_screenshort(self.driver, "test_login.png")
