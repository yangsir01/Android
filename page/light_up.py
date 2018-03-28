# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class LightUp(object):
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 解决输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def find_element_click(self):
       self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
       self.driver.find_element_by_xpath("//*[contains(@text,'亮度')]").click()
       light_button = self.driver.find_element_by_id("com.android.systemui:id/slider")
       location = light_button.location
       print(location)
       TouchAction(self.driver).press(x=300, y=290).wait(1000).move_to(x=500, y=290).perform()

if __name__ == '__main__':
    LightUp().find_element_click()

