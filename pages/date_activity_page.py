from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class DateActivityPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.YEAR_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.PREVIOUSLY_MONTH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.MONTH_NAME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.NEXT_MONTH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.DAY_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.MESSAGE_DATE_SELECTED = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
