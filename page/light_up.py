# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.getcwd())
from appium.webdriver.common.touch_action import TouchAction
from base.base_driver import base_driver


class LightUp(object):

    def __init__(self):
        self.driver = base_driver()

    def find_element_click(self):
       self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
       self.driver.find_element_by_xpath("//*[contains(@text,'亮度')]").click()
       light_button = self.driver.find_element_by_id("com.android.systemui:id/slider")
       location = light_button.location
       print(location)
       TouchAction(self.driver).press(x=300, y=290).wait(1000).move_to(x=500, y=290).perform()


if __name__ == '__main__':
    LightUp().find_element_click()

