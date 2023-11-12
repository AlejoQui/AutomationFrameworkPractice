from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class EnterAdminPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )
        self.PAGE_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "Enter Admin")]',
        )

        self.INPUT_ENTER_ADMIN = (AppiumBy.ID, "com.code2lead.kwad:id/Edt_admin")
        self.SUBMIT_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/Btn_admin_sub")
        self.MESSAGE_PREVIEW = (AppiumBy.ID, "com.code2lead.kwad:id/Tv_admin")
