from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class TimeActivityPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='KWADemo']")
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Time Activity"]')

        self.TIME_HEADER = (AppiumBy.ID, 'android:id/time_header')
        self.HOUR_BUTTON = (AppiumBy.ID, 'android:id/hours')
        self.SEPARATOR = (AppiumBy.ID, 'android:id/separator')
        self.MINUTES_BUTTON = (AppiumBy.ID, 'android:id/minutes')
        self.AM_BUTTON = (AppiumBy.ID, 'android:id/am_label')
        self.PM_BUTTON = (AppiumBy.ID, 'android:id/pm_label')

        self.CLOCK = (AppiumBy.ID, 'android:id/radial_picker')
        self.HOUR_ON_CLOCK_1 = (AppiumBy.ACCESSIBILITY_ID, '1')
        self.HOUR_ON_CLOCK_2 = (AppiumBy.ACCESSIBILITY_ID, '2')
        self.HOUR_ON_CLOCK_3 = (AppiumBy.ACCESSIBILITY_ID, '3')
        self.HOUR_ON_CLOCK_4 = (AppiumBy.ACCESSIBILITY_ID, '4')
        self.HOUR_ON_CLOCK_5 = (AppiumBy.ACCESSIBILITY_ID, '5')
        self.HOUR_ON_CLOCK_6 = (AppiumBy.ACCESSIBILITY_ID, '6')
        self.HOUR_ON_CLOCK_7 = (AppiumBy.ACCESSIBILITY_ID, '7')
        self.HOUR_ON_CLOCK_8 = (AppiumBy.ACCESSIBILITY_ID, '8')
        self.HOUR_ON_CLOCK_9 = (AppiumBy.ACCESSIBILITY_ID, '9')
        self.HOUR_ON_CLOCK_10 = (AppiumBy.ACCESSIBILITY_ID, '10')
        self.HOUR_ON_CLOCK_11 = (AppiumBy.ACCESSIBILITY_ID, '11')
        self.HOUR_ON_CLOCK_12 = (AppiumBy.ACCESSIBILITY_ID, '12')

        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '0')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '5')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '10')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '15')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '20')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '25')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '30')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '35')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '40')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '45')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '50')
        self.MIN_ON_CLOCK_00 = (AppiumBy.ACCESSIBILITY_ID, '55')

        self.CHANGE_FORMAT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Switch to text input mode for the time input.")
