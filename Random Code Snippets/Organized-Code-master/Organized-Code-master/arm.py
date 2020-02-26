#Raven Robotics 2019 Deep Space
#
#This class implements control for the robot's arm, including the "shoulder" motor, the "wrist" motor,
#and the "flywheel" motors for picking up and shooting the balls
#

import wpilib

class ArmController():

    def __init__(self):

        #Flywheel motors setup
        self.rightFly = wpilib.Talon(10) #Right Fly Wheel
        self.leftFly = wpilib.Talon(11) #Left Fly Wheel

        #Arm Shoulder and Wrist motor setup
        self.shoulderMotor1 = wpilib.Talon(12) #Arm Shoulder Bottom
        self.shoulderMotor2 = wpilib.Talon(14) #Arm Shoulder Top
        self.wristMotor = wpilib.Talon(13)     #Arm Wrist

        #Encoders Setup
        self.shoulderEncoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)
        self.wristEncoder = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X)

        # These are commented out because I think they're redundant,
        # encoder counts should automatically be set to zero upon initialization
        # self.shoulderEncoder.reset()
        # self.wristEncoder.reset()

        #Misc Variables Setup
        self.ballIntakeSpeed = 0.1
        self.ballSpitSpeed = -0.1
        self.shoulderZ = 0.005
        self.wristZ = 0.005
        self.shoulderSpeedUp = 0.2
        self.shoulderSpeedDown = -0.1
        self.wristSpeedUp = 0.2
        self.wristSpeedDown = -0.1
        self.armHeight1LowS = 14500
        self.armHeight1HighS = 14600
        self.armHeightLowG = 1800
        self.armHeightHighG = 1900
        self.armHeightHigh2 = 23700
        self.armHeightLow2 = 23600
        self.armHeightHigh3 = 32700
        self.armHeightLow3 = 32800
        
        #The setpoint for the shoulder/wrist
        self.shoulderSetpoint = 0
        self.wristSetpoint = 0

        #The position the shoulder/wrist is currently in. Either that being start, 1st, 2nd, 3rd, or manual
        self.shoulderPosition = 'Start'
        self.wristPosition = 'Start'

        #When the shoulder/wrist isn't being conroller manually then the value is False,
        #but when the robot is driving then the value is True
        self.shoulderIsDriving = False
        self.wristIsDriving = False

    def teleopPeriodic(self, robot):
        
        #Test for manual up/down control of the arm's shoulder
        if robot.gamepad.getRawButton(5): #Up
            self.shoulderIsDriving = True
            self.shoulderMotor1.set(self.shoulderSpeedUp)
            self.shoulderMotor2.set(self.shoulderSpeedUp)
            self.shoulderPosition = 'Manual'
        elif robot.gamepad.getRawButton(6): #Down
            self.shoulderIsDriving = True
            self.shoulderMotor1.set(self.shoulderSpeedDown)
            self.shoulderMotor2.set(self.shoulderSpeedDown)
            self.shoulderPosition = 'Manual'
        else: #Stop
            self.shoulderMotor1.set(0)
            self.shoulderMotor2.set(0)
            self.shoulderIsDriving = False
            
        #Shoulder Stablizer
        if True == self.shoulderIsDriving and 'Manual' == self.shoulderPosition:
            self.shoulderSetpoint = self.shoulderEncoder.get()
        else:
            #Equation: speed = error * z
            #If the shoulder is moving more up and down then lower the shoulderZ,
            #If it is still dropping then increase the shoulderZ
            self.shoulderError = self.shoulderSetpoint - self.shoulderEncoder.get()
            speed = self.shoulderError * self.shoulderZ 
            self.shoulderMotor1.set(speed)
            self.shoulderMotor2.set(speed)
            
        #Test for manual up/down control of the arm's wrist
        if robot.gamepad.getRawButton(7):
            self.wristIsDriving = True
            self.wristMotor.set(wristSpeedUp)
            self.wristPosition = 'Manual'
        elif robot.gamepad.getRawButton(8):
            self.wristIsDriving = True
            self.wristMotor.set(wristSpeedDown)
            self.wristPosition = 'Manual'
        else: #Stop
            self.wristMotor.set(0)
            self.wristIsDriving = False

        #Wrist Stablizer
        if True == self.wristIsDriving and 'Manual' == self.wristPosition:
            self.wristSetpoint = self.wristEncoder.get()
        else:
            #Equation: speed = error * z
            #If the shoulder is moving more up and down then lower the shoulderZ,
            #If it is still dropping then increase the shoulderZ
            self.wristError = self.wristSetpoint - self.wristEncoder.get()
            speed = self.wristError * self.wristZ 
            self.wristMotor.set(speed)

        #Shoulder and Wrist Semi-automatic position control
        # if self.gamepad.getRawButton(1): #Hold the button for it to work or it will just keep going 
            # #To bring the arm and hand from starting position
            # self.driving = True
            # if self.armEncoder.get() <= self.armHeightHighG:
                # self.armMotor1.set(.1)
                # self.armMotor2.set(.1)
            # elif self.armEncoder.get() >= self.armHeightLowG:
                # self.armMotor1.set(0)
                # self.armMotor2.set(0)
                # if self.wristEncoder.get() <= 14300: #bring the hand up 
                    # self.wristMotor.set(.1)
                # elif self.wristEncoder.get() >= 14200:
                    # self.wristMotor.set(0.09)
                    # if self.armEncoder.get() >= self.armHeightHighS: #lower the arm to 1st position
                        # self.armMotor1.set(-.1)
                        # self.armMotor2.set(-.1)
                    # elif self.armEncoder.get() <= self.armHeightHighS:
                        # self.position = 'First'
                        # self.setPoint = self.armEncoder.get()
                        # self.armMotor1.set(0)
                        # self.armMotor2.set(0)
                        # self.driving = False

            # #if the height is higher than first position
            # elif self.armEncoder.get() >= 13000:
                # self.armMotor1.set(-.1)
                # self.armMotor2.set(-.1)
            # elif self.armEncoder.get() <= 13000:
                # self.position = 'First'
                # self.setPoint = self.armEncoder.get()
                # self.armMotor1.set(0)
                # self.armMotor2.set(0)
                # self.driving = False

        # # if self.driving == False and self.position == 'First':
            # # self.error = self.setPoint - self.armEncoder.get()
            # # self.speed = self.error * .005 #.005 is the z. If the hand/arm is moving more up and down then lower the Z
            # # #If it is still dropping then increase z
            # # #Eqaution: speed = error * z
            # # self.armMotor1(self.speed)
            # # self.armMotor2(self.speed)
            
        #Flywheel motors for ball intake/outtake
        if robot.stick2.getRawButton(1):
            self.rightFly.set(self.ballIntakeSpeed)
            self.leftFly.set(-self.ballIntakeSpeed)
        elif robot.stick1.getRawButton(1):
            self.rightFly.set(self.ballSpitSpeed)
            self.leftFly.set(-self.ballSpitSpeed)
        else:
            self.rightFly.set(0)
            self.leftFly.set(0)


