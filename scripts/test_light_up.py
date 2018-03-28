# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.getcwd())
from page.light_up import LightUp


class TestLights(LightUp):
    def setup(self):
        pass

    def teardown(self):
        pass
        # driver.quit()

    def test_light_up(self):
        # TouchAction(driver).press(x=location["x"], y=location["y"]).move_to(x=location["x"] + 100, y=location["y"])
        LightUp().find_element_click()
