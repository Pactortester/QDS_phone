# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:19
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: start.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

# import random
# import re
# import time
#
# from selenium import webdriver

# import re
# import random
# import sys
# import time
# import datetime
# import threading
#
# from random import choice
# import requests
# import bs4
# from urllib3.connectionpool import xrange
#
#
# def get_ip():
#     """获取代理IP"""
#     url = "http://www.xicidaili.com/nn"
#     headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
#                 "Accept-Encoding":"gzip, deflate, sdch",
#                 "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
#                 "Referer":"http://www.xicidaili.com",
#                 "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
#                 }
#     r = requests.get(url,headers=headers)
#     soup = bs4.BeautifulSoup(r.text, 'html.parser')
#     data = soup.table.find_all("td")
#     ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
#     port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
#     ip = re.findall(ip_compile,str(data))       # 获取所有IP
#     port = re.findall(port_compile,str(data))   # 获取所有端口
#     return [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080
# # 设置 user-agent列表，每次请求时，可在此列表中随机挑选一个user-agnet
# uas = [
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
#     "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
#     "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
#     "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
#     ]
# def get_url(code=0,ips=[]):
#     """
#         投票
#         如果因为代理IP不可用造成投票失败，则会自动换一个代理IP后继续投
#     """
#     try:
#         ip = choice(ips)
#     except:
#         return False
#     else:
#         proxies = {
#             "http":ip,
#         }
#         headers2 = { "Accept":"text/html,application/xhtml+xml,application/xml;",
#                         "Accept-Encoding":"gzip, deflate, sdch",
#                         "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
#                         "Referer":"",
#                         "User-Agent":choice(uas),
#                         }
#     try:
#         num = random.uniform(0,1)
#         hz_url = "http://www.xxxxx.com/xxxx%s" % num   # 某投票网站的地址，这里不用真实的域名
#         hz_r = requests.get(hz_url,headers=headers2,proxies=proxies)
#     except requests.exceptions.ConnectionError:
#         print ("ConnectionError")
#         if not ips:
#             print ("not ip")
#             sys.exit()
#         # 删除不可用的代理IP
#         if ip in ips:
#             ips.remove(ip)
#         # 重新请求URL
#         get_url(code,ips)
#     else:
#         date = datetime.datetime.now().strftime('%H:%M:%S')
#         print (u"第%s次 [%s] [%s]：投票%s (剩余可用代理IP数：%s)" % (code,date,ip,hz_r.text,len(ips)))
# ips = []
# for i in xrange(6000):
#     # 每隔1000次重新获取一次最新的代理IP，每次可获取最新的100个代理IP
#     if i % 1000 == 0:
#         ips.extend(get_ip())
#     # 启用线程，隔1秒产生一个线程，可控制时间加快投票速度 ,time.sleep的最小单位是毫秒
#     t1 = threading.Thread(target=get_url,args=(i,ips))
#     t1.start()
#     time.sleep(1)
# import random
# suiji=random.randint(2, 46)
# print(suiji-1)
# print(suiji)

# -*- coding: utf-8 -*-
# import random
# import time, re
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# #from PIL import Image
# import requests
# from io import BytesIO
#
#
# class HuXiu(object):
#     def __init__(self):
#         chrome_option = webdriver.ChromeOptions()
#         # chrome_option.set_headless()
#
#         self.driver = webdriver.Chrome(executable_path=r"/usr1/webdrivers/chromedriver", chrome_options=chrome_option)
#         self.driver.set_window_size(1440, 900)
#
#     def visit_index(self):
#         self.driver.get("https://www.huxiu.com/")
#
#         WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="js-register"]')))
#         reg_element = self.driver.find_element_by_xpath('//*[@class="js-register"]')
#         reg_element.click()
#
#         WebDriverWait(self.driver, 10, 0.5).until(
#             EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_slider_knob gt_show"]')))
#
#         # 进入模拟拖动流程
#         self.analog_drag()
#
#     def analog_drag(self):
#         # 鼠标移动到拖动按钮，显示出拖动图片
#         element = self.driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
#         ActionChains(self.driver).move_to_element(element).perform()
#         time.sleep(3)
#
#         # 刷新一下极验图片
#         element = self.driver.find_element_by_xpath('//a[@class="gt_refresh_button"]')
#         element.click()
#         time.sleep(1)
#
#         # 获取图片地址和位置坐标列表
#         cut_image_url, cut_location = self.get_image_url('//div[@class="gt_cut_bg_slice"]')
#         full_image_url, full_location = self.get_image_url('//div[@class="gt_cut_fullbg_slice"]')
#
#         # 根据坐标拼接图片
#         cut_image = self.mosaic_image(cut_image_url, cut_location)
#         full_image = self.mosaic_image(full_image_url, full_location)
#
#         # 保存图片方便查看
#         cut_image.save("cut.jpg")
#         full_image.save("full.jpg")
#
#         # 根据两个图片计算距离
#         distance = self.get_offset_distance(cut_image, full_image)
#
#         # 开始移动
#         self.start_move(distance)
#
#         # 如果出现error
#         try:
#             WebDriverWait(self.driver, 5, 0.5).until(
#                 EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_ajax_tip gt_error"]')))
#             print("验证失败")
#             return
#         except TimeoutException as e:
#             pass
#
#         # 判断是否验证成功
#         try:
#             WebDriverWait(self.driver, 10, 0.5).until(
#                 EC.element_to_be_clickable((By.XPATH, '//div[@class="gt_ajax_tip gt_success"]')))
#         except TimeoutException:
#             print("again times")
#             time.sleep(5)
#             # 失败后递归执行拖动
#             self.analog_drag()
#         else:
#             # 成功后输入手机号，发送验证码
#             self.register()
#
#     # 获取图片和位置列表
#     def get_image_url(self, xpath):
#         link = re.compile('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;')
#         elements = self.driver.find_elements_by_xpath(xpath)
#         image_url = None
#         location = list()
#         for element in elements:
#             style = element.get_attribute("style")
#             groups = link.search(style)
#             url = groups[1]
#             x_pos = groups[2]
#             y_pos = groups[3]
#             location.append((int(x_pos), int(y_pos)))
#             image_url = url
#         return image_url, location
#
#     # 拼接图片
#     def mosaic_image(self, image_url, location):
#         resq = requests.get(image_url)
#         file = BytesIO(resq.content)
#         img = Image.open(file)
#         image_upper_lst = []
#         image_down_lst = []
#         for pos in location:
#             if pos[1] == 0:
#                 # y值==0的图片属于上半部分，高度58
#                 image_upper_lst.append(img.crop((abs(pos[0]), 0, abs(pos[0]) + 10, 58)))
#             else:
#                 # y值==58的图片属于下半部分
#                 image_down_lst.append(img.crop((abs(pos[0]), 58, abs(pos[0]) + 10, img.height)))
#
#         x_offset = 0
#         # 创建一张画布，x_offset主要为新画布使用
#         new_img = Image.new("RGB", (260, img.height))
#         for img in image_upper_lst:
#             new_img.paste(img, (x_offset, 58))
#             x_offset += img.width
#
#         x_offset = 0
#         for img in image_down_lst:
#             new_img.paste(img, (x_offset, 0))
#             x_offset += img.width
#
#         return new_img
#
#     # 判断颜色是否相近
#     def is_similar_color(self, x_pixel, y_pixel):
#         for i, pixel in enumerate(x_pixel):
#             if abs(y_pixel[i] - pixel) > 50:
#                 return False
#         return True
#
#     # 计算距离
#     def get_offset_distance(self, cut_image, full_image):
#         for x in range(cut_image.width):
#             for y in range(cut_image.height):
#                 cpx = cut_image.getpixel((x, y))
#                 fpx = full_image.getpixel((x, y))
#                 if not self.is_similar_color(cpx, fpx):
#                     img = cut_image.crop((x, y, x + 50, y + 40))
#                     # 保存一下计算出来位置图片，看看是不是缺口部分
#                     img.save("1.jpg")
#                     return x
#
#     # 开始移动
#     def start_move(self, distance):
#         element = self.driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
#
#         # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
#         distance -= element.size.get('width') / 2
#         distance += 15
#
#         # 按下鼠标左键
#         ActionChains(self.driver).click_and_hold(element).perform()
#         time.sleep(0.5)
#         while distance > 0:
#             if distance > 10:
#                 # 如果距离大于10，就让他移动快一点
#                 span = random.randint(5, 8)
#             else:
#                 # 快到缺口了，就移动慢一点
#                 span = random.randint(2, 3)
#             ActionChains(self.driver).move_by_offset(span, 0).perform()
#             distance -= span
#             time.sleep(random.randint(10, 50) / 100)
#
#         ActionChains(self.driver).move_by_offset(distance, 1).perform()
#         ActionChains(self.driver).release(on_element=element).perform()
#
#     def register(self):
#         element = self.driver.find_element_by_xpath('//input[@id="sms_username"]')
#         element.clear()
#         element.send_keys("17801188215")
#
#         ele_captcha = self.driver.find_element_by_xpath('//span[@class="js-btn-captcha btn-captcha"]')
#         ele_captcha.click()
#
#
# if __name__ == "__main__":
#     h = HuXiu()
#     h.visit_index()



# import re
# string = "127米"
# #print (re.findall(r"\d+\.?\d*", string))
#
# aa=re.findall(r"\d+\.?\d*", string)
# print(aa)
# totalCount = '已为您检索到19条近似商标'
#
# totalCount = re.sub("\D","",totalCount)
#
# print(totalCount)
# from config.globalparam import report_path, img_path
# from utils.random import unicode, patent_number
# from selenium import webdriver
#
# print("包针雨我爱你！")
# s = unicode()
# a = len(s)
# print(a)
# print(s)
#
# print(report_path)
# print(img_path)
#
# print(patent_number())
#
#
# driver = webdriver.PhantomJS()
# driver.get('https://blog.csdn.net/xm_csdn/article/details/72636381')

# suite = unittest.defaultTestLoader.discover("G:\\QDS_company\\case\\", "*test.py")
# unittest.TextTestRunner().run(suite)
# path = os.path.dirname(__file__)
import random
import urllib

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import unittest
from utils.screenshort import get_screenshort

#
# class test(unittest.TestCase):
#
#     def test_bd(self):
#         chrome_options = Options()
#         chrome_options.add_argument('--headless')
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get("http://www.baidu.com")
#         driver.set_window_size(1920, 1080)
#         time.sleep(2)
#         print(driver.get_window_position())
#         print(driver.get_window_size())
#         print(driver.get_window_rect())
#
#         get_screenshort(driver, "test.png")
#
#         time.sleep(10)
#         driver.close()
#
#
# if __name__ == "__main__":
#     unittest.main()

#
# 不愿染是与非 怎料事与愿违
# 心中的花枯萎 时光它去不回
# 回忆辗转来回 痛不过这心扉
# 愿只愿余生无悔 随花香远飞
#

# !/usr/bin/env python
# encoding: utf-8
# '''
# 1、读取指定目录下的所有文件
# 2、读取文件，正则匹配出需要的内容，获取文件名
# 3、打开此文件(可以选择打开可以选择复制到别的地方去)
# '''
# import os.path
# import re
#
#
# def eachfile(filepath):
#     pathdir = os.listdir(filepath)
#     for allDir in pathdir:
#         child = os.path.join('%s\%s' % (filepath, allDir))
#         if os.path.isfile(child):
#             readfile(child)
#             # print(child)
#             continue
#         eachfile(child)
#
#
# def readfile(filenames):
#     fopen = open(filenames, 'r')  # r 代表read
#     fileread = fopen.read()
#     fopen.close()
#     t = re.search(r'title', fileread)  # 寻找的内容
#     if t:
#         print("匹配到的文件是:"+filenames)
#         arr.append(filenames)
#
#
# if __name__ == "__main__":
#     filenames = 'D:\\10.15'  # 目标文件夹
#     arr = []
#     eachfile(filenames)

# from utils.datachoice import xz
#
# print(xz("驰名商标.txt"))



# coding:utf-8
# 本实例用于获取糗事百科热门的文章内容和好评数量。
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
# 糗事百科需要设置MIME头才能正常请求，不需要登陆，也不需要cookie
print('=======================糗事百科数据挖掘==========================')

urlstr = "https://www.qiushibaike.com/8hr/page/%d"


data = {}


def getdata(html):  # 从字符串中安装正则表达式获取值
    soup = BeautifulSoup(html, 'html.parser')
    alldiv = soup.find_all("div", class_="content")   # 内容的外部div
    allnum = soup.find_all("span", class_="stats-vote")  # 点赞数量的外部span
    for i in range(0,len(alldiv)):
        print(str(alldiv[i].find_all('span')[0]).replace('<span>','').replace('</span>','').replace('<br/>','\r\n').strip())  # 内容文字，使用string在文字里还有<br/>时，无法打印，使用text会省略调用<br/>
        print(allnum[i].find_all('i')[0].string)  # 好评数量


# 根据一个网址，获取该网址中符合指定正则表达式的内容

def craw(url):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent' : user_agent}  # 设置MIME头，糗事百科对这个进行了验证
        request = urllib.request.Request(url,headers=headers)  # 创建一个请求
        response = urllib.request.urlopen(request)  # 获取响应
        html = response.read()  # 读取返回html源码
        getdata(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


for i in range(1,14):
    url = urlstr % i
    print(url)
    craw(url)