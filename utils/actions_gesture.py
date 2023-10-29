import json
import os

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils.resolution_screen import ResolutionDevice
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()


class ActionGestures(ResolutionDevice):

    current_directory = os.path.dirname(__file__)
    relative_path = 'config/constans_swipe_to.json'
    coordinates_path = os.path.join(current_directory, relative_path)

    with open(coordinates_path, "r") as json_file:
        directions = json.load(json_file)

    def __init__(self):
        super().__init__()
        self.driver = KWALauncher().get_driver()
        self.resolution_device = ResolutionDevice().get_resolution()
        self.BUTTON_NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")

    def wait_and_click(self, value, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(value))
        element.click()

    def scroll_to_element_click(self, by, value, timeout=30):
        element_scroll = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((by, value)))
        element_scroll.click()

    def scroll_to_element(self, by, value, timeout=30):
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((by, value)))

    def click_back_button(self):
        self.wait_and_click(self.BUTTON_NAVIGATE_UP)

    def back_driver(self):
        self.driver.back()

    def long_click(self, by, value, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, value)))
        action = ActionChains(self.driver)
        action.click_and_hold(element).perform()
        # Remember:
        # ActionChains(driver) for Web Applications (Hybrid).
        # TouchActions(driver) for native Applications (iOS & Android).

    def tap_gesture(self, by, value, timeout, x, y, time):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((by, value)))
        actions = TouchAction(self.driver)
        actions.tap(element, x, y, time)
        # (element, CorX,Cor Y, mil seg)
        actions.perform()
        # perform() mandatory for execute the TouchAction(driver)

    def drag_drop(self, by, value, timeout=30):
        # Define element positions
        element_a = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, value)))
        element_b = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((by, value)))
        # TouchActions(driver) library
        actions = TouchAction(self.driver)
        # Press Element. Then, move to element b position.
        actions.long_press(element_a).move_to(element_b).release().perform()

    def swipe_to(self, move_to):
        self.resolution_device()
        direction = move_to.lower()

        if direction in self.directions:
            coordinate = self.directions[direction]

            start_x = coordinate['start_x'] * self.screen_width
            start_y = coordinate['start_y'] * self.screen_height
            end_x = coordinate['end_x'] * self.screen_width
            end_y = coordinate['end_y'] * self.screen_height

            actions = TouchAction(self.driver)
            actions.long_press(None, start_x, start_y).move_to(None, end_x, end_y).release().perform()
        else:
            print('Invalid Input. Please, indicate the direction in which the sweep is performed:'
                  '\nLeft\nRight\nTop\nBottom')
