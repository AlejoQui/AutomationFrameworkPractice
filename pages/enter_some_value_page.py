from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class EnterSomeValuePage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='KWADemo']")
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enter some Value"]')
        self.INPUT_ENTER_SOME_VALUE = (AppiumBy.ID, "com.code2lead.kwad:id/Et1")
        self.SUBMIT_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
        self.OUTPUT_ENTER_SOME_VALUE = (AppiumBy.ID, "com.code2lead.kwad:id/Tv1")
