from pages.homefeed_page import HomefeedPage
from pages.scroll_view_page import ScrollViewPage

home_buttons = HomefeedPage()
scroll_view_page = ScrollViewPage()


def test_check_header_name_in_scroll_view():
    home_buttons.choose_scrollview()
    scroll_view_page.check_header_name()


def test_check_title_name_in_scroll_view():
    home_buttons.choose_scrollview()
    scroll_view_page.check_title_name()


def test_check_user_can_see_all_buttons_on_screen():
    home_buttons.choose_scrollview()
    scroll_view_page.check_the_presence_of_the_buttons_on_the_screen()


def test_user_is_able_to_swipe_across_the_screen():
    home_buttons.choose_scrollview()
    scroll_view_page.scroll_to_the_bottom_of_the_page()


def test_user_is_able_to_close_the_scroll_view_screen_with_pop_up():
    home_buttons.choose_scrollview()
    scroll_view_page.choose_button16()
    scroll_view_page.choose_yes_in_pop_up()
    # Deberia existir un metodo para verificar en que pantalla finaliza el proceso


def test_user_is_able_to_cancel_the_process_at_the_pop_up():
    home_buttons.choose_scrollview()
    scroll_view_page.choose_button16()
    scroll_view_page.choose_no_in_pop_up()
    # Deberia existir un metodo para verificar en que pantalla finaliza el proceso


def test_user_able_to_see_all_elements_in_pop_up():
    home_buttons.choose_scrollview()
    scroll_view_page.choose_button16()
    scroll_view_page.check_elements_in_alert_pop_up()
