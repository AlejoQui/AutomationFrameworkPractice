from pages.homefeed_page import HomefeedPage
from pages.tab_view_page import TabViewPage

home_buttons = HomefeedPage()
tab_view_page = TabViewPage()


def test_move_between_home_sports_movie_tabs_right():
    home_buttons.choose_tab_activity()
    tab_view_page.check_swipe_right_tab()


def test_move_between_home_sports_movie_tabs_left():
    home_buttons.choose_tab_activity()
    tab_view_page.check_swipe_left_tab()


def test_check_header_name_in_tab_view_page():
    home_buttons.choose_tab_activity()
    tab_view_page.check_header_name()


def test_user_able_select_home_tab():
    home_buttons.choose_tab_activity()
    tab_view_page.choose_home_tab()


def test_user_able_select_sport_tab():
    home_buttons.choose_tab_activity()
    tab_view_page.choose_sport_tab()


def test_user_able_select_movie_tab():
    home_buttons.choose_tab_activity()
    tab_view_page.choose_movie_tab()


def test_home_tab_name_is_correct():
    home_buttons.choose_tab_activity()
    tab_view_page.check_tab_name_home()


def test_sport_tab_name_is_correct():
    home_buttons.choose_tab_activity()
    tab_view_page.check_tab_name_sport()


def test_movie_tab_name_is_correct():
    home_buttons.choose_tab_activity()
    tab_view_page.check_tab_name_movie()


def test_contents_of_the_tab_are_shown_home():
    home_buttons.choose_tab_activity()
    tab_view_page.check_message_in_home_tab()


def test_contents_of_the_tab_are_shown_sport():
    home_buttons.choose_tab_activity()
    tab_view_page.check_message_in_sport_tab()


def test_contents_of_the_tab_are_shown_movie():
    home_buttons.choose_tab_activity()
    tab_view_page.check_message_in_movie_tab()
