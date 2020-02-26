# numbers subject to change
import wpilib
import ctre

#from rev.color import ColorSensorV3
#import ColorSensor
#color sensor instalation (py -3 -m pip install -U robotpy-rev-color)

class ClimberController():

    def __init__(self):

        self.Winch = ctre.WPI_VictorSPX(1)
        self.Scissor = ctre.WPI_TalonSRX(3)
        self.Scissor.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder,0,0)
        self.Scissor.config_kP(0, 0.005, 0)
        self.Scissor.config_kI(0, 0.0000001, 0)
        self.Scissor.config_kD(0, 0.0, 0)
        self.coFlyWheel = ctre.WPI_VictorSPX(2)
        self.stickLift = ctre.WPI_VictorSPX(4)
        '''self.Winch = wpilib.Victor(1)
        self.Scissor = ctre.WPI_TalonSRX(3)
        self.coFlyWheel = wpilib.Victor(3)
        self.stickLift = wpilib.Victor(4)'''
        self.scissorExtendSpeed = .6
        self.scissorRetractSpeed = -.6
        self.winchRetractSpeed = -.1
        self.CoSpeed = .1
        self.targetB = [(0,255,255) ,(0,206,209)]
        self.targetY = [(255,255,0) ,(184,134,11)]
        self.targetG = [(60,179,113) ,(0,100,0)]
        self.targetR = [(255,0,0) ,(178,34,34)]
        rotations = 0

        self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)

        self.timer = wpilib.Timer()
        self.Scissor.setQuadraturePosition(0)
        '''self.motor1 = ctre.WPI_VictorSPX(3)'''
        self.motor1 = wpilib.Victor(3)
        #self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        #self.colorSensor = ColorSensor.ColorSensor()
        #self.colorSensor.setSensor(ColorSensorV3(wpilib.I2C.Port.kOnboard))

    def teleopPeriodic(self, robot):
        if robot.gamepad.getRawButton(5) and self.Scissor.getSelectedSensorPosition(0) < 2717000:
            print("work")
            #self.Scissor.set(self.scissorExtendSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 2517000)
        elif robot.gamepad.getRawButton(6) and self.Scissor.getSelectedSensorPosition(0) > 0:
            #self.Scissor.set(self.scissorRetractSpeed)
            self.Scissor.set(ctre.ControlMode.Position, 0)
        else:
            self.Scissor.set(0)
            print(self.Scissor.getSelectedSensorPosition(0))
        if robot.stick1.getRawButton(3):
            self.Winch.set(self.winchRetractSpeed)
        else:
            self.Winch.set(0)
        if robot.stick1.getRawButton(2):
            self.stickLift.set(self.colorFlyWheelSpeed)
        else:
            self.stickLift.set(0)

#Color sensor V3
        print(self.colorSensor.getColor())
        colorStr = self.colorSensor.getColor()
        proximity = self.colorSensor.sensor.getProximity()

        wpilib.SmartDashboard.putNumber("proximity", proximity)
        wpilib.SmartDashboard.putString("Color", colorStr)

