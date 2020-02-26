#Raven Robotics 2020 Infinite Recharge
#
#This class implements control for the robot's driving mechanism, 
#Specifically a tank drive.
#

import wpilib
from wpilib.drive import DifferentialDrive
import ctre

class DrivetrainController():

    def __init__(self, robot):# This defines __init__(self, robot):

        #Drivetrain Motor Setup
    
        '''self.frontLeft = wpilib.Victor(9)
        #self.frontLeft.setInverted(True)
        self.rearLeft = wpilib.Victor(5)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Victor(7)
        #self.frontRight.setInverted(True)
        self.rearRight = wpilib.Victor(8)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        robot.drive = DifferentialDrive(self.left, self.right)'''

        self.redLine = ctre.WPI_VictorSPX(1)
        self.redLine1 = ctre.WPI_VictorSPX(2)
        

    def teleopPeriodic(self, robot):

        #Joystick Axis Setup
        stick1_Y = robot.stick1.getY()
        stick2_Y = robot.stick2.getY()
        
        #Dominant Joystick thing
        if robot.stick1.getButton(1):
            stick2_Y = stick1_Y
        if robot.stick2.getButton(1):
            stick1_Y = stick2_Y

        #Joystick Deadzone Setup
        if stick1_Y > -0.05 and stick1_Y < 0.05:
            stick1_Y = 0
        if stick2_Y > -0.05 and stick2_Y < 0.05:
            stick2_Y = 0
        
        #Fine range control
        if robot.stick1.getButton(2) or robot.stick2.getButton(2):
            stick1_Y *= 0.5
            stick2_Y *= 0.5
        
        #Tank Drive Setup
        #robot.drive.tankDrive(stick1_Y, stick2_Y)

        if robot.stick1.getRawButton(2):
            self.redLine.set(0.5)
        else:
            self.redLine.set(0.0)

    def autonomousInit(self, robot):
        #robot.drive.setSafetyEnabled( False )
        pass
        
    def teleopInit(self, robot):
        #robot.drive.setSafetyEnabled( True )
        pass
