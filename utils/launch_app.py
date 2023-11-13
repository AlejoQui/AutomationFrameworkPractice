import json
from os.path import isfile
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
        self.verify_constants_file()

    def verify_constants_file(self):
        if not self.constants_path.is_file():
            raise FileNotFoundError(f"Constants file not found: {self.constants_path}")
        else:
            print(f"Constants file found: {self.constants_path}")

    @staticmethod
    def load_capabilities(file_path):
        print(f"Verify: Attempting to load file from: {file_path}")
        try:
            utils_directory = Path(__file__).resolve().parent
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice\utils
            framework_practice_directory = utils_directory.parent
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice
            capabilities_json_path = (framework_practice_directory / file_path).resolve()
            # Get C:\Users\Alejandro Q\Desktop\FrameworkPractice\config\capabilities.json

            with open(capabilities_json_path, 'r') as file:
                capabilities = json.load(file)

            app_path = Path(capabilities.get('app'))

            if app_path.is_absolute():
                return capabilities
            else:
                absolute_path = (framework_practice_directory / app_path).resolve()
                capabilities['app'] = str(absolute_path)
                print(f'Ruta convertida {absolute_path}')
                return capabilities

        except FileNotFoundError as e:
            raise ValueError(f"Error verifying app path in JSON: File not found - {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error verifying app path in JSON: JSON decoding error - {e}")
        except Exception as e:
            raise ValueError(f"Error verifying app path in JSON: {e}")

    @staticmethod
    def verify_apk_file(file_path):
        try:
            apk_path = file_path.get('app')

            if not apk_path:
                raise FileNotFoundError("The 'app' key is missing in the JSON.")

            apk_path = Path(apk_path)
            print(f"Absolute APK path: {apk_path}")

            if not apk_path.exists():
                raise FileNotFoundError(f"The APK file does not exist at the specified path: {apk_path}."
                                        f"Please check the 'capabilities.json' file and "
                                        f"verify that the 'app' key is present.")

            print(f"APK file exists: {isfile(apk_path)}")

        except FileNotFoundError as e:
            raise ValueError(f"Error loading capabilities from file: File not found - {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error loading capabilities from file: JSON decoding error - {e}")
        except Exception as e:
            raise ValueError(f"Error loading capabilities from file: {e}")

    def launch_app(self):
        try:
            capabilities_file_path = self.constants.CAPABILITIES_PATH
            capabilities_json = self.load_capabilities(capabilities_file_path)
            self.verify_apk_file(capabilities_json)

            self.driver = webdriver.Remote(self.constants.SERVER_PATH, capabilities_json)

        except WebDriverException as e:
            raise WebDriverException(f"Error launching the app: {e}")

    def close_app(self):
        try:
            if self.driver:
                self.driver.quit()
                self.driver = None
        except Exception as e:
            raise RuntimeError(f"Error closing the app: {e}")
