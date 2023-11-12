from utils.constants import General
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
driver = app_launcher.get_driver()
constants = General()


class ResolutionDevice:
    def __init__(self):
        self.SCREEN_HEIGHT = 0
        self.SCREEN_WIDTH = 0

    def get_resolution(self):
        resolution_screen = driver.get_window_size()
        self.SCREEN_HEIGHT = resolution_screen[constants.DEVICE_HEIGHT]
        self.SCREEN_WIDTH = resolution_screen[constants.DEVICE_WIDTH]
