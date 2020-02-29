import wpilib
import utilities
import ctre

class ShooterController():
    def __init__(self, robot):
        #Motor Setup
        self.RakeMotor = ctre.WPI_TalonSRX(6)
        self.PivotMotor = ctre.WPI_TalonSRX(5)
        self.ConveyorMotor1 = ctre.WPI_TalonSRX(4)
        self.ConveyorMotor2 = ctre.WPI_TalonSRX(3)
        self.Flywheel = ctre.WPI_TalonSRX(2)
        self.TimedMotor = ctre.WPI_TalonSRX(1)
        '''self.ConveyorMotor1 = wpilib.Victor(4) #not the real port
        self.ConveyorMotor2 = wpilib.Victor(3) #not the real port
        self.Flywheel = wpilib.Victor(2) #not the real port
        #self.TimedMotor = wpilib.Victor(1) #not the real port
        self.RakeMotor = wpilib.Victor(5) #not the real port'''

        #Timer Setup
        self.ShootTimer = wpilib.Timer()
        self.PrintTimer = wpilib.Timer()
        self.PrintTimer.start()
        self.RakeTimer = wpilib.Timer()
        self.IndexTimer = wpilib.Timer()

        #Encoder Setup 
        #Fix these
        #self.Conveyor1Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)
        #self.Conveyor2Encoder = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X)
        #self.FlywheelEncoder = wpilib.Encoder(10, 11, False, wpilib.Encoder.EncodingType.k1X)
		self.ConveyorMotor1.get

        #Misc Setup:
        self.IndexSensor1 = wpilib.DigitalInput(5) #not the real port
        self.IndexSensor2 = wpilib.DigitalInput(6) #not the real port
        self.IndexSensor3 = wpilib.DigitalInput(7) #not the real port
        self.BumpSwitch = wpilib.DigitalInput(1) #not the real port
        self.RakeRelease1 = wpilib.PWM(0) #not the real port
        self.RakeRelease2 = wpilib.PWM(3) #not the real port
        self.RakeDropping = True
        self.AutoShoot = False
        self.AutoShootLow = False
        self.TimerBegin = False
        self.TimerRunning = False
        self.IndexRunning = False
        self.WaitTime = .5
        self.ConveyorIndex = 1536 #1.5 rotations * 1024 encoder counts, Placeholder
        
    #---------------------------------------------------------------------------------
    
        #PID loop for velocity
        #keeps the flywheel going at a constant RPM at all times 
        #Corrects for errors
        self.Flywheel.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder,0,0)
        self.Flywheel.config_kF(0, 0.01, 0)
        self.Flywheel.config_kP(0, 0.01, 0)
        self.Flywheel.config_kI(0, 0.00001, 0)
        self.Flywheel.config_kD(0, 0.0, 0)
        self.fleshWound = wpilib.Timer()
        self.fleshWound.start()
        self.Errorzone = 0
        

    #---------------------------------------------------------------------------
    def autonomousInit(self, robot):
        self.RakeRelease1.setPosition(1)
        self.RakeRelease2.setPosition(1)
        #self.PrintTimer.start()

    #---------------------------------------------------------------------------
    def autonomousPeriodic(self, robot):
        pass
        #Just in case servos need 
        '''self.RakeTimer.start()
        if self.RakeTimer.get() > 3:
            self.RakeRelease1.setPosition(0)
            self.RakeRelease2.setPosition(0)
            self.RakeTimer.stop()
            self.RakeTimer.reset()
            self.RakeDropping = False
            self.PrintTimer.stop()
        if self.PrintTimer.hasPeriodPassed(1) and self.RakeDropping == True:
            print(int(self.RakeTimer.get()))'''



    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        
    def teleopPeriodic(self, robot):
        
        #keeping the fly wheel at a set speed
        if self.fleshwound.hasPeriodPassed(.1):
            vel = (self.Flywheel.getSelectedSensorPosition(0) - self.Errorzone) * 10
            self.Errorzone = self.Flywheel.getSelectedSensorPosition(0)
            self.fleshwound.reset()
            self.fleshwound.start()
        
        #Manual Shooting and Ball Pickup
        if robot.gamepad.getRawButton(7):
            self.Flywheel.set(.5)
        elif self.AutoShoot == False and self.AutoShootLow == False:
            self.Flywheel.set(0)

        if robot.gamepad.getRawButton(8):
            self.ConveyorMotor1.set(.1)
            self.ConveyorMotor2.set(.1)
        elif robot.gamepad.getRawButton(3):
            self.ConveyorMotor1.set(.1)
            self.RakeMotor.set(.1)
        elif self.AutoShoot == False and self.AutoShootLow == False:
            self.ConveyorMotor1.set(0)
            self.ConveyorMotor2.set(0)
            self.RakeMotor.set(0)


        #Auto-Shoot
        if robot.gamepad.getRawButton(9):
            self.AutoShoot = True
            self.ShootTimer.start()

        if self.AutoShoot == True:
            utilities.utilities.AutoShoot(self)


        if robot.gamepad.getRawButton(11):
            self.AutoShootLow = True
            self.ShootTimer.start()

        if self.AutoShootLow:
            utilities.utilities.AutoShootLow(self)

        #Ball Index System
        #if robot.gamepad.getRawButton(1):
        if self.IndexSensor1.get() and not self.IndexController3:
            self.IndexTimer.start()
            self.IndexRunning = True

        if self.IndexRunning:
            utilities.utilities.BallIndex(self)
           
        
	def AutoShoot(robot):
       	    robot.Flywheel.set(ctre.ControlMode.Velocity, 10240)
            if robot.ShootTimer.get() < robot.WaitTime:
                robot.ConveyorMotor1.set(.1)
                robot.ConveyorMotor2.set(.1)
            elif robot.ShootTimer.get() < robot.WaitTime + .5:
                robot.ConveyorMotor1.set(0)
                robot.ConveyorMotor2.set(0)
            else:
                robot.WaitTime += 1
            
            if robot.ShootTimer.get() > 5:
                robot.Flywheel.set(ctre.ControlMode.Velocity, 0)
                robot.ConveyorMotor1.set(0)
                robot.ConveyorMotor2.set(0)
                robot.ShootTimer.stop()
                robot.ShootTimer.reset()
                robot.AutoShoot = False
                robot.WaitTime = .5

            if robot.PrintTimer.hasPeriodPassed(1):
                print(int(robot.ShootTimer.get()))
			
	def AutoShootLow(robot):
            robot.Flywheel.set(ctre.ControlMode.Velocity, 5240)
            if robot.ShootTimer.get() < robot.WaitTime:
                robot.ConveyorMotor1.set(.1)
                robot.ConveyorMotor2.set(.1)
            elif robot.ShootTimer.get() < robot.WaitTime + .5:
                robot.ConveyorMotor1.set(0)
                robot.ConveyorMotor2.set(0)
            else:
                robot.WaitTime += 1
                
            if robot.ShootTimer.get() > 5:
                robot.Flywheel.set(ctre.ControlMode.Velocity, 0)
                robot.ConveyorMotor1.set(0)
                robot.ConveyorMotor2.set(0)
                robot.ShootTimer.stop()
                robot.ShootTimer.reset()
                robot.AutoShootLow = False
                robot.WaitTime = .5
    
            if robot.PrintTimer.hasPeriodPassed(1):
                print(int(robot.ShootTimer.get()))
        #-----------------------------------------------------------------------
        #Test Stuff
        
        '''
        #Solenoid Activation
        if robot.gamepad.getRawButton(2):
            self.RakeRelease1.set(True)
            self.RakeRelease2.set(True)

        
  

        #Ultrasonic
        if robot.stick1.getRawButton(3):
            Ultrasonic.ping()
            print(pidGet())

        #Timed Button
        if robot.stick1.getRawButton(10):
            self.TimerBegin = True
        
        if self.TimerBegin:
            if self.TimerRunning == False:
                self.Timer.start()
                self.PrintTimer.start()
                self.TimedMotor.set(.1)
            if self.Timer.get() < 5:
                self.TimerRunning = True
                if self.PrintTimer.hasPeriodPassed(1):
                    print(int(self.Timer.get()))
                
            else:
                print(int(self.Timer.get()))
                self.TimedMotor.set(0)
                self.Timer.reset()
                self.TimerBegin = False
                self.TimerRunning = False
         '''
