import wpilib

class Ultrasonic():
    def __init__(self, pin):
        self.pin = pin
        self.analog = wpilib.AnalogInput(pin)
    def getDistance(self):
        return self.analog.getValue()
