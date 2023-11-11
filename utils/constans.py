class General:
    DEVICE_HEIGHT = "height"
    DEVICE_WIDTH = "width"
    CAPABILITIES_PATH = "../config/capabilities.json"
    SERVER_PATH = "http://127.0.0.1:4723/wd/hub"
    APP_IN_CAPABILITIES_JSON_PATH = "app"
    COORDINATES_SWIPE_TO = "../config/constans_swipe_to.json"
    COORDINATES_START_X = "start_x"
    COORDINATES_START_Y = "start_y"
    COORDINATES_END_X = "end_x"
    COORDINATES_END_Y = "end_y"


class ErrorMessages:
    INVALID_INPUT = "Invalid Input"


class InformativeMessage:
    SWIPE_NO_VALID = "It is not possible to swipe"
