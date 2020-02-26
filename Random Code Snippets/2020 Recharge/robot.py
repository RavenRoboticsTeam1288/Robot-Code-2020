#robot Python
import wpilib

class MyRobot():

    def __init__(self):

        self.stick1 = wpilib.Joystick(1)
        self.stick2 = wpilib.Joystick(2)
        self.gamepad = wpilib.Joystick(3)

