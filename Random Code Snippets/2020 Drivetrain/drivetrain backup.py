#Raven Robotics 2020 Infinite Recharge
#
#This class implements control for the robot's driving mechanism, 
#Specifically a tank drive.
#

import wpilib
from wpilib.drive import DifferentialDrive

class DrivetrainController():

    def __init__(self, robot):

        #Drivetrain Motor Setup
    
        self.frontLeft = wpilib.Victor(9)
        #self.frontLeft.setInverted(True)
        self.rearLeft = wpilib.Victor(5)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Victor(7)
        #self.frontRight.setInverted(True)
        self.rearRight = wpilib.Victor(8)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        robot.drive = DifferentialDrive(self.left, self.right)
        

    def teleopPeriodic(self, robot):

        #Joystick Axis Setup
        stick1_Y = robot.stick1.getY()
        stick2_Y = robot.stick2.getY()

        #Joystick Deadzone Setup
        if stick1_Y > -0.05 and stick1_Y < 0.05:
            stick1_Y = 0
        if stick2_Y > -0.05 and stick2_Y < 0.05:
            stick2_Y = 0

        #Tank Drive Setup
        robot.drive.tankDrive(stick1_Y, stick2_Y)

    def autonomousInit(self, robot):
        robot.drive.setSafetyEnabled( False )
        
    def teleopInit(self, robot):
        robot.drive.setSafetyEnabled( True )
        
