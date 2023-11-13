import json
import os
from pathlib import Path

from appium import webdriver
from selenium.common import WebDriverException

from utils.constants import General


class KWALauncher:
    def __init__(self, constants_path="constants.py"):
        self.script_directory = Path(__file__).resolve().parent
        self.constants_path = self.script_directory / constants_path
        self.driver = None

        self.constants = General()
        self.initialize()

    def initialize(self):
        if not self.constants_path.is_file():
            raise FileNotFoundError(f"Constants file not found: {self.constants_path}")
        else:
            print(f"Constants file found: {self.constants_path}")

    @staticmethod
    def load_capabilities_from_file(file_path):
        print(f"Attempting to load file from: {file_path}")
        try:
            utils_directory = Path(__file__).resolve().parent
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice\utils
            framework_practice_directory = utils_directory.parent
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice
            capabilities_json_path = os.path.join(framework_practice_directory, file_path)
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice\config\capabilities.json

            with open(capabilities_json_path, 'r') as file:
                capabilities = json.load(file)

            if 'app' not in capabilities:
                raise ValueError("Check the 'capabilities.json'. Verify that the 'app' key is present.")

            script_directory = Path(__file__).resolve().parent
            main_directory = script_directory.parent
            apk_relative_path = capabilities['app']
            apk_path = os.path.abspath(os.path.join(main_directory, apk_relative_path))
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice\config\Android_Demo_App.apk

            print(f"Absolute APK path: {apk_path}")
            print(f"APK file exists: {os.path.isfile(apk_path)}")

            if not os.path.isfile(apk_path):
                raise FileNotFoundError(f"The APK file was not found at the specified path: {apk_path}."
                                        f"Please check the 'capabilities.json' file and "
                                        f"verify that the 'app' key is present.")

            return capabilities

        except FileNotFoundError as e:
            raise ValueError(f"Error loading capabilities from file: File not found - {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error loading capabilities from file: JSON decoding error - {e}")
        except Exception as e:
            raise ValueError(f"Error loading capabilities from file: {e}")

    def launch_app(self):
        try:
            capabilities_file_path = self.constants.CAPABILITIES_PATH
            capabilities = self.load_capabilities_from_file(capabilities_file_path)

            self.driver = webdriver.Remote(self.constants.SERVER_PATH, capabilities)

        except WebDriverException as e:
            raise WebDriverException(f"Error launching the app: {e}")
        finally:
            os.chdir(self.script_directory)

    def close_app(self):
        try:
            if self.driver:
                self.driver.quit()
                self.driver = None
        except Exception as e:
            raise RuntimeError(f"Error closing the app: {e}")
