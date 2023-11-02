from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class TimeActivitySetTimePage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='KWADemo']")
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Time Activity"]')

        self.TIME_HEADER = (AppiumBy.ID, 'android:id/input_header')
        self.MESSAGE_TYPE_IN_TIME = (AppiumBy.ID, 'android:id/top_label')

        self.INPUT_HOUR = (AppiumBy.ID, 'android:id/input_hour')
        self.SEPARATOR = (AppiumBy.ID, 'android:id/input_separator')
        self.INPUT_MINUTES = (AppiumBy.ID, 'android:id/input_minute')

        self.AM_PM_DROPDOWN = (AppiumBy.ID, 'android:id/am_pm_spinner')
        self.AM_PM_TEXT = (AppiumBy.ID, 'android:id/text1')

        self.HOUR_TEXT = (AppiumBy.ID, 'android:id/label_hour')
        self.MINUTE_TEXT = (AppiumBy.ID, 'android:id/label_minute')

        self.CHANGE_FORMAT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Switch to text input mode for the time input.")
