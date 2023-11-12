import json
import os

from appium import webdriver

from utils.constants import General

constants = General()


class KWALauncher:
    def __init__(self):
        current_directory = os.path.dirname(__file__)
        capabilities_path = os.path.join(current_directory, constants.CAPABILITIES_PATH)

        with open(capabilities_path, "r") as json_file:
            self.appium_options = json.load(json_file)

        # Convert absolute path to relative path
        self.appium_options[constants.APP_IN_CAPABILITIES_JSON_PATH] = os.path.relpath(
            self.appium_options[constants.APP_IN_CAPABILITIES_JSON_PATH], start=current_directory
        )

        self.driver = self.launch_app()

    def launch_app(self):
        return webdriver.Remote(constants.SERVER_PATH, self.appium_options)

    def get_driver(self):
        return self.driver