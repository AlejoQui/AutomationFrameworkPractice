from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from utils.actions_gesture import ActionGestures
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
action_gestures = ActionGestures()


class TabViewPage:
    def __init__(self):
        self.driver = KWALauncher().launch_app()
        self.action_gestures = action_gestures
        self.PAGE_HEADER = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text, "Tab View"])',
        )

        self.HOME_TAB_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Home")
        self.HOME_TAB_NAME = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"HOME"])')
        self.HOME_TAB_MESSAGE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"HomeFragment"])',
        )

        self.SPORT_TAB_NAME = (AppiumBy.ACCESSIBILITY_ID, "Sport")
        self.SPORT_TAB_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"SPORT"])',
        )
        self.SPORT_TAB_MESSAGE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"SportFragment"])',
        )

        self.MOVIE_TAB_NAME = (AppiumBy.ACCESSIBILITY_ID, "Movie")
        self.MOVIE_TAB_TITLE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"MOVIE"])',
        )
        self.MOVIE_TAB_MESSAGE = (
            AppiumBy.XPATH,
            '//android.widget.TextView[contains(@text,"MovieFragment"])',
        )

    def check_header_name(self):
        actual_header_name = self.driver.find_element(self.PAGE_HEADER)
        expected_header_name = "Tab View"
        assert actual_header_name == expected_header_name, (
            f"Expected text: '{expected_header_name}',1`" f"\nActual text: '{actual_header_name}'"
        )

    def choose_home_tab(self):
        home_tab = self.driver.find_element(self.HOME_TAB_TITLE)
        home_tab.click()

    def choose_sport_tab(self):
        home_tab = self.driver.find_element(self.SPORT_TAB_TITLE)
        home_tab.click()

    def choose_movie_tab(self):
        home_tab = self.driver.find_element(self.MOVIE_TAB_TITLE)
        home_tab.click()

    def check_tab_name_home(self):
        actual_tab_name = self.driver.find_element(self.HOME_TAB_NAME)
        expected_tab_name = "HOME"
        assert actual_tab_name == expected_tab_name, (
            f"Expected text: '{expected_tab_name}',1`" f"\nActual text: '{actual_tab_name}'"
        )

    def check_tab_name_sport(self):
        actual_tab_name = self.driver.find_element(self.SPORT_TAB_NAME)
        expected_tab_name = "SPORT"
        assert actual_tab_name == expected_tab_name, (
            f"Expected text: '{expected_tab_name}',1`" f"\nActual text: '{actual_tab_name}'"
        )

    def check_tab_name_movie(self):
        actual_tab_name = self.driver.find_element(self.MOVIE_TAB_NAME)
        expected_tab_name = "MOVIE"
        assert actual_tab_name == expected_tab_name, (
            f"Expected text: '{expected_tab_name}',1`" f"\nActual text: '{actual_tab_name}'"
        )

    def check_message_in_home_tab(self):
        actual_message_tab_name = self.driver.find_element(self.HOME_TAB_MESSAGE)
        expected_message_tab_name = "HomeFragment"
        assert actual_message_tab_name == expected_message_tab_name, (
            f"Expected text: '{expected_message_tab_name}',1`"
            f"\nActual text: '{actual_message_tab_name}'"
        )

    def check_message_in_sport_tab(self):
        actual_message_tab_name = self.driver.find_element(self.SPORT_TAB_MESSAGE)
        expected_message_tab_name = "HomeFragment"
        assert actual_message_tab_name == expected_message_tab_name, (
            f"Expected text: '{expected_message_tab_name}',1`"
            f"\nActual text: '{actual_message_tab_name}'"
        )

    def check_message_in_movie_tab(self):
        actual_message_tab_name = self.driver.find_element(self.MOVIE_TAB_MESSAGE)
        expected_message_tab_name = "HomeFragment"
        assert actual_message_tab_name == expected_message_tab_name, (
            f"Expected text: '{expected_message_tab_name}',1`"
            f"\nActual text: '{actual_message_tab_name}'"
        )

    def check_swipe_right_tab(self):
        self.choose_home_tab()
        self.assert_tab(self.HOME_TAB_MESSAGE, "HomeFragment")

        action_gestures.swipe_to("right")
        self.assert_tab(self.SPORT_TAB_MESSAGE, "SportFragment")

        action_gestures.swipe_to("right")
        self.assert_tab(self.MOVIE_TAB_MESSAGE, "MovieFragment")

    def check_swipe_left_tab(self):
        self.choose_movie_tab()
        self.assert_tab(self.HOME_TAB_MESSAGE, "HomeFragment")

        action_gestures.swipe_to("left")
        self.assert_tab(self.SPORT_TAB_MESSAGE, "SportFragment")

        action_gestures.swipe_to("left")
        self.assert_tab(self.MOVIE_TAB_MESSAGE, "MovieFragment")

    def assert_tab(self, locator, expected_tab):
        actual_tab = self.driver.find_element(locator)
        assert actual_tab == expected_tab, (
            f"Expected text: '{expected_tab}'," f"\nActual text: '{actual_tab}'"
        )

    def check_swipe_right_between_tabs(self):
        self.choose_home_tab()
        try:
            actual_tab = self.driver.find_element(self.HOME_TAB_MESSAGE)
        except NoSuchElementException:
            actual_tab = None

        while True:
            if actual_tab == self.HOME_TAB_MESSAGE:
                action_gestures.swipe_to("right")
                break
            else:
                self.choose_home_tab()
                actual_tab = self.driver.find_element(self.HOME_TAB_MESSAGE)

        new_tab = self.driver.find_element(self.SPORT_TAB_MESSAGE)
        expected_message_tab_name = "SportFragment"
        assert new_tab == expected_message_tab_name, (
            f"Expected text: '{expected_message_tab_name}',1`" f"\nActual text: '{new_tab}'"
        )
