#Raven Robotics 2020 Infinite Recharge
#
#This class implements control for the robot's driving mechanism,
#Specifically a tank drive.
#

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib.drive import MecanumDrive
import ctre
import utilities
from utilities import utilities

class DrivetrainController():

    def __init__(self, robot):# This defines __init__(self, robot):

        #Drivetrain Motor Setup
        #Setup for Tank Drive
        self.frontLeft = ctre.WPI_TalonSRX(9)
        #self.frontLeft.setInverted(True)
        self.rearLeft = ctre.WPI_TalonSRX(5)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)
        self.frontRight = ctre.WPI_TalonSRX(7)
        #self.frontRight.setInverted(True)
        self.rearRight = ctre.WPI_TalonSRX(8)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)
        robot.drive = DifferentialDrive(self.left, self.right)
        
        #Can bus Mecanum Drive
        '''self.frontLeft = ctre.WPI_VictorSPX(4)
        self.rearLeft = ctre.WPI_VictorSPX(3)
        self.frontRight = wpilib.Talon(0)
        self.rearRight = ctre.WPI_VictorSPX(2)
        robot.drive = MecanumDrive(self.frontLeft, self.rearLeft, self.frontRight, self.rearRight)'''
    
    #---------------------------------------------------------------------------------------------------
    
    def teleopPeriodic(self, robot):

        #Joystick Axis Setup
        stick1_Y = robot.stick1.getY()
        stick2_Y = robot.stick2.getY()

        #Dominant Joystick thing
        if robot.stick1.getRawButton(1):
            stick2_Y = stick1_Y
        if robot.stick2.getRawButton(1):
            stick1_Y = stick2_Y

        #Joystick Deadzone Setup
        if stick1_Y > -0.05 and stick1_Y < 0.05:
            stick1_Y = 0
        if stick2_Y > -0.05 and stick2_Y < 0.05:
            stick2_Y = 0

        #Fine range control
        if robot.stick1.getRawButton(2) or robot.stick2.getRawButton(2):
            stick1_Y *= 0.5
            stick2_Y *= 0.5

        robot.gamepad.getRawButton(1):
            utilities.ControlPanelDriving(robot)
            
        #Tank Drive Setup
        robot.drive.tankDrive(stick1_Y, stick2_Y)

    #--------------------------------------------------------------------    
        
    def autonomousInit(self, robot):
        robot.drive.setSafetyEnabled( False )
        pass

    def autonomousPeriodic(self, robot):
        autostate = 'Ideal'
    #Ideal Start™
        if autostate == 'Ideal':
            done = utilities.driveNumInches(robot, 1, .5, 24)
            if done:
                autostate = 'done'
        elif autostate == 'aim':
            done = utilities.ultrasonicAim(robot, 2)
            if done:
                autostate = 'shoot'
        elif autostate == 'shoot':
            pass #shooting auto code
        elif autostate == 'done': #says auto is complete, you can rest until teleop
            return True

    #First alternate Start™
        if autostate == 'Alt1':
            print("gotz to drivezz")
            pass #gyro
        elif autostate == 'move':
            done = utilities.DriveNumInches(MyRobot, 1, .5, 48)
            if done:
                autostate = 'aim'
        elif autostate == 'aim':
            done = utilities.ultrasonicAim(MyRobot, 'FIX HERE')
            if done:
                autostate = 'shoot'
        elif autostate == 'shoot':
            pass #shooting auto code
        elif autostate == 'done': #says auto is complete, you can rest until teleop
            return True

    #second alternate start tm
        if autostate == 'Alt2':
            print("gotz to drivez")
            pass #gyro
        elif autostate == 'move':
            done = utilities.DriveNumInches(MyRobot, 1, .5, (30 * 12))
            if done:
                autostate = 'aim'
        elif autostate == 'aim':
            done = utilities.ultrasonicAim(MyRobot, 'FIX HERE')
            if done:
                autostate = 'shoot'
        elif autostate == 'shoot':
            pass #shooting auto code
        elif autostate == 'done': #says auto is complete, you can rest until teleop
            return True



    def teleopInit(self, robot):
        robot.drive.setSafetyEnabled( True )
        pass
