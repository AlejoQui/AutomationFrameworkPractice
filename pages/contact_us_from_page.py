from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class ContactUsFromPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="KWADemo"]')
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Contact Us form"]')

        self.INPUT_ENTER_NAME = (AppiumBy.ID, "com.code2lead.kwad:id/Et2")
        self.INPUT_ENTER_EMAIL = (AppiumBy.ID, "com.code2lead.kwad:id/Et3")
        self.INPUT_ENTER_ADDRESS = (AppiumBy.ID, "com.code2lead.kwad:id/Et6")
        self.INPUT_ENTER_MOBILE_NO = (AppiumBy.ID, "com.code2lead.kwad:id/Et7")
        self.SUBMIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "com.code2lead.kwad:id/Btn2")

        self.OUTPUT_ENTER_NAME = (AppiumBy.ID, "com.code2lead.kwad:id/Tv2")
        self.OUTPUT_ENTER_EMAIL = (AppiumBy.ID, "com.code2lead.kwad:id/Tv7")
        self.OUTPUT_PASSWORD = (AppiumBy.ID, "com.code2lead.kwad:id/Tv5")
        self.OUTPUT_ENTER_MOBILE_NO = (AppiumBy.ID, "com.code2lead.kwad:id/Tv6")

        self.MESSAGE_SUCCESSFUL_REGISTRATION = (AppiumBy.ACCESSIBILITY_ID, "Btn1")  # No tiene locator.
