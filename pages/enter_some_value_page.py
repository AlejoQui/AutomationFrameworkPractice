from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class EnterSomeValuePage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )
        self.PAGE_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "Enter some Value")]',
        )

        self.INPUT_ENTER_SOME_VALUE = (AppiumBy.ID, "com.code2lead.kwad:id/Et1")
        self.SUBMIT_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
        self.OUTPUT_ENTER_SOME_VALUE = (AppiumBy.ID, "com.code2lead.kwad:id/Tv1")

        self.ENTERED_TEXT = ""

    def send_keys_enter_some_value(self, text="Test Enter Some Value Page"):
        element = self.driver.find_element(self.INPUT_ENTER_SOME_VALUE)
        element.send_keys(text)
        self.ENTERED_TEXT = text

    def choose_enter_value_submit_button(self):
        submit_button = self.driver.find_element(self.SUBMIT_BUTTON)
        submit_button.click()

    def check_output_enter_some_value(self):
        output = self.driver.find_element(self.OUTPUT_ENTER_SOME_VALUE)
        actual_text = output.text

        assert actual_text == self.ENTERED_TEXT, (
            f"Expected text: '{self.ENTERED_TEXT}',1`" f"\nActual text: '{actual_text}'"
        )

    def check_header_name(self):
        actual_header_name = self.driver.find_element(self.PAGE_HEADER)
        expected_header_name = "KWADem0"
        assert actual_header_name == expected_header_name, (
            f"Expected text: '{expected_header_name}',1`" f"\nActual text: '{actual_header_name}'"
        )

    def check_title_name(self):
        actual_title_name = self.driver.find_element(self.PAGE_TITLE)
        expected_title_name = "Enter Some Value"
        assert actual_title_name == expected_title_name, (
            f"Expected text: '{expected_title_name}',1`" f"\nActual text: '{actual_title_name}'"
        )
