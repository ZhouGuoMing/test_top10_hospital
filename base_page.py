# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : base_page.py
import json
import allure
import logging
import yaml
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os

class Base_Page:

    _params = {}
    _blacklist = [(MobileBy.XPATH, '//*[@text="关闭"]')]
    _max_mun = 3
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def setup_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, locator, value):
        logging.info(f"find: locator={locator}, value={value}")
        try:
            element = self.driver.find_element(locator, value)
            self._error_num = 0
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            # 处理黑名单
            self.setup_implicitly_wait(5)
            self.driver.get_screenshot_as_file("tem.png")
            allure.attach.file("tem.png", attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数
            if self._error_num > self._max_mun:
                self._error_num = 0
                self.setup_implicitly_wait(10)
                raise e
            # 每次进except一次都执行+1操作
            self._error_num += 1
            for ele in self._blacklist:
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    self.setup_implicitly_wait(10)
                    return self.find(locator, value)
            raise e

    def finds(self, locator, value):
        logging.info(f"find: locator={locator}, value={value}")
        return self.driver.find_elements(locator, value)

    def find_click(self, loctor, value):
        return self.find(loctor, value).click()

    def target_click(self, x1, y1):
        logging.info(f"target_click: x={x1}, y={y1}")
        # x_1=x1/1080
        # y_1=y1/2280
        # x=self.driver.get_window_size()['width']
        # y=self.driver.get_window_size()['height']
        # self.driver.tap([(x1,y1)], 500)
        action = TouchAction(self.driver)
        action.tap(x=x1, y=y1).perform()

    def swipe(self,x1,y1,x2,y2):
        logging.info(f"swipe: x1={x1}, y1={y1},x2={x2}, y2={y2}")
        self.driver.swipe(x1,y1,x2,y2)

    def swip_click(self, text):
        logging.info(f"swip_click: text={text}")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def staleness_of(self, locator, value):
        logging.info(f"staleness_of: locator={locator}, value={value}")
        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.staleness_of((locator, value)))
            return True
        except TimeoutError:
            return False

    def element_to_be_clickable(self, locator, value):
        logging.info(f"wait element_to_be_clickable: locator={locator}, value={value}")
        WebDriverWait(self.driver, 15).until(
         expected_conditions.element_located_to_be_selected((locator, value)))

    def element_to_be_clickable_click(self, locator, value):
        logging.info(f"wait element_to_be_clickable before click: locator={locator}, value={value}")
        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.element_to_be_clickable((locator, value)))
            self.find_click(locator, value)
            return True
        except TimeoutError:
            return False

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            # print(function)
            steps: list[dict] = function[fun_name]
            # print(steps)
            # json.dumps()序列化 python对象转化成字符串
            # json.loads()反序列化 python字符串转化为python对象
            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace("${" + key + "}", value)
            steps = json.loads(raw)

        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                if step["find_to_do"] == "text":
                    return self.find(step["by"], step["locator"]).text
                else:
                    self.find(step["by"], step["locator"])
            elif step["action"] == "finds":
                if step["finds_to_do"] == "return":
                    return self.finds(step["by"], step["locator"])
                else:
                    self.finds(step["by"], step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "send_keys":
                self.find(step["by"], step["locator"]).send_keys(step["text"])
            elif step["action"] == "staleness_of":
                self.staleness_of(step["by"], step["locator"])
            elif step["action"] == "sleep":
                sleep(step["time"])
            elif step["action"] == "element_to_be_clickable_click":
                self.element_to_be_clickable_click(step["by"],step["locator"])
            elif step["action"] == "element_to_be_clickable":
                self.element_to_be_clickable(step["by"],step["locator"])
            elif step["action"] == "switch_to.context":
                sleep(5)
                logging.info(f"switch_to.context：{self.driver.contexts}")
                contexts=self.driver.contexts[-1]
                self.driver.switch_to.context(contexts)
            elif step["action"] == "switch_to.window":
                windows=self.driver.window_handles[-1]
                self.driver.switch_to.window(windows)
            elif step["action"] == "switch_to.context":
                self.driver.switch_to.context(self.driver.contexts[-1])
            elif step["action"] == "target_click":
                self.target_click(step["x"], step["y"])
            elif step["action"] == "swipe":
                self.swipe(step["x1"], step["y1"],step["x2"], step["y2"])
            elif step["action"] == "startActivity":
                self.driver.start_activity("com.tencent.mm", ".plugin.brandservice.ui.BrandServiceIndexUI")
            elif step["action"] == "print":
                sleep(5)
                # print(self.driver.contexts)
                print(self.driver.window_handles)
            elif step["action"] == "png":
                sleep(8)
                self.driver.get_screenshot_as_file(f"{os.getcwd()}/test_png/test_{fun_name}.png")
                allure.attach.file(f"{os.getcwd()}/test_png/test_{fun_name}.png", attachment_type=allure.attachment_type.PNG)