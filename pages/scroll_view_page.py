from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class ScrollViewPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_1 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_2 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_3 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_4 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_5 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_6 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_7 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_8 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_9 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_10 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_11 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_12 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_13 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_14 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_15 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_16 = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.POP_UP_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.POP_UP_Yes = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.POP_UP_NO = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
