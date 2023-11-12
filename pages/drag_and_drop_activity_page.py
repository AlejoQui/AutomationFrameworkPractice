from appium.webdriver.common.appiumby import AppiumBy

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class DragAndDropActivityPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            "//android.widget.TextView[contains(@text, 'KWADemo')]",
        )

        self.DRAGGABLE_TEXT = (AppiumBy.ID, "com.code2lead.kwad:id/lbl")
        self.DRAGGABLE_LOGO = (AppiumBy.ID, "com.code2lead.kwad:id/ingvw")
        self.DRAGGABLE_BUTTON = (AppiumBy.ID, "com.code2lead.kwad:id/btnDrag")

        self.SECTION_ORANGE = (AppiumBy.ID, "com.code2lead.kwad:id/layout1")
        self.SECTION_BLUE = (AppiumBy.ID, "com.code2lead.kwad:id/layout2")
        self.SECTION_GREEN = (AppiumBy.ID, "com.code2lead.kwad:id/layout3")
