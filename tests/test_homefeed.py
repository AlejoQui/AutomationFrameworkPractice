from pages.homefeed_page import HomefeedPage

home_buttons = HomefeedPage()


def test_send_values_to_kwa_demo():
    home_buttons.choose_enter_value()
    home_buttons.go_back_button()


def test_user_submits_contact_information():
    home_buttons.choose_contact_us_from()
    home_buttons.go_back_button()


def test_move_between_home_sports_movie_tabs():
    home_buttons.choose_tab_activity()
    home_buttons.go_back_button()


def test_change_of_logo_display():
    home_buttons.choose_zoom()


def test_login():
    home_buttons.choose_login()
    home_buttons.go_back_button()


def test_get_password_of_the_entered_email():
    home_buttons.choose_long_click()


def test_enter_the_time_activity():
    home_buttons.choose_time()
    home_buttons.go_back()


def test_enter_the_date_activity():
    home_buttons.choose_date()
    home_buttons.go_back()


def test_connectivity_between_website_and_app():
    home_buttons.choose_hybrid()
    home_buttons.go_back_button()
    

def test_increase_or_decrease_the_user_logo():
    home_buttons.choose_pinch_in_out()
    home_buttons.go_back()


def test_change_position_of_items_by_user_categories():
    home_buttons.choose_draganddrop()
    home_buttons.go_back()
    

def test_enter_auto_suggestion():
    home_buttons.choose_auto_suggestion()
    home_buttons.go_back()


def test_crash_simulation():
    home_buttons.choose_crash()


def test_scroll_view():
    home_buttons.choose_scrollview()
    home_buttons.go_back_button()
