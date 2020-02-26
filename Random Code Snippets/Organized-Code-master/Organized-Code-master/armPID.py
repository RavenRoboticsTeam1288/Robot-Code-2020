import wpilib

class armPIDController():
    
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
		
        #PID Setup
        self.maxArmPosition = 35000 #Just a guess
        self.maxWristPosition = 12000 #Just a guess, will fine tune
        self.tolerancePercent = 5.0 #another guess
        
        self.shoulderPIDLoop = wpilib.PIDController(1, 0, 0, 0, self.shoulderEncoder, self.shoulderMotor1, .05)
        self.wristPIDLoop = wpilib.PIDController(1, 0, 0, 0, self.wristEncoder, self.wristMotor, .05)
        self.wristPIDLoop.setInputRange(0, self.maxWristPosition)
        self.shoulderPIDLoop.setInputRange(0, self.maxArmPosition)
        self.wristPIDLoop.setOutputRange(-.5, .5) #Ranges can be changed if needed
        self.shoulderPIDLoop.setOutputRange(-.5, .5)
        
        self.shoulderPIDLoop.setSetpoint(self.shoulderEncoder.get())
        self.wristPIDLoop.setSetpoint(self.wristEncoder.get())
        
        self.shoulderPIDLoop.setPercentTolerance(self.tolerancePercent)
        self.wristPIDLoop.setPercentTolerance(self.tolerancePercent) 
        
        # May be redundant
        # self.shoulderPIDLoop.disable()
        # self.wristPIDLoop.disable()

        #Misc Variables Setup
        #Most values are placeholds
        self.ballIntakeSpeed = 0.1
        self.ballSpitSpeed = -0.1
        self.shoulderSpeedUp = 0.2
        self.shoulderSpeedDown = -0.1
        self.wristSpeedUp = 0.2
        self.wristSpeedDown = -0.1
        self.armHeight1 = 14550
        self.armHeight2 = 23750
        self.armHeight3 = 32700
        self.armHeightG = 1850 #Ground
        self.armHeightT = 10050 #Transition
        self.armHeightH = 0 #Home
        self.wristHeight1 = 7050
        self.wristHeight2 = 5050
        self.wristHeight3 = 8050
        self.wristHeightG = 9050 #Ground
        self.wristHeightT = 3050 #Transition
        self.wristHeightH = 0 #Home
        
        #The setpoint for the shoulder/wrist
        self.shoulderSetpoint = 0
        self.wristSetpoint = 0

        #When the shoulder/wrist isn't being conroller manually then the value is False,
        #but when the robot is driving then the value is True
        self.shoulderIsDriving = False
        self.wristIsDriving = False

    
    def teleopPeriodic(self, robot):

        #Print the encoder values to the console
        if robot.stick1.getRawButton(4):
            print(self.shoulderEncoder.get())
            print(self.wristEncoder.get())

        #Test for manual up/down control of the arm's shoulder
        if robot.gamepad.getRawButton(5): #Up
            self.shoulderIsDriving = True
            self.shoulderPIDLoop.disable()
            self.shoulderMotor1.set(self.shoulderSpeedUp)
            self.shoulderMotor2.set(self.shoulderSpeedUp)
            self.shoulderPIDLoop.setSetpoint(self.shoulderEncoder.get())
        elif robot.gamepad.getRawButton(6): #Down
            self.shoulderIsDriving = True
            self.shoulderPIDLoop.disable()
            self.shoulderMotor1.set(self.shoulderSpeedDown)
            self.shoulderMotor2.set(self.shoulderSpeedDown)
            self.shoulderPIDLoop.setSetpoint(self.shoulderEncoder.get())
        else: #Stop
            self.shoulderPIDLoop.enable()
            self.shoulderIsDriving = False
            
        #Test for manual up/down control of the arm's wrist
        if robot.gamepad.getRawButton(7):
            self.wristIsDriving = True
            self.wristPIDLoop.disable()
            self.wristMotor.set(wristSpeedUp)
            self.wristPIDLoop.setSetpoint(self.wristEncoder.get())
        elif robot.gamepad.getRawButton(8):
            self.wristIsDriving = True
            self.wristPIDLoop.disable()
            self.wristMotor.set(wristSpeedDown)
            self.wristPIDLoop.setSetpoint(self.wristEncoder.get())
        else: #Stop
            self.wristPIDLoop.enable()
            self.wristIsDriving = False

        #Shoulder and Wrist Semi-automatic position control
        #All values are placeholds
        if self.wristIsDriving == False and self.shoulderIsDriving == False:
            if robot.gamepad.getRawButton(1): 
                self.shoulderPIDLoop.setSetpoint(self.armHeightT)
                self.wristPIDLoop.setSetpoint(self.wristHeightT)
            
            if robot.gamepad.getRawButton(2): 
                self.shoulderPIDLoop.setSetpoint(self.armHeightG)
                self.wristPIDLoop.setSetpoint(self.wristHeightG)
                
            if robot.gamepad.getRawButton(3): 
                self.shoulderPIDLoop.setSetpoint(self.armHeight1)
                self.wristPIDLoop.setSetpoint(self.wristHeight1)
                
            if robot.gamepad.getRawButton(4): 
                self.shoulderPIDLoop.setSetpoint(self.armHeight2)
                self.wristPIDLoop.setSetpoint(self.wristHeight3)
                
            if robot.gamepad.getRawButton(5): 
                self.shoulderPIDLoop.setSetpoint(self.armHeight3)
                self.wristPIDLoop.setSetpoint(self.wristHeight3)
                
            if robot.gamepad.getRawButton(6): 
                self.shoulderPIDLoop.setSetpoint(self.armHeightH)
                self.wristPIDLoop.setSetpoint(self.wristHeightH)
            
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