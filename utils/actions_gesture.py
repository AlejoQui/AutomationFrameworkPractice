import json
from pathlib import Path

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from utils.constants import ErrorMessages, General, InformativeMessage
from utils.launch_app import KWALauncher
from utils.resolution_screen import ResolutionDevice

app_launcher = KWALauncher()
constants = General()
error_messages = ErrorMessages()
informative_messages = InformativeMessage()


class ActionGestures(ResolutionDevice):

    current_directory = Path(__file__).resolve().parent
    relative_path = constants.COORDINATES_SWIPE_TO
    coordinates_path = (current_directory / relative_path).resolve()

    try:
        with open(coordinates_path, "r") as json_file:
            directions = json.load(json_file)
    except FileNotFoundError:
        print(f"the file was not found: {coordinates_path}")
    except Exception as e:
        print(f"Error to open file: {e}")

    def __init__(self):
        super().__init__()
        self.driver = KWALauncher().launch_app()
        self.resolution_device = ResolutionDevice().get_resolution()
        self.BUTTON_NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")

    def wait_and_click(self, value, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(value))
        element.click()

    def scroll_to_element_click(self, value, timeout=10, max_attempts=5):
        attempts = 0
        while attempts <= max_attempts:
            try:
                element_scroll = WebDriverWait(self.driver, timeout).until(
                    ec.presence_of_element_located(value)
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element_scroll)
                element_scroll.click()
                break
            except TimeoutException:
                self.driver.execute_script("window.scrollBy(0, 300);")
                attempts += 1
        else:
            print("Element not found after multiple attempts")

    def scroll_to_element(self, value, timeout=10, max_attempts=5):
        attempts = 0
        while attempts <= max_attempts:
            try:
                element_scroll = WebDriverWait(self.driver, timeout).until(
                    ec.presence_of_element_located(value)
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element_scroll)
                break
            except TimeoutException:
                self.driver.execute_script("window.scrollBy(0, 300);")
                attempts += 1
        else:
            raise NoSuchElementException(
                f"Element {value} not found after {max_attempts} attempts"
            )

    def click_back_button(self):
        self.wait_and_click(self.BUTTON_NAVIGATE_UP)

    def back_driver(self):
        self.driver.back()

    def long_click(self, value, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(value))
        action = ActionChains(self.driver)
        action.click_and_hold(element).perform()
        # Remember:
        # ActionChains(driver) for Web Applications (Hybrid).
        # TouchActions(driver) for native Applications (iOS & Android).

    def tap_gesture(self, value, timeout, x, y, time):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(value))
        actions = TouchAction(self.driver)
        actions.tap(element, x, y, time)
        # (element, CorX,Cor Y, mil seg)
        actions.perform()
        # perform() mandatory for execute the TouchAction(driver)

    def drag_drop(self, value, timeout=30):
        # Define element positions
        element_a = WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(value))
        element_b = WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(value)
        )
        # TouchActions(driver) library
        actions = TouchAction(self.driver)
        # Press Element. Then, move to element b position.
        actions.long_press(element_a).move_to(element_b).release().perform()

    def swipe_to(self, move_to=None):
        self.resolution_device()

        direction = (move_to or "top").lower()

        if direction in self.directions:
            try:
                coordinate = self.directions[direction]

                start_x = coordinate[constants.COORDINATES_START_X] * self.SCREEN_WIDTH
                start_y = coordinate[constants.COORDINATES_START_Y] * self.SCREEN_HEIGHT
                end_x = coordinate[constants.COORDINATES_END_X] * self.SCREEN_WIDTH
                end_y = coordinate[constants.COORDINATES_END_Y] * self.SCREEN_HEIGHT

                actions = TouchAction(self.driver)
                actions.long_press(None, start_x, start_y).move_to(
                    None, end_x, end_y
                ).release().perform()

            except KeyError:
                messages = informative_messages.SWIPE_NO_VALID
                print(messages)
        else:
            error = error_messages.INVALID_INPUT
            print(error)
