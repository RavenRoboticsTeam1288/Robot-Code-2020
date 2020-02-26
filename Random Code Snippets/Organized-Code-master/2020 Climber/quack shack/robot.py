import wpilib
import ctre
from networktables import NetworkTables

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.rgb = (wpilib.PWM(0), wpilib.PWM(1), wpilib.PWM(2))
        self.sd = NetworkTables.getTable('SmartDashboard')
        self.motorthing = ctre.TalonSRX(4)
        self.motorthing.config_kF(0, 0.0, 0)
        self.motorthing.config_kP(0, 0.4, 0)
        self.motorthing.config_kI(0, 0.0, 0)
        self.motorthing.config_kD(0, 0.0, 0)
        
        #Joystick/gamepad setup
        self.stick1 = wpilib.Joystick(1) #Right
        self.stick2 = wpilib.Joystick(2) #Left
        self.gamepad = wpilib.Joystick(3) #Operator Controller

		#Drivetrain Controller Setup, create the drive control object for the robot 

        #Arm Controller Setup, create the arm control object for the robot
        #self.armController = ArmController() 


        #Climber Controller Setup, create the climber control object for the robot
 
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        self.teleopPeriodic()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        print(self.motorthing.getSelectedSensorPosition(0))
        if self.gamepad.getRawButton(1):
            print("bruh momentum")
            self.motorthing.set(ctre.ControlMode.MotionMagic, 10240)
        if self.gamepad.getRawButton(2):
            self.motorthing.set(ctre.ControlMode.MotionMagic, 0)

            
if __name__ == '__main__':
    wpilib.run(MyRobot)
