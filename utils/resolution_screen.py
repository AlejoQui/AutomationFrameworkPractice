from utils.constants import General
from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
driver = app_launcher.launch_app()
constants = General()


class ResolutionDevice:
    def __init__(self):
        self.SCREEN_HEIGHT = 0
        self.SCREEN_WIDTH = 0

    def get_resolution(self):
        try:
            resolution_screen = driver.get_window_size()
            self.SCREEN_HEIGHT = resolution_screen[constants.DEVICE_HEIGHT]
            self.SCREEN_WIDTH = resolution_screen[constants.DEVICE_WIDTH]
        except Exception as e:
            print(f"Error get resolution: {e}")


