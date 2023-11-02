from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class HybridActivityPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.XPATH, "//android.widget.TextView[@text='KWADemo']")
        self.PAGE_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Hybrid Activity"]')

        self.URL_WEBSITE = (AppiumBy.ID, 'com.code2lead.kwad:id/HydUrl')
        self.WEB_VIEW = (AppiumBy.ID, 'com.code2lead.kwad:id/webView')

        self.ENTER_SOME_VALUE_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Enter some Value"]')
        self.INPUT_ENTER_SOME_VALUE = (AppiumBy.ID, 'com.code2lead.kwad:id/hEt1')
        self.SUBMIT_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/hBtn1")
        self.PREVIEW_MESSAGE = (AppiumBy.ID, "com.code2lead.kwad:id/hTv1")
