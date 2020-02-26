#Raven Robotics 2019 Deep Space
#
#This class implements control for the robot's driving mechanism, 
#apecifically a mecanum drive.
#
import wpilib
from wpilib.drive import MecanumDrive
import utilities

class DrivetrainController():

    def __init__(self, robot):

        #Drivetrain Motor Setup
        robot.rightFrontMotor = wpilib.Talon(7) #Right front
        self.rightBackMotor = wpilib.Talon(6) #Right back
        self.leftFrontMotor = wpilib.Talon(8) #Left front
        self.leftBackMotor = wpilib.Talon(9) #Left back

        #Mecanum Drive Setup
        robot.drive = MecanumDrive(self.leftFrontMotor, 
                                  self.leftBackMotor, 
                                  robot.rightFrontMotor, 
                                  self.rightBackMotor)
        #Auto Stuff
        robot.AutoTimer = wpilib.Timer()
        robot.State = ""

    def autonomousInit(self, robot):
        robot.State = 1
        robot.AutoTimer.start()

    def teleopInit(self, robot):
        pass
        
    def autonomousPeriodic(self, robot):
        robot.drive.setSafetyEnabled(False) #DON'T DELETE THIS
        if robot.State == 1:
            utilities.utilities.DriveNumSecs(robot, 1, .1, 3)
            

    def teleopPeriodic(self, robot):
        robot.drive.setSafetyEnabled(False) #DON'T DELETE THIS

        #Joystick Axis Setup
        stick1_X = robot.stick1.getX()
        stick2_Y = robot.stick2.getY()
        stick2_X = robot.stick2.getX()

        #Joystick Deadzone Setup
        if stick1_X > -0.05 and stick1_X < 0.05:
            stick1_X = 0
        if stick2_Y > -0.05 and stick2_Y < 0.05:
            stick2_Y = 0
        if stick2_X > -0.05 and stick2_X < 0.05:
            stick2_X = 0

        #Mecanum Drive Setup
        robot.drive.driveCartesian( -stick2_X, -stick2_Y, -stick1_X, 0 )

    
        
    
        
