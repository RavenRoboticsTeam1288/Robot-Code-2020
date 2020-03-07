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
        self.Winch1 = ctre.WPI_TalonSRX(11)
        self.Winch2 = ctre.WPI_TalonSRX(3)
        self.Winch = wpilib.SpeedControllerGroup(self.Winch1, self.Winch2)
        self.Scissor = ctre.WPI_TalonSRX(9)
        #self.coFlyWheel = ctre.WPI_TalonSRX(5)
        self.stickLift = ctre.WPI_TalonSRX(5)

        #Scissor lift Positional PID loop
        #Starts by getting the the encoder that is connected to the Motor controller
        self.Scissor.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder,0,0)
        self.Scissor.config_kP(0, 0.005, 0) #Configuring the different parts of the loop.
        self.Scissor.config_kI(0, 0.0000001, 0)
        self.Scissor.config_kD(0, 0.0, 0)

        #Misc variable setups
        self.PIDRunning = False
        self.scissorExtendSpeed = .6
        self.scissorRetractSpeed = -.6
        self.winchRetractSpeed = -.1
        self.CoSpeed = .1
        self.LowerLimit = wpilib.DigitalInput(4)
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
        if self.LowerLimit == False:
            self.Scissor.set(0)
            print("Limit Triggered")
        if robot.gamepad.getRawButton(5) and self.Scissor.getSelectedSensorPosition(0) < 2717000:
            print("work")
            #self.Scissor.set(self.scissorExtendSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 2517000)
            self.PIDRunning = True
        elif robot.gamepad.getRawButton(6) and self.Scissor.getSelectedSensorPosition(0) > 0:
            #self.Scissor.set(self.scissorRetractSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 0.0)
            self.PIDRunning = True
        else:
            self.Scissor.set(ctre.ControlMode.Position, self.Scissor.getSelectedSensorPosition())
            #print(self.Scissor.getSelectedSensorPosition(0))
            self.PIDRunning = False

        if robot.gamepad.getRawButton(3):
            self.Scissor.set(.3)
        elif robot.gamepad.getRawButton(4):
            self.Scissor.set(-.3)
        else:
            self.Scissor.set(0)

        if robot.stick1.getRawButton(3):
            self.Winch1.set(self.winchRetractSpeed)
            self.Winch2.set(self.winchRetractSpeed)
        else:
            self.Winch1.set(0)
            self.Winch2.set(0)

        wpilib.SmartDashboard.putBoolean("Scissor limit", self.LowerLimit.get())

#Color sensor V3
        #print(ColorSensor.getColor(self)) #Prints out the color in the terminal
        colorStr = ColorSensor.getColor(self) #Assigns the color it finds to a variable to grab later on
        #proximity = ColorSensor.sensor.getProximity() #Uses the small proximity sensor built into it

        #Uploads the strings and values to shuffle board to be seen easier.
        #wpilib.SmartDashboard.putNumber("proximity", proximity)
        wpilib.SmartDashboard.putString("Color", colorStr)

