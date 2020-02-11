import wpilib 
#import ctre
'''from networktables import NetworkTablesInstance
from .tab import ShuffleboardTab
from .instance import ShuffleboardInstance
from .recordingcontroller import RecordingController
from .eventimportance import EventImportance'''


from rev.color import ColorSensorV3
#color sensor instalation (py -3 -m pip install -U robotpy-rev-color)

class ClimberController():

    def __init__(self):

        '''self.Winch = ctre.WPI_VictorSPX(1)
        self.Scissor = ctre.WPI_VictorSPX(2)
        self.coFlyWheel = ctre.WPI_VictorSPX(3)
        self.stickLift = ctre.WPI_VictorSPX(4)'''
        self.Winch = wpilib.Victor(1)
        self.Scissor = wpilib.Victor(2)
        self.coFlyWheel = wpilib.Victor(3)
        self.stickLift = wpilib.Victor(4)
        self.scissorExtendSpeed = .1
        self.scissorRetractSpeed = -.1
        self.winchRetractSpeed = -.1
        self.CoSpeed = .1
        rotations = 0

        self.Encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k1X)
  
        self.timer = wpilib.Timer()
        #self.motor1 = ctre.WPI_VictorSPX(3)
        self.motor1 = wpilib.Victor(3)

    def teleopPeriodic(self, robot):
        if robot.stick1.getRawButton(6):
            self.Scissor.set(self.scissorExtendSpeed)
        elif robot.stick1.getRawButton(7):
            self.Scissor.set(self.scissorRetractSpeed)
        else:
            self.Scissor.set(0)
        if robot.stick1.getRawButton(3):
            self.Winch.set(self.winchRetractSpeed)
        else:
            self.Winch.set(0)
        if robot.stick1.getRawButton(2):
            self.stickLift.set(self.colorFlyWheelSpeed)
        else:
            self.stickLift.set(0)
#Timer
        if robot.stick1.getRawButton(8):
            self.timer.start()
            self.motor1.set(0.1)

        if self.timer.get() >= 5:
            self.timer.reset()
            self.timer.stop()
            self.motor1.set(0)
         
#shuffleboard
        #colorStr = self.colorSensor.getColor()    
        #wpilib.SmartDashboard.putString("color", colorStr) 

#Encoder
        if self.Encoder.get() < 3000:
            if robot.gamepad.getRawButton(2):
                self.Winch.set(.3)
            elif robot.gamepad.getRawButton(1):
                self.Winch.set(-.3)
            elif self.Encoder.get() > 3000:
                 self.Winch.set(0)
            else:
                 self.Winch.set(0)
                 
    class ColorSensor:
        def __init__(self):
            self.sensor = None
        def setSensor(self, sensor):
            self.sensor = sensor
        def getColor(self):
            assert self.sensor != None
            c = self.sensor.getColor()
            #return str(str(c.red) + "," + str(c.green) + "," + str(c.blue))
            out = ""
            maptable = {"red" : [0.564, 0.321, 0.115], "green" : [0.150, 0.600, 0.248], "blue" : [0.110, 0.422, 0.469], "yellow" : [0.324, 0.568, 0.108]}
            costs = dict()
            for name in maptable:
                test = maptable[name]
                cost = 0
                cost += (c.red - test[0])**2
                cost += (c.green - test[1])**2
                cost += (c.blue - test[2])**2
                costs[name] = cost
            min_cost = min(costs.values())
            results = [a for a in costs if costs[a] == min_cost]
            return results[0]
