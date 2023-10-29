from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class ContactUsFromPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.INPUT_ENTER_NAME = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.INPUT_ENTER_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.INPUT_ENTER_ADDRESS = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.INPUT_ENTER_MOBILE_NO = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.SUBMIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.MESSAGE_SUCCESSFUL_REGISTRATION = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
