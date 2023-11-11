from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class TimeActivityPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )
        self.PAGE_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "Time Activity")]',
        )

        self.TIME_HEADER = (AppiumBy.ID, "android:id/time_header")
        self.HOUR_BUTTON = (AppiumBy.ID, "android:id/hours")
        self.SEPARATOR = (AppiumBy.ID, "android:id/separator")
        self.MINUTES_BUTTON = (AppiumBy.ID, "android:id/minutes")
        self.AM_BUTTON = (AppiumBy.ID, "android:id/am_label")
        self.PM_BUTTON = (AppiumBy.ID, "android:id/pm_label")

        self.CLOCK = (AppiumBy.ID, "android:id/radial_picker")
        self.HOUR_ON_CLOCK_11 = (AppiumBy.ACCESSIBILITY_ID, "11")
        self.MIN_ON_CLOCK_30 = (AppiumBy.ACCESSIBILITY_ID, "30")

        self.CHANGE_FORMAT_BUTTON = (
            AppiumBy.ACCESSIBILITY_ID,
            "Switch to text input mode for the time input.",
        )
