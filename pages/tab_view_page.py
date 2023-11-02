from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class TabViewPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Tab View"]')

        self.HOME_TAB_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Home')
        self.HOME_TAB_NAME = (AppiumBy.XPATH, '//android.widget.TextView[@text="HOME"]')
        self.HOME_TAB_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="HomeFragment"]')

        self.SPORT_TAB_NAME = (AppiumBy.ACCESSIBILITY_ID, 'Sport')
        self.SPORT_TAB_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="SPORT"]')
        self.SPORT_TAB_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="SportFragment"]')

        self.MOVIE_TAB_NAME = (AppiumBy.ACCESSIBILITY_ID, 'Movie')
        self.MOVIE_TAB_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="MOVIE"]')
        self.MOVIE_TAB_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="MovieFragment"]')
