from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class TabViewPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.HOME_TAB = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.HOME_TAB_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.HOME_SPORT = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.HOME_SPORT_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.HOME_MOVIE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.HOME_MOVIE_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
