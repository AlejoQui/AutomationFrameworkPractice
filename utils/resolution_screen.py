from utils.launch_app import KWALauncher

app_launcher = KWALauncher()
driver = app_launcher.get_driver()


class ResolutionDevice:
    def __init__(self):
        self.screen_height = 0
        self.screen_width = 0

    def get_resolution(self):
        resolution_screen = driver.get_window_size()
        self.screen_height = resolution_screen['height']
        self.screen_width = resolution_screen['width']
