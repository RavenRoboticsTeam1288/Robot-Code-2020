# numbers subject to change
import wpilib
import ctre

from rev.color import ColorSensorV3
import colorSensor
from colorSensor import ColorSensor
#color sensor instalation (py -3 -m pip install -U robotpy-rev-color)

class ClimberController():

    def __init__(self):

        #Setup for the Motors using CTRE can bus
        #Uses The phonix Turner Software to Assign the Motor Ids
        self.Winch = ctre.WPI_VictorSPX(1)
        self.Scissor = ctre.TalonSRX(3)
        self.coFlyWheel = ctre.WPI_VictorSPX(2)
        self.stickLift = ctre.WPI_VictorSPX(4)

        #Scissor lift Positional PID loop
        #Starts by getting the the encoder that is connected to the Motor controller
        self.Scissor.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder,0,0)
        self.Scissor.config_kP(0, 0.005, 0) #Configuring the different parts of the loop.
        self.Scissor.config_kI(0, 0.0000001, 0)
        self.Scissor.config_kD(0, 0.0, 0)

        '''self.Winch = wpilib.Victor(1)
        self.Scissor = ctre.WPI_TalonSRX(3)
        self.coFlyWheel = wpilib.Victor(3)
        self.stickLift = wpilib.Victor(4)'''

        #Misc variable setups
        self.scissorExtendSpeed = .6
        self.scissorRetractSpeed = -.6
        self.winchRetractSpeed = -.1
        self.CoSpeed = .1
        rotations = 0

        self.timer = wpilib.Timer()
        self.Scissor.getSensorCollection().setPulseWidthPosition(0, 10)
        '''self.motor1 = ctre.WPI_VictorSPX(3)'''
        self.motor1 = wpilib.Victor(3)
#------------------------------------------------------------------------------------------------------------------------------#

        #Seting up the Color sensor
        #self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        #self.colorSensor = ColorSensor.ColorSensor()
        ColorSensor.setSensor(self, ColorSensorV3(wpilib.I2C.Port.kOnboard))

    def teleopPeriodic(self, robot):
        if robot.gamepad.getRawButton(5) and self.Scissor.getSelectedSensorPosition(0) < 2717000:
            print("work")
            #self.Scissor.set(self.scissorExtendSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 2517000)
        elif robot.gamepad.getRawButton(6) and self.Scissor.getSelectedSensorPosition(0) > 0:
            #self.Scissor.set(self.scissorRetractSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 0.0)
        else:
            self.Scissor.set(ctre.ControlMode.Position, self.Scissor.getSelectedSensorPosition())
            print(self.Scissor.getSelectedSensorPosition(0))
        if robot.stick1.getRawButton(3):
            self.Winch.set(self.winchRetractSpeed)
        else:
            self.Winch.set(0)
        if robot.stick1.getRawButton(2):
            self.stickLift.set(self.CoSpeed)
        else:
            self.stickLift.set(0)

#Color sensor V3
        print(ColorSensor.getColor(self)) #Prints out the color in the terminal
        colorStr = ColorSensor.getColor(self) #Assigns the color it finds to a variable to grab later on
        #proximity = ColorSensor.sensor.getProximity() #Uses the small proximity sensor built into it

        #Uploads the strings and values to shuffle board to be seen easier.
        #wpilib.SmartDashboard.putNumber("proximity", proximity)
        wpilib.SmartDashboard.putString("Color", colorStr)

