#n is a placeholder
import wpilib
import ctre

class ShooterController():

    def __init__(self, robot):
        #Physical Stuff Setup
        '''self.Ultrasonic = wpilib.Ultrasonic(7, 8)
        self.RakeMotor = wpilib.Victor(6)
        self.PivotMotor = wpilib.Victor(5)
        self.ConveyorMotor1 = wpilib.Victor(4)
        self.ConveyorMotor2 = wpilib.Victor(3)
        self.FlyWheelMotor = wpilib.Victor(2)'''
        #self.TimedMotor = wpilib.Victor(1)
        self.RakeWheel = wpilib.talon(1)
        self.TimedMotor = ctre.WPI_VictorSPX(1)
        self.Timer = wpilib.Timer()
        self.PrintTimer = wpilib.Timer()
        #self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)
        
        #Misc Variable Setup:
        self.TimerBegin = False
        self.TimerRunning = False            
      

    def teleopPeriodic(self, robot):
        #Timed Button
        if robot.stick1.getRawButton(10) == 1:
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

        #Rake Wheel
        if robot.stick1.getRawButton(3)
            self.RakeWheel.set(.2)
        if robot.stick1.getRawButton(4)
            self.RakeWheel.set(0)
        else:
            self.RakeWheel.set(0)
                
        #Encoder Button
        if robot.stick1.getRawButton(9) == 1:
            self.EncoderRunning = True
            self.TimedMotor.set(.01)
        if self.EncoderRunning == True:
            if self.Encoder.get() >= 5*1024:
                self.TimedMotor.set(0)
                self.EncoderRunning = False


        #Ultrasonic
wpilib        if robot.stick1.getRawButton(3) == 1:
            Ultrasonic.ping()
            print(pidGet())