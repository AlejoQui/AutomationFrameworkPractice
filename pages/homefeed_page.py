from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class HomefeedPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.BUTTON_ENTER_SOME_VALUE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.BUTTON_CONTACT_US_FROM = (AppiumBy.ACCESSIBILITY_ID, "Btn2")
        self.BUTTON_SCROLLVIEW = (AppiumBy.ACCESSIBILITY_ID, "Btn3")
        self.BUTTON_TAB_ACTIVITY = (AppiumBy.ACCESSIBILITY_ID, "Btn4")
        self.BUTTON_ZOOM = (AppiumBy.ACCESSIBILITY_ID, "Btn5")
        self.BUTTON_LOGIN = (AppiumBy.ACCESSIBILITY_ID, "Btn6")
        self.BUTTON_LONG_CLICK = (AppiumBy.ACCESSIBILITY_ID, "Btn7")
        self.BUTTON_TIME = (AppiumBy.ACCESSIBILITY_ID, "Btn8")
        self.BUTTON_DATE = (AppiumBy.ACCESSIBILITY_ID, "Btn9")
        self.BUTTON_HYBRID = (AppiumBy.ACCESSIBILITY_ID, "com.code2lead.kwad:id/hybrid")
        self.BUTTON_PINCH_IN_OUT = (AppiumBy.ACCESSIBILITY_ID, "com.code2lead.kwad:id/pinch")
        self.BUTTON_DRAGANDDROP = (AppiumBy.ACCESSIBILITY_ID, "com.code2lead.kwad:id/drag")
        self.BUTTON_CRASH = (AppiumBy.ACCESSIBILITY_ID, "com.code2lead.kwad:id/crash")
        self.BUTTON_AUTO_SUGGESTION = (
            AppiumBy.ACCESSIBILITY_ID,
            "com.code2lead.kwad:id/autocomlete",
        )

    def choose_enter_value(self):
        self.action_gestures.wait_and_click(self.BUTTON_ENTER_SOME_VALUE)

    def choose_contact_us_from(self):
        self.action_gestures.wait_and_click(self.BUTTON_CONTACT_US_FROM)

    def choose_scrollview(self):
        self.action_gestures.wait_and_click(self.BUTTON_SCROLLVIEW)

    def choose_tab_activity(self):
        self.action_gestures.wait_and_click(self.BUTTON_TAB_ACTIVITY)

    def choose_zoom(self):
        self.action_gestures.wait_and_click(self.BUTTON_ZOOM)

    def choose_login(self):
        self.action_gestures.wait_and_click(self.BUTTON_LOGIN)

    def choose_long_click(self):
        self.action_gestures.wait_and_click(self.BUTTON_LONG_CLICK)

    def choose_time(self):
        self.action_gestures.wait_and_click(self.BUTTON_TIME)

    def choose_date(self):
        self.action_gestures.wait_and_click(self.BUTTON_DATE)

    def choose_hybrid(self):
        self.action_gestures.wait_and_click(self.BUTTON_HYBRID)

    def choose_pinch_in_out(self):
        self.action_gestures.wait_and_click(self.BUTTON_PINCH_IN_OUT)

    def choose_draganddrop(self):
        self.action_gestures.wait_and_click(self.BUTTON_DRAGANDDROP)

    def choose_crash(self):
        self.action_gestures.wait_and_click(self.BUTTON_CRASH)

    def choose_auto_suggestion(self):
        self.action_gestures.wait_and_click(self.BUTTON_AUTO_SUGGESTION)

    def go_back_button(self):
        action_gestures.click_back_button()

    def go_back(self):
        action_gestures.back_driver()
