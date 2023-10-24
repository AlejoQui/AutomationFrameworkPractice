from utils.launch_app import KWALauncher
from utils.actions_gesture import ActionGestures
from pages.homefeed import HomeButtons

app_launcher = KWALauncher()
action_gestures = ActionGestures()
home_buttons = HomeButtons()


def test_enter_value_button():
    home_buttons.choose_enter_value()
    action_gestures.click_back_button()


def test_contact_button():
    home_buttons.choose_contact_us_from()
    action_gestures.click_back_button()


def test_scroll_view():
    home_buttons.choose_scrollview()
    action_gestures.click_back_button()


def test_tab_activity():
    home_buttons.choose_tab_activity()
    action_gestures.click_back_button()


def test_zoom():
    home_buttons.choose_zoom()


def test_login():
    home_buttons.choose_login()
    action_gestures.click_back_button()


def test_longclick():
    home_buttons.choose_long_click()


def test_time():
    home_buttons.choose_time()
    action_gestures.back_driver()


def test_date():
    home_buttons.choose_date()
    action_gestures.back_driver()


def test_hybrid():
    home_buttons.choose_hybrid()
    action_gestures.click_back_button()
    

def test_pinch_in_put():
    home_buttons.choose_pinch_in_out()
    action_gestures.back_driver()


def test_drag_and_drop():
    home_buttons.choose_draganddrop()
    action_gestures.back_driver()
    

def test_auto_suggestion():
    home_buttons.choose_auto_suggestion()
    action_gestures.back_driver()


def test_crash():
    home_buttons.choose_crash()
