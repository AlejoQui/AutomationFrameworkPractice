from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class ContactUsFromPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )
        self.PAGE_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "Contact Us form")]',
        )

        self.INPUT_ENTER_NAME = (AppiumBy.ID, "com.code2lead.kwad:id/Et2")
        self.INPUT_ENTER_EMAIL = (AppiumBy.ID, "com.code2lead.kwad:id/Et3")
        self.INPUT_ENTER_ADDRESS = (AppiumBy.ID, "com.code2lead.kwad:id/Et6")
        self.INPUT_ENTER_MOBILE_NO = (AppiumBy.ID, "com.code2lead.kwad:id/Et7")
        self.SUBMIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "com.code2lead.kwad:id/Btn2")

        self.OUTPUT_ENTER_NAME = (AppiumBy.ID, "com.code2lead.kwad:id/Tv2")
        self.OUTPUT_ENTER_EMAIL = (AppiumBy.ID, "com.code2lead.kwad:id/Tv7")
        self.OUTPUT_PASSWORD = (AppiumBy.ID, "com.code2lead.kwad:id/Tv5")
        self.OUTPUT_ENTER_MOBILE_NO = (AppiumBy.ID, "com.code2lead.kwad:id/Tv6")

        self.MESSAGE_SUCCESSFUL_REGISTRATION = (
            AppiumBy.ACCESSIBILITY_ID,
            "Btn1",
        )  # No tiene locator.

        self.ENTERED_NAME = ""
        self.ENTERED_EMAIL = ""
        self.ENTERED_ADDRESS = ""
        self.ENTERED_MOBILE_NO = ""

    def check_header_name(self):
        actual_header_name = self.driver.find_element(self.PAGE_HEADER)
        expected_header_name = "KWADem0"
        assert actual_header_name == expected_header_name, (
            f"Expected text: '{expected_header_name}',1`" f"\nActual text: '{actual_header_name}'"
        )

    def check_title_name(self):
        actual_title_name = self.driver.find_element(self.PAGE_TITLE)
        expected_title_name = "Contact Us form"
        assert actual_title_name == expected_title_name, (
            f"Expected text: '{expected_title_name}',1`" f"\nActual text: '{actual_title_name}'"
        )

    def send_keys_enter_name(self, text="Test Name"):
        element = self.driver.find_element(self.INPUT_ENTER_NAME)
        element.send_keys(text)
        self.ENTERED_NAME = text

    def send_keys_enter_email(self, text="Test Email"):
        element = self.driver.find_element(self.INPUT_ENTER_EMAIL)
        element.send_keys(text)
        self.ENTERED_EMAIL = text

    def send_keys_enter_address(self, text="Test Address"):
        element = self.driver.find_element(self.INPUT_ENTER_ADDRESS)
        element.send_keys(text)
        self.ENTERED_ADDRESS = text

    def send_keys_enter_mobile_no(self, text="Test Mobile No"):
        element = self.driver.find_element(self.INPUT_ENTER_MOBILE_NO)
        element.send_keys(text)
        self.ENTERED_MOBILE_NO = text

    def choose_contact_us_form_submit_button(self):
        submit_button = self.driver.find_element(self.SUBMIT_BUTTON)
        submit_button.click()

    def check_output_entered_name(self):
        output = self.driver.find_element(self.OUTPUT_ENTER_NAME)
        actual_text = output.text

        assert actual_text == self.ENTERED_NAME, (
            f"Expected text: '{self.ENTERED_NAME}',1`" f"\nActual text: '{actual_text}'"
        )

    def check_output_entered_email(self):
        output = self.driver.find_element(self.OUTPUT_ENTER_EMAIL)
        actual_text = output.text

        assert actual_text == self.ENTERED_EMAIL, (
            f"Expected text: '{self.ENTERED_EMAIL}',1`" f"\nActual text: '{actual_text}'"
        )

    def check_output_entered_address(self):
        output = self.driver.find_element(self.OUTPUT_PASSWORD)
        actual_text = output.text

        assert actual_text == self.ENTERED_ADDRESS, (
            f"Expected text: '{self.ENTERED_ADDRESS}',1`" f"\nActual text: '{actual_text}'"
        )

    def check_output_entered_mobile_no(self):
        output = self.driver.find_element(self.OUTPUT_ENTER_MOBILE_NO)
        actual_text = output.text

        assert actual_text == self.ENTERED_MOBILE_NO, (
            f"Expected text: '{self.ENTERED_MOBILE_NO}',1`" f"\nActual text: '{actual_text}'"
        )
