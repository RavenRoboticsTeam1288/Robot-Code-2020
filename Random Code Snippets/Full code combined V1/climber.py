# numbers subject to change
import wpilib
#import ctre

from rev.color import ColorSensorV3
import ColorSensor
#color sensor instalation (py -3 -m pip install -U robotpy-rev-color)

class ClimberController():

    def __init__(self):

        '''self.Winch = ctre.WPI_VictorSPX(1)
        self.Scissor = ctre.WPI_VictorSPX(2)
        self.coFlyWheel = ctre.WPI_VictorSPX(3)
        self.stickLift = ctre.WPI_VictorSPX(4)'''
        self.Winch = wpilib.Victor(1)
        self.Scissor = wpilib.Victor(2)
        self.Scissor.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder,0,0)
        self.TestMotor.config_kP(0, 0.001, 0)
        self.TestMotor.config_kI(0, 0.00001, 0)
        self.TestMotor.config_kD(0, 0.0, 0)
        self.coFlyWheel = wpilib.Victor(3)
        self.stickLift = wpilib.Victor(4)
        self.scissorExtendSpeed = .1
        self.scissorRetractSpeed = -.1
        self.winchRetractSpeed = -.1
        self.CoSpeed = .1
        self.targetB = [(0,255,255) ,(0,206,209)]
        self.targetY = [(255,255,0) ,(184,134,11)]
        self.targetG = [(60,179,113) ,(0,100,0)]
        self.targetR = [(255,0,0) ,(178,34,34)]
        rotations = 0

        self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)

        self.timer = wpilib.Timer()
        '''self.motor1 = ctre.WPI_VictorSPX(3)'''
        self.motor1 = wpilib.Victor(3)
        #self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.colorSensor = ColorSensor.ColorSensor()
        self.colorSensor.setSensor(ColorSensorV3(wpilib.I2C.Port.kOnboard))

    def teleopPeriodic(self, robot):
        if robot.gamepad.getRawButton(6):#getB:
            #self.Scissor.set(self.scissorExtendSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 2500000)
        elif robot.gamepad.getRawButton(7):
            #self.Scissor.set(self.scissorRetractSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 0)
        else:
            self.Scissor.set(0)
        if robot.stick1.getRawButton(3):
            self.Winch.set(self.winchRetractSpeed)
        else:
            self.Winch.set(0)
        if robot.stick1.getRawButton(2):
            self.stickLift.set(self.colorFlyWheelSpeed)
        else:
            self.stickLift.set(0)
#Timer
        if robot.stick1.getRawButton(8):
            self.timer.start()
            self.motor1.set(0.1)

        if self.timer.get() >= 5:
            self.timer.reset()
            self.timer.stop()
            self.motor1.set(0)

#Color sensor V3
        print(self.colorSensor.getColor())
        colorStr = self.colorSensor.getColor()
        proximity = self.colorSensor.sensor.getProximity()

        wpilib.SmartDashboard.putNumber("proximity", proximity)
        wpilib.SmartDashboard.putString("Color", colorStr)
        '''
        color = self.colorSensor.getColor()
        ir = self.colorSensor.getIR()

        red = color.red
        blue = color.blue
        green = color.green

        #Turn color into percents so we don't have funky outputs
        mag = max([red,green,blue])
        red2 = red/mag
        green2 = green/mag
        blue2 = blue/mag
        color_str = None
        if red2 == 1.:
            if green2 >= 0.7 and blue2 <= 0.7:
                color_str = "yellow"
            elif blue2 >= 0.7 and green2 <= 0.7:
                color_str = "magenta"
            else:
                color_str = "red"
        elif blue2 == 1.:
            if red2 >= 0.5 and green2 <= 0.5:
                color_str = "magenta"
            elif green2 >= 0.5 and red2 <= 0.5:
                color_str = "cyan"
            else:
                color_str = "blue"
        elif green2 == 1.:
            if red2 >= 0.5 and blue2 <= 0.5:
                color_str = "yellow"
            elif blue2 >= 0.5 and red2 <= 0.5:
                color_str = "cyan"
            else:
                color_str = "green"
        print(color_str)
        proximity = self.colorSensor.getProximity()
        print(str(red) + "," + str(green) + "," + str(blue))'''

    if __name__ == "__main__":
        wpilib.run(MyRobot)





#Encoder
        '''if self.Encoder.get() < 3000:
            if robot.gamepad.getRawButton(2):
                self.Winch.set(.3)
            elif robot.gamepad.getRawButton(1):
                self.Winch.set(-.3)
            elif self.Encoder.get() > 3000:
                 self.Winch.set(0)
            else:
                 self.Winch.set(0)'''

#Duncan's dumb not working color sensor
'''class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    def robotPeriodic(self):
        # Get the sensor attributes
        color = self.colorSensor.getColor()
        ir = self.colorSensor.getIR()

        # Get the individual components of the color
        red = color.red
        blue = color.blue
        green = color.green

        # Open Smart Dashboard or Shuffleboard to see the color detected by the
        # sensor.
        wpilib.SmartDashboard.putNumber("Red", detectedColor.red)
        wpilib.SmartDashboard.putNumber("Green", detectedColor.green)
        wpilib.SmartDashboard.putNumber("Blue", detectedColor.blue)
        wpilib.SmartDashboard.putNumber("IR", ir)

        # Get the approximate proximity of an object
        proximity = self.colorSensor.getProximity()

    if __name__ == self.timer.stop(): #"__main__"
    wpilib.run(MyRobot

    #def ColorSensorPart1(self):
    if self.joystickbutton(6)
        if self.colorSensor == targetB:
            self.coFlyWheel(self.CoSpeed)
            if color == targetB:
                self.timer.start()
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    1 += rotations
                        if rotations == 5:
                        self.coFlyWheel(0)



        elif self.colorSensor == targetY:
             self.coFlyWheel(self.CoSpeed)
             if color == targetG:
                self.timer.start()
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    1 += rotations
                        if rotations == 5:
                        self.coFlyWheel(0)




        elif self.colorSensor == targetG:
             self.coFlyWheel(self.CoSpeed)
             if color == targetG:
                self.timer.start()
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    1 += rotations
                        if rotations == 5:
                        self.coFlyWheel(0)



        elif self.colorSensor == targetR:
             self.coFlyWheel(self.CoSpeed)
             if color == targetR:
                self.timer.start()
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    1 += rotations
                        if rotations == 5:
                        self.coFlyWheel(0)


    #def ColorSensorPart2(self):
    if self.joystickbutton(3)
        if self.colorsensor == targetR:
            if self.colorsensor =\ targetR
                self.coFlyWheel(self.CoSpeed)
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    self.coFlyWheel(0)
        else:
            self.timer.start()
            self.coFlyWheel(self.CoSpeed)
            if self.timer.get() >= 5:
                self.timer.reset()
                self.timer.stop()
                self.coFlyWheel(0)



        elif self.colorsensor == targetB:
            if self.colorsensor =\ targetB:
                self.coFlyWheel(self.CoSpeed)
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    self.coFlyWheel(0)
        else:
            self.timer.start()
            self.coFlyWheel(self.CoSpeed)
            if self.timer.get() >= 5:
                self.timer.reset()
                self.timer.stop()
                self.coFlyWheel(0)



        elif self.colorsensor == targetY:
            if self.colorsensor =\ targetY:
                self.coFlyWheel(self.CoSpeed)
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    self.coFlyWheel(0)
        else:
            self.timer.start()
            self.coFlyWheel(self.CoSpeed)
            if self.timer.get() >= 5:
                self.timer.reset()
                self.timer.stop()
                self.coFlyWheel(0)


        elif self.colorsensor == targetG:
            if self.colorsensor =\ targetG:
                self.coFlyWheel(self.CoSpeed)
                if self.timer.get() >= 5:
                    self.timer.reset()
                    self.timer.stop()
                    self.coFlyWheel(0)
        else:
            self.timer.start()
            self.coFlyWheel(self.CoSpeed)
            if self.timer.get() >= 5:
                self.timer.reset()
                self.timer.stop()
                self.coFlyWheel(0)'''

