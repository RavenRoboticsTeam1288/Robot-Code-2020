import wpilib
from networktables import NetworkTables
from drivetrain import DrivetrainController
from wpilib import Encoder
from autoStates import autoStates
from wpilib import interfaces
from climber import ClimberController
from Ultrasonic import Ultrasonic

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        self.sd = NetworkTables.getTable('SmartDashboard')
        wpilib.CameraServer.launch('camera.py:main')

        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

        #Drivetrain Controller Setup, create the drive control object for the robot
        self.drivetrainController = DrivetrainController(self)

        #Climber Controller Setup, create the climber control object for the robot
        self.climberController = ClimberController()

        self.encoderLeft = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X) #left drive
        self.encoderRight = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X) #right drive

        self.gyro = wpilib.AnalogGyro(1)
        self.ultrasonic = Ultrasonic(2)

        self.autostate = 'start'
        self.autoComplete = False

    def autonomousPeriodic(self):
        self.drivetrainController.autonomousPeriodic(self)
        if self.autoComplete:
            self.left.set(0)
            self.right.set(0)
            #shooter stop too
            #chill until teleop
        else:
            #autostate function calling hell
            #self.autoComplete = autoStates.portStart(self)
            pass

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
        self.armController.teleopPeriodic(self)'''

        #Climber Controller
        self.climberController.teleopPeriodic(self)

        #ultrasonic
        self.ultrasonic.getDistance()

if __name__ == '__main__':
    wpilib.run(MyRobot)
