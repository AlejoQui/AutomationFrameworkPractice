from appium.webdriver.common.appiumby import AppiumBy
from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class DragAndDropActivityPage:
    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.DRAGGABLE_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.DRAGGABLE_LOGO = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.DRAGGABLE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.SECTION_ORANGE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.SECTION_BLUE = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
        self.SECTION_GREEN = (AppiumBy.ACCESSIBILITY_ID, "Btn1")
