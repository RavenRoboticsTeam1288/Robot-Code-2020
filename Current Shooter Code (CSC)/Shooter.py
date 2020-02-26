import wpilib
import utilities
import ctre

class ShooterController():
    def __init__(self, robot):
        #Motor Setup
        self.RakeMotor = wpilib.Victor(6)
        self.PivotMotor = wpilib.Victor(5)
        self.ConveyorMotor1 = ctre.WPI_VictorSPX(4)
        self.ConveyorMotor2 = ctre.WPI_VictorSPX(3)
        self.Flywheel = ctre.WPI_VictorSPX(2)
        self.TimedMotor = ctre.WPI_VictorSPX(1)
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
        self.Conveyor1Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)
        self.Conveyor2Encoder = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k1X)
        self.FlywheelEncoder = wpilib.Encoder(10, 11, False, wpilib.Encoder.EncodingType.k1X)

        #Misc Setup:
        self.IndexSensor = wpilib.DigitalInput(5) #not the real port
        self.BumpSwitch = wpilib.DigitalInput(1) #not the real port
        self.RakeRelease1 = wpilib.DigitalOutput(0) #not the real port
        self.RakeRelease2 = wpilib.DigitalOutput(3) #not the real port
        self.RakeDropping = True
        self.AutoShoot = False
        self.AutoShootLow = False
        self.TimerBegin = False
        self.TimerRunning = False
        self.IndexRunning = False
        self.WaitTime = .5
        self.ConveyorIndex = 1536 #1.5 rotations * 1024 encoder counts, Placeholder

    #---------------------------------------------------------------------------
    def autonomousInit(self, robot):
        self.RakeRelease1.set(True)
        self.RakeRelease2.set(True)
        #self.PrintTimer.start()

    #---------------------------------------------------------------------------
    def autonomousPeriodic(self, robot):
        self.RakeTimer.start()
        if self.RakeTimer.get() > 3:
            self.RakeRelease1.set(False)
            self.RakeRelease2.set(False)
            self.RakeTimer.stop()
            self.RakeTimer.reset()
            self.RakeDropping = False
            '''self.PrintTimer.stop()
        if self.PrintTimer.hasPeriodPassed(1) and self.RakeDropping == True:
            print(int(self.RakeTimer.get()))'''



    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        
    def teleopPeriodic(self, robot):
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
        #if self.IndexSensor.get():
        if robot.gamepad.getRawButton(1): #Replace with above sensor
            self.IndexTimer.start()
            self.IndexRunning = True

        if self.IndexRunning:
            utilities.utilities.BallIndex(self)
        
        #-----------------------------------------------------------------------
        #Test Stuff

        #Solenoid Activation
        if robot.gamepad.getRawButton(2):
            self.RakeRelease1.set(True)
            self.RakeRelease2.set(True)

        
        #Encoder Button
        '''if robot.stick1.getRawButton(2):
            self.EncoderBegin = True
        if EncoderBegin == True:
            self.Encoder.'''

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
