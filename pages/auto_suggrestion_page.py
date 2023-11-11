from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class AutoSuggestionPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )

        self.INPUT_ENTER_HERE = (AppiumBy.ID, "com.code2lead.kwad:id/multiAutoCompleteTextView")
        self.SUBMIT_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/btn_submit")
        self.MESSAGE_SENT = (AppiumBy.ID, "com.code2lead.kwad:id/tv_value")
