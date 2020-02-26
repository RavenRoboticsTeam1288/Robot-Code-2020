import wpilib
from networktables import NetworkTables
from drivetrain import DrivetrainController
from Shooter import ShooterController

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        self.sd = NetworkTables.getTable('SmartDashboard')
        #wpilib.CameraServer.launch('vision.py:main')

        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

	#Drivetrain Controller Setup, create the drive control object for the robot
        self.DrivetrainController = DrivetrainController(self)

        #Shooter Setup
        self.ShooterController = ShooterController(self)

    def autonomousInit(self):
        self.ShooterController.autonomousInit(self)
        self.DrivetrainController.autonomousInit(self)
    
    def autonomousPeriodic(self):
        self.ShooterController.autonomousPeriodic(self)
        self.DrivetrainController.autonomousPeriodic(self)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        #Drivetrain
        self.DrivetrainController.teleopPeriodic(self)

        #Shooter
        self.ShooterController.teleopPeriodic(self)
            
if __name__ == '__main__':
    wpilib.run(MyRobot)
