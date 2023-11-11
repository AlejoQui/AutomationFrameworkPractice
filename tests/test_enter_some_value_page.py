from pages.enter_some_value_page import EnterSomeValuePage
from pages.homefeed_page import HomefeedPage

home_buttons = HomefeedPage()
enter_some_value_page = EnterSomeValuePage()


def test_user_able_to_send_values():
    home_buttons.choose_enter_value()
    enter_some_value_page.send_keys_enter_some_value("test")
    enter_some_value_page.choose_enter_value_submit_button()
    enter_some_value_page.check_output_enter_some_value()
    home_buttons.go_back_button()


def test_check_header_name_in_enter_some_value_page():
    home_buttons.choose_enter_value()
    enter_some_value_page.check_header_name()


def test_check_title_name_in_enter_some_value_page():
    home_buttons.choose_enter_value()
    enter_some_value_page.check_title_name()
