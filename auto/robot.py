import wpilib
from networktables import NetworkTables
from drivetrain import DrivetrainController
from wpilib import Encoder
import autoStates
from autoStates import AutoStates
from wpilib import interfaces
#from arm import ArmController
#from climber import ClimberController

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        self.sd = NetworkTables.getTable('SmartDashboard')

        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

        #Drivetrain Controller Setup, create the drive control object for the robot
        self.drivetrainController = DrivetrainController(self)

        '''#Arm Controller Setup, create the arm control object for the robot
        self.armController = ArmController()
        #Climber Controller Setup, create the climber control object for the robot
        self.climberController = ClimberController()'''

        self.encoderLeft = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X) #left drive
        self.encoderRight = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X) #right drive

        self.gyro = wpilib.AnalogGyro(3)
        self.ultrasonic = wpilib.Ultrasonic(0, 1)

        self.autostate = 'start'
        self.autoComplete = False

    def autonomousPeriodic(self):

        if self.autoComplete:
            self.left.set(0)
            self.right.set(0)
            #shooter stop too
            #chill until teleop
        else:
            #autostate function calling hell
            self.autoComplete = AutoStates.portStart(self)

    def autonomousInit(self):
        self.drivetrainController.autonomousInit(self)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        self.drivetrainController.autonomousInit(self)

    def teleopPeriodic(self):

        #Drivetrain Controller
        self.drivetrainController.teleopPeriodic(self)

        #if robot.gamepad.getRawButton(1):
            #utilities.turnNumDegrees(self, 45, .1, 1)

        '''#Arm Controller
        self.armController.teleopPeriodic(self)
        #Climber Controller
        self.climberController.teleopPeriodic(self)'''


if __name__ == '__main__':
    wpilib.run(MyRobot)
