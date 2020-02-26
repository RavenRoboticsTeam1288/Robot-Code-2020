#Raven Robotics 2019 Deep Space
#
#This class implements control for the robot's driving mechanism, 
#apecifically a mecanum drive.
#

import wpilib
from wpilib.drive import MecanumDrive

class DrivetrainController():

    def __init__(self, robot):

        #Drivetrain Motor Setup
        self.rightFrontMotor = wpilib.Talon(7) #Right front
        self.rightBackMotor = wpilib.Talon(6) #Right back
        self.leftFrontMotor = wpilib.Talon(8) #Left front
        self.leftBackMotor = wpilib.Talon(9) #Left back

        #Mecanum Drive Setup
        robot.drive = MecanumDrive(self.leftFrontMotor, 
                                  self.leftBackMotor, 
                                  self.rightFrontMotor, 
                                  self.rightBackMotor)


    def teleopPeriodic(self, robot):

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

    def autonomousInit(self, robot):
        robot.drive.setSafetyEnabled( False )
        
    def teleopInit(self, robot):
        robot.drive.setSafetyEnabled( True )
        
