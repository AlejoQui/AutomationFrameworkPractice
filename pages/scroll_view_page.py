from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class ScrollViewPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='KWADemo']")
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enter some Value"]')

        self.BUTTON_1 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON1"]')
        self.BUTTON_2 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON2"]')
        self.BUTTON_3 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON3"]')
        self.BUTTON_4 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON4"]')
        self.BUTTON_5 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON5"]')
        self.BUTTON_6 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON6"]')
        self.BUTTON_7 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON7"]')
        self.BUTTON_8 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON8"]')
        self.BUTTON_9 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON9"]')
        self.BUTTON_10 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON10"]')
        self.BUTTON_11 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON11"]')
        self.BUTTON_12 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON12"]')
        self.BUTTON_13 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON13"]')
        self.BUTTON_14 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON14"]')
        self.BUTTON_15 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON15"]')
        self.BUTTON_16 = (AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON16"]')

        self.POP_UP_ICON = (AppiumBy.ID, 'android:id/icon')
        self.POP_UP_TITLE = (AppiumBy.ID, 'com.code2lead.kwad:id/alertTitle')
        self.POP_UP_MESSAGE = (AppiumBy.ID, 'android:id/message')
        self.POP_UP_Yes = (AppiumBy.ID, 'android:id/button1')
        self.POP_UP_NO = (AppiumBy.ID, 'android:id/button2')
