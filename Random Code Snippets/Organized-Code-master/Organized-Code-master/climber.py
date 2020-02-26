#Raven Robotics 2019 Deep Space
#
#This class implements control for the robot's climbing mechanism, 
#including three "actuator" motors (left, right, and back), 
#and the drive wheel motor at the bottom of the back actuator.
#

import wpilib
from Utilities import UtilityFunctions

class ClimberController():

    def __init__(self):

        #Climber Motor Setup
        self.climberRight = wpilib.Talon(4)
        self.climberLeft = wpilib.Talon(3)
        self.climberBack = wpilib.Talon(2)
        self.climberWheel = wpilib.Talon(18)

        #Encoders Setup
        self.backEncoder = wpilib.Encoder(2, 3, False, wpilib.Encoder.EncodingType.k1X)
        self.leftEncoder = wpilib.Encoder(4, 5, False, wpilib.Encoder.EncodingType.k1X)
        self.rightEncoder = wpilib.Encoder(0, 1, False, wpilib.Encoder.EncodingType.k1X)

        # These are commented out because I think they're redundant,
        # encoder counts should automatically be set to zero upon initialization
        # self.backEncoder.reset()
        # self.leftEncoder.reset()
        # self.rightEncoder.reset()

        #Misc Variables Setup
        self.extend19 = 247000 #the number of encoder counts to extend any actuator by 19 inches
        self.extend6 = 78000 #the number of encoder counts to extend any actuator by 6 inches
        self.fullRetract = 500
        self.extendSpeed = .35
        self.retactSpeed = -.25
        self.climbWheelSpeed = .1
        self.encoderMotor = {self.backEncoder : self.climberBack, self.rightEncoder : self.climberRight, self.leftEncoder : self.climberLeft}
        #self.actuatorMove = {self.climberBack : True, self.climberRight : True, self.climberLeft : True}
        


    def teleopPeriodic(self, robot):

        #Extend all three actuators until they have reached 19 inches.
        #Monitor the position of each encoder and don't let any of them lead the others by more than 0.5 inches
        if robot.stick1.getRawButton(8):
            if UtilityFunctions.encoderCompareUp(self, self.backEncoder, self.encoderMotor) == True and self.backEncoder.get() <= self.extend19:
                self.climberBack.set(self.extendSpeed)
            else:
                self.climberBack.set(0)
            if UtilityFunctions.encoderCompareUp(self, self.leftEncoder, self.encoderMotor) == True and self.leftEncoder.get() <= self.extend19:
                self.climberLeft.set(self.extendSpeed)
            else:
                self.climberLeft.set(0)
            if UtilityFunctions.encoderCompareUp(self, self.rightEncoder, self.encoderMotor) == True and self.rightEncoder.get() <= self.extend19:
                self.climberRight.set(self.extendSpeed)
            else:
                self.climberRight.set(0)
                
        #Retract the left and right actuators until they reach their home position (zero encoder value)
        #Monitor the position of each encoder and don't let any of them lead the others by more than 0.5 inches
        elif robot.stick2.getRawButton(8):
            if UtilityFunctions.encoderCompareDown(self, self.leftEncoder, self.encoderMotor) == True and self.backEncoder.get() >= self.fullRetract:
                self.climberLeft.set(self.retactSpeed)
            else:
                self.climberLeft.set(0)
            if UtilityFunctions.encoderCompareDown(self, self.rightEncoder, self.encoderMotor) == True and self.backEncoder.get() >= self.fullRetract:
                self.climberRight.set(self.retactSpeed)
            else:
                self.climberRight.set(0)
                
        #Retract the back actuators until it reaches its home position (zero encoder value)
        elif robot.stick2.getRawButton(9):
            if self.backEncoder.get() >= self.fullRetract:
                self.climberBack.set(self.retactSpeed)
            else:
                self.climberBack.set(0)
                
        else:
            self.climberRight.set(0)
            self.climberLeft.set(0)
            self.climberBack.set(0)

        #Drive the back actuator's driver wheel forward
        if robot.stick1.getRawButton(9):
            self.climberWheel.set(self.climbWheelSpeed)
        else:
            self.climberWheel.set(0)
            
        #FOR TESTING: Reset the actuator encoders to zero
        if robot.stick1.getRawButton(11):
            print('Reset Climber Encoders')
            self.backEncoder.reset()
            self.leftEncoder.reset()
            self.rightEncoder.reset()
            
        #FOR TESTING: Display all the actuator encoder values on the console
        if robot.stick2.getRawButton(11):
            print('Encoder.Back: ' + str(self.backEncoder.get()))
            print('Encoder.Left: ' + str(self.leftEncoder.get()))
            print('Encoder.Right: ' + str(self.rightEncoder.get()))
