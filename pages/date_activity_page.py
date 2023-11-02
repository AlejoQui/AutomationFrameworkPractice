from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class DateActivityPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='KWADemo']")
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Date Activity"]')

        self.DATE_LAYOUT = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="android:id/date_picker_header"'
                                            ']/android.widget.LinearLayout')
        self.YEAR_BUTTON = (AppiumBy.ID, "android:id/date_picker_header_year")
        self.DATE_HEADER = (AppiumBy.ID, "android:id/date_picker_header_date")

        self.PREVIOUSLY_MONTH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Previous month")
        self.NEXT_MONTH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Next month")

        self.DAY_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "22 November 2023")
