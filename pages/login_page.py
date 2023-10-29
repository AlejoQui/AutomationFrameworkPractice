from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class LoginPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.EMAIL_EXAMPLE_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.PASSWORD_EXAMPLE_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.INPUT_ENTER_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.INPUT_ENTER_PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.MESSAGE_SUCCESSFUL_REGISTRATION = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.MESSAGE_WRONG_CREDENTIALS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
