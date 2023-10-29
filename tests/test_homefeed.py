from pages.homefeed_page import HomefeedPage

home_buttons = HomefeedPage()


def test_enter_value_button():
    home_buttons.choose_enter_value()
    home_buttons.go_back_button()


def test_contact_button():
    home_buttons.choose_contact_us_from()
    home_buttons.go_back_button()


def test_scroll_view():
    home_buttons.choose_scrollview()
    home_buttons.go_back_button()


def test_tab_activity():
    home_buttons.choose_tab_activity()
    home_buttons.go_back_button()


def test_zoom():
    home_buttons.choose_zoom()


def test_login():
    home_buttons.choose_login()
    home_buttons.go_back_button()


def test_longclick():
    home_buttons.choose_long_click()


def test_time():
    home_buttons.choose_time()
    home_buttons.go_back()


def test_date():
    home_buttons.choose_date()
    home_buttons.go_back()


def test_hybrid():
    home_buttons.choose_hybrid()
    home_buttons.go_back_button()
    

def test_pinch_in_put():
    home_buttons.choose_pinch_in_out()
    home_buttons.go_back()


def test_drag_and_drop():
    home_buttons.choose_draganddrop()
    home_buttons.go_back()
    

def test_auto_suggestion():
    home_buttons.choose_auto_suggestion()
    home_buttons.go_back()


def test_crash():
    home_buttons.choose_crash()
