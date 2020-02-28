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
from climber_and_colorSenor import ClimberController

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        
        #Trying to start up all the commands for Shuffleboard upon boot
        self.sd = NetworkTables.getTable('SmartDashboard')
        #self.sd.putBoolean("IdealStart", True)
        self.sd.putNumber("bruh moment", 2.7)
        self.sd.putString("Start Position", "Panic")
        #wpilib.CameraServer.launch('camera.py:main')

        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

        #Drivetrain Controller Setup, create the drive control object for the robot
        self.drivetrainController = DrivetrainController(self)

        #Climber Controller Setup, create the climber control object for the robot
        self.climberController = ClimberController()
        self.Winch = ctre.WPI_VictorSPX(1)
        self.Scissor = ctre.WPI_VictorSPX(2)
        self.coFlyWheel = ctre.WPI_VictorSPX(3)
        self.stickLift = ctre.WPI_VictorSPX(4)

        '''self.encoderLeft = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X) #left driv - fix to canbus
        self.encoderRight = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X) #right drive - fix to canbus
        self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X) #climber encoder - fix to canbus'''

        #Start up the other sensors that are needed that aren't using Can Bus
        self.gyro = wpilib.AnalogGyro(3)
        self.Servo = wpilib.PWM(4)
        self.ultrasonic = wpilib.AnalogInput(2)

        self.autostate = 'start'
        self.autoComplete = False

        #PID Loop Testing

        self.TestMotor = ctre.TalonSRX(4)
        self.fleshWound = wpilib.Timer()
        self.fleshWound.start()
        
        self.climberController = ClimberController()
        
        self.ShooterController = ShooterController(self)




        #self.PIDLoop = wpilib.PIDLoopController(1, 0, 0, 0, self.TestEncoder, self.TestMotor, .05)


    def autonomousPeriodic(self):
        self.drivetrainController.autonomousPeriodic(self)
        if self.autoComplete:
            self.left.set(0)
            self.right.set(0)
            #shooter stop too
            #chill until teleop
        else:
            #autostate function calling hell
            if self.sd.getString("Start Position", "") == "offStart":
                self.autoComplete = utilities.offStart(self)
            elif self.sd.getString("Start Position", "") == "portStart":
                self.autoComplete = utilities.portStart(self)
            elif self.sd.getString("Start Position", "") == "lastResortStart":
                self.autoComplete = utilities.lastResortStart(self)
        self.ShooterController.autonomousPeriodic(self)
        self.DrivetrainController.autonomousPeriodic(self)

    def autonomousInit(self):
        self.autostate = 'start'
        self.autoComplete = False
        self.ShooterController.autonomousInit(self)
        self.DrivetrainController.autonomousInit(self)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        self.drivetrainController.autonomousInit(self)
        self.TestMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder,0,0)
        self.blackKnight = 0
        self.TestMotor.config_kF(0, 0.01, 0)
        self.TestMotor.config_kP(0, 0.001, 0) #What is the proportional gain of an unladden swallow?
        self.TestMotor.config_kI(0, 0.00001, 0)
        self.TestMotor.config_kD(0, 0.0, 0)

    def teleopPeriodic(self):
        self.Servo.setRaw(180)
        #Drivetrain Controller
        self.drivetrainController.teleopPeriodic(self)
        self.climberController.teleopPeriodic(self)
        self.drivetrainController.frontRight.set(.5)
        #PID Loop Testing
        if self.gamepad.getRawButton(5):
            print("B R U H")
            #some thing to run the motor written by the upperclass twits
            self.TestMotor.set(ctre.ControlMode.Velocity, 10240)
        else:
            self.TestMotor.set(ctre.ControlMode.Velocity, 0)

        if self.fleshWound.hasPeriodPassed(.1):
            vel = (self.TestMotor.getSelectedSensorPosition(0) - self.blackKnight) * 10
            print("bruh " + str(vel) + ", " + str(self.TestMotor.getSelectedSensorPosition(0)))
            self.blackKnight = self.TestMotor.getSelectedSensorPosition(0)
            self.fleshWound.reset()
            self.fleshWound.start()

        #Drivetrain
        self.DrivetrainController.teleopPeriodic(self)

        #Shooter
        self.ShooterController.teleopPeriodic(self)


        #print(self.TestMotor.getSelectedSensorPosition(0))
        #else:
        #    self.TestMotor.set(ctre.ControlMode.Velocity, 0)
        #if robot.gamepad.getRawButton(1):
            #utilities.turnNumDegrees(self, 45, .1, 1)

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
            print("works")
            print(self.sd.getValue('test'))

if __name__ == '__main__':
    wpilib.run(MyRobot)
