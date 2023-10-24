import json

from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class HomeButtons:
    with open(r"C:\Users\Alejandro Q\Desktop\FrameworkPractice\config\constants_homebuttons.json", "r") as json_file:
        constants = json.load(json_file)

    def __init__(self):
        self.driver = KWALauncher().get_driver()
        self.action_gestures = action_gestures

    def choose_enter_value(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_ENTER_SOME_VALUE"])
    
    def choose_contact_us_from(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_CONTACT_US_FROM"])

    def choose_scrollview(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_SCROLLVIEW"])
        
    def choose_tab_activity(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_TAB_ACTIVITY"])
        
    def choose_zoom(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_ZOOM"])

    def choose_login(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_LOGIN"])
        
    def choose_long_click(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_LONG_CLICK"])

    def choose_time(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_TIME"])

    def choose_date(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_DATE"])

    def choose_hybrid(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_HYBRID"])
        
    def choose_pinch_in_out(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_PINCH_IN_OUT"])

    def choose_draganddrop(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_DRAGANDDROP"])

    def choose_crash(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_CRASH"])

    def choose_auto_suggestion(self):
        self.action_gestures.click_by_accessibility_id(self.constants["HomeButtons"]["BUTTON_AUTO_SUGGESTION"])
