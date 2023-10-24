import json

from appium import webdriver


class KWALauncher:
    def __init__(self):

        with open(r'C:\Users\Alejandro Q\Desktop\FrameworkPractice\config\capabilities.json', 'r') as json_file:
            self.appium_options = json.load(json_file)

        self.driver = self.launch_app()

    def launch_app(self):
        return webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.appium_options)

    def get_driver(self):
        return self.driver
