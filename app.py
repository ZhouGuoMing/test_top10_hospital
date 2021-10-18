# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : app.py
import platform
import os, re
from appium import webdriver
from patient_service import Patient_Service
from exclusive_doctor import Exclusive_Doctor
from PIL import Image
import logging
import math
import operator
from functools import reduce
# 手机需root或使用安卓模拟器(默认root),分辨率设置为1440*810
#  启动前需保证手机开启usb调试且adb已连接手机
class App:
    def __init__(self):
        self.driver = None
        self.start()
    # 读取设备的udid
    def getUdid(self):
        str_init = ''
        if platform.system() == 'Windows':
            all_info = os.popen('adb devices').readlines()
        else:
            all_info = os.popen('idevice_id -l').readlines()
        for i in range(len(all_info)):
            str_init += all_info[i]
        if platform.system() == 'Windows':
            udid_list = re.findall('\n(.+?)\t', str_init, re.S)
        else:
            udid_list = re.findall('(.+?)\n', str_init, re.S)
        logging.info(f"getUdid: udid={udid_list}")
        return udid_list
    # 将两张图片尺寸和像素分布转化为直方图，并计算直方图的方差，返回两图相似度百分比
    def image_contrast(self,funname):
        img1=f"{os.getcwd()}\\expect_png\\{funname}.png"
        img2=f"{os.getcwd()}\\test_png\\test_{funname}.png"
        image1 = Image.open(img1)
        image2 = Image.open(img2)

        h1 = image1.histogram()
        h2 = image2.histogram()

        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        original_value= math.sqrt(reduce(operator.add, list(map(lambda a: a ** 2, h1))) / len(h1))
        poor=original_value - result
        percentage=poor/original_value
        logging.info(f"image_contrast: 相似度百分比：{percentage}")
        return percentage



    def start(self):
        caps={}
        caps["platformName"] = "Android"
        caps["deviceName"] = self.getUdid()[0]
        caps["appPackage"] = "com.tencent.mm"
        # caps["appActivity"] = ".ui.LauncherUI"
        caps["appActivity"] = ".plugin.brandservice.ui.BrandServiceIndexUI"
        caps["noReset"] = "true"
        # caps["chromedriverExecutable"] = f"{os.getcwd()}\\89.0.4389.72_chromedriver\\chromedriver.exe"
        # caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:tools"}
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def goto_public_patient(self):
        return Patient_Service(self.driver)

    def goto_public_exclusive(self):
        return Exclusive_Doctor(self.driver)
