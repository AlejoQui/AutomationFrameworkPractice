import json
import os

from appium import webdriver


class KWALauncher:
    def __init__(self):
        current_directory = os.path.dirname(__file__)
        relative_path = 'config/capabilities.json'
        capabilities_path = os.path.join(current_directory, relative_path)

        with open(capabilities_path, 'r') as json_file:
            self.appium_options = json.load(json_file)

        # Convert absolute path to relative path
        self.appium_options['app'] = os.path.relpath(self.appium_options['app'], start=current_directory)

        self.driver = self.launch_app()

    def launch_app(self):
        return webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.appium_options)

    def get_driver(self):
        return self.driver
