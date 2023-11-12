from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class ScrollViewPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )
        self.PAGE_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Enter some Value"]',
        )  # Revisar

        self.BUTTON_1 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON1")]')
        self.BUTTON_2 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON2")]')
        self.BUTTON_3 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON3")]')
        self.BUTTON_4 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON4")]')
        self.BUTTON_5 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON5")]')
        self.BUTTON_6 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON6")]')
        self.BUTTON_7 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON7")]')
        self.BUTTON_8 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON8")]')
        self.BUTTON_9 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON9")]')
        self.BUTTON_10 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON10")]')
        self.BUTTON_11 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON11")]')
        self.BUTTON_12 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON12")]')
        self.BUTTON_13 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON13")]')
        self.BUTTON_14 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON14")]')
        self.BUTTON_15 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON15")]')
        self.BUTTON_16 = (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "BUTTON16")]')

        self.POP_UP_ICON = (AppiumBy.ID, "android:id/icon")
        self.POP_UP_TITLE = (AppiumBy.ID, "com.code2lead.kwad:id/alertTitle")
        self.POP_UP_MESSAGE = (AppiumBy.ID, "android:id/message")
        self.POP_UP_YES = (AppiumBy.ID, "android:id/button1")
        self.POP_UP_NO = (AppiumBy.ID, "android:id/button2")

    def check_header_name(self):
        actual_header_name = self.driver.find_element(self.PAGE_HEADER)
        expected_header_name = "KWADem0"
        assert actual_header_name == expected_header_name, (
            f"Expected text: '{expected_header_name}',1`" f"\nActual text: '{actual_header_name}'"
        )

    def check_title_name(self):
        actual_title_name = self.driver.find_element(self.PAGE_TITLE)
        expected_title_name = "ScrollView"
        assert actual_title_name == expected_title_name, (
            f"Expected text: '{expected_title_name}',1`" f"\nActual text: '{actual_title_name}'"
        )

    def choose_button16(self):
        action_gestures.scroll_to_element_click(self.BUTTON_16)

    def scroll_to_the_bottom_of_the_page(self):
        action_gestures.scroll_to_element(self.BUTTON_16)

    def check_the_presence_of_the_buttons_on_the_screen(self):
        buttons = [
            self.BUTTON_1,
            self.BUTTON_2,
            self.BUTTON_3,
            self.BUTTON_4,
            self.BUTTON_5,
            self.BUTTON_6,
            self.BUTTON_7,
            self.BUTTON_8,
            self.BUTTON_9,
            self.BUTTON_10,
            self.BUTTON_11,
            self.BUTTON_12,
            self.BUTTON_13,
            self.BUTTON_14,
            self.BUTTON_15,
            self.BUTTON_16,
        ]

        for button_locator in buttons:
            self.check_button(button_locator)

    @staticmethod
    def check_button(button_locator):
        try:
            _ = action_gestures.scroll_to_element(button_locator)
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Button {button_locator} not found") from e

    def check_elements_in_alert_pop_up(self):
        elements = [
            self.POP_UP_ICON,
            self.POP_UP_TITLE,
            self.POP_UP_MESSAGE,
            self.POP_UP_NO,
            self.POP_UP_YES,
        ]

        for element in elements:
            self.check_element(element)

    def check_element(self, element):
        try:
            _ = self.driver.find_element(element)
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Element {element} not found") from e

    def choose_yes_in_pop_up(self):
        yes_button = self.driver.find_element(self.POP_UP_YES)
        yes_button.click()

    def choose_no_in_pop_up(self):
        no_button = self.driver.find_element(self.POP_UP_NO)
        no_button.click()

    def check_that_the_screen_is_closed(self):
        pass
