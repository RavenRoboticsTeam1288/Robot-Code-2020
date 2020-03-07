#Library Imports
import wpilib
import ctre
from networktables import NetworkTables
from wpilib import SmartDashboard
from ctre import TalonSRX
from wpilib import Encoder
from wpilib import interfaces

#Subfile imports
from drivetrain import DrivetrainController
from autoStates import AutoStates
from utilities import utilities
from Ultrasonic import Ultrasonic
from climber_and_colorSensor import ClimberController
from Shooter import ShooterController

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        #Trying to start up all the commands for Shuffleboard upon boot
        self.sd = NetworkTables.getTable('SmartDashboard')
        #self.sd.putBoolean("IdealStart", True)
        self.sd.putNumber("bruh moment", 2.7)
        self.sd.putString("Start Position", "panic")
        #wpilib.CameraServer.launch('camera.py:main')

        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

        #Drivetrain Controller Setup, create the drive control object for the robot
        self.drivetrainController = DrivetrainController(self)

        #Climber Controller Setup, create the climber control object for the robot
        self.climberController = ClimberController()

        '''self.encoderLeft = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X) #left driv - fix to canbus
        self.encoderRight = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X) #right drive - fix to canbus
        self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X) #climber encoder - fix to canbus'''

        #Start up the other sensors that are needed that aren't using Can Bus
        self.gyro = wpilib.AnalogGyro(3)
        self.Servo = wpilib.PWM(4)
        self.ultrasonic = wpilib.AnalogInput(2)

        self.autostate = 'Test'
        self.autoComplete = False

        #PID Loop Setup for the flywheel
        self.AutoTimer = wpilib.Timer()
        self.AutoTimer.start()

        self.TestMotor = ctre.TalonSRX(4)
        self.fleshWound = wpilib.Timer()
        self.fleshWound.start()

        #Setup for the shooter sub file
        self.ShooterController = ShooterController(self)

    def autonomousPeriodic(self):
        #self.drivetrainController.autonomousPeriodic(self)
        if self.autoComplete:
            self.drivetrainController.left.set(0)
            self.drivetrainController.right.set(0)
            #shooter stop too
            #chill until teleop
        else:
            #autostate function calling hell
            if self.sd.getString("Start Position", "") == "1":
                self.autoComplete = AutoStates.portStart(self)
                print("portStart")
            elif self.sd.getString("Start Position", "") == "2":
                self.autoComplete = AutoStates.lastResortStart(self)
                print("lastResortStart")
        #self.ShooterController.autonomousPeriodic(self)
        #self.drivetrainController.autonomousPeriodic(self)

    def autonomousInit(self):
        self.autostate = 'Test'
        self.autoComplete = False
        self.ShooterController.autonomousInit(self)
        moveSafe = "empty"
        #self.drivetrainController.autonomousInit(self)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.Servo.setRaw(180)
        #Drivetrain Controller
        self.drivetrainController.teleopPeriodic(self)
        self.climberController.teleopPeriodic(self)

        #Drivetrain
        #self.DrivetrainController.teleopPeriodic(self)

        #Shooter
        self.ShooterController.teleopPeriodic(self)

        '''#Arm Controller
        self.armController.teleopPeriodic(self)'''

        #Climber Controller
        #self.climberController.teleopPeriodic(self)

        #ultrasonic
        #self.ultrasonic.getDistance()
        #print(self.sd.getString("Start Position", ""))
        #print(self.gyro.getAngle())
        self.sd.putNumber("angle", self.gyro.getAngle())
        if self.sd.containsKey('TEST'):
            #print("works")
            print(self.sd.getValue('test'))

if __name__ == '__main__':
    wpilib.run(MyRobot)
