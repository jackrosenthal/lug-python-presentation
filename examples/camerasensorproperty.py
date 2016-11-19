class CameraSensor:
    def __init__(self):
        self._brightness = 10

    def take_picture(self):
        # do something
        return image

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if not 0 <= value <= 100:
            raise ValueError
        self._brightness = value
