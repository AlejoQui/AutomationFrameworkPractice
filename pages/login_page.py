from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class LoginPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )
        self.PAGE_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "Login Page")]',
        )

        self.EMAIL_EXAMPLE_MESSAGE = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, " '"Email: admin@gmail.com")]',
        )
        self.PASSWORD_EXAMPLE_MESSAGE = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, " '"Email: admin@gmail.com")]',
        )  # Reviser el locator

        self.INPUT_ENTER_EMAIL = (AppiumBy.ID, "com.code2lead.kwad:id/Et4")
        self.INPUT_ENTER_PASSWORD = (AppiumBy.ID, "com.code2lead.kwad:id/Et5")
        self.LOGIN_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/Btn3")

        self.MESSAGE_SUCCESSFUL_REGISTRATION = (
            AppiumBy.ACCESSIBILITY_ID,
            "Btn1",
        )  # No tiene locator, preguntar a Edi.

        self.MESSAGE_WRONG_CREDENTIALS = (AppiumBy.ID, "com.code2lead.kwad:id/Tv8")
        self.MESSAGE_WRONG_USERNAME = (AppiumBy.ID, "com.code2lead.kwad:id/Tv3")
        self.MESSAGE_WRONG_PASSWORD = (AppiumBy.ID, "com.code2lead.kwad:id/Tv4")
