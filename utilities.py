import wpilib
from wpilib import Encoder
from wpilib import Ultrasonic
import ctre
import wpilib

class utilities():
    def driveNumInches(robot, direction, speed1, num):
        print("Got to DNI")
        ticksNeeded = num * (100/2.67)
        if robot.drivetrainController.frontLeft.getSelectedSensorPosition(0) < ticksNeeded:
            robot.drivetrainController.left.set(speed1)
            #robot.drivetrainController.frontLeft.set(speed1)
            #robot.drivetrainController.rearLeft.set(speed1)
        else:
            robot.drivetrainController.left.set(0)
            #robot.drivetrainController.frontLeft.set(0)
            #robot.drivetrainController.rearLeft.set(0)
            #robot.drivetrainController.encoderLeft.reset()
        if robot.drivetrainController.frontRight.getSelectedSensorPosition(0) < ticksNeeded:
            robot.drivetrainController.right.set(speed1)
            #robot.drivetrainController.frontRight.set(speed1)
            #robot.drivetrainController.rearRight.set(speed1)
        else:
            #robot.right.set(0)
            #robot.drivetrainController.frontRight.set(0)
            #robot.drivetrainController.rearRight.set(0)
            robot.drivetrainController.right.set(0)
            robot.drivetrainController.left.set(0)
            #robot.drivetrainController.encoderRight.reset()
        if robot.drivetrainController.frontLeft.getSelectedSensorPosition(0) >= ticksNeeded and robot.drivetrainController.frontRight.getSelectedSensorPosition(0) >= ticksNeeded:
            return True
        
    def BallIndex(robot):
        if Shooter.IndexSensor3:
            pass
        else:
            robot.ConveyorMotor1.set(.1)
            robot.ConveyorMotor2.set(.1)
            if Shooter.IndexSensor2:
                if Shooter.IndexTimer > .25:
                    pass
                else:
                    if Shooter.IndexSensor2:
                        robot.ConveyorMotor1.set(0)
                        robot.ConveyorMotor2.set(0)
                        robot.IndexTimer.stop()
                        robot.IndexTimer.reset()
                        robot.IndexRunning = False
                        print("Ball Indexed")

                    if robot.PrintTimer.hasPeriodPassed(1):
                        print(int(robot.IndexTimer.get()))
            
    def ultrasonicAim(robot, distFt):
        print("ultrasonicAim")
        distGoalLow = distFt * 12.0 - 1.0
        distGoalHigh = distFt * 12.0 + 1.0
        value = robot.ultrasonic.getVoltage() * 4.8
        if value > distGoalHigh:
            robot.drivetrainController.left.set(.1)
            #robot.drivetrainController.frontLeft.set(.1)
            #robot.drivetrainController.frontRight.set(.1)
            #robot.drivetrainController.rearLeft.set(.1)
            #robot.drivetrainController.rearRight.set(.1)
        elif value < distGoalLow:
            robot.drivetrainController.right.set(.1)
            #robot.drivetrainController.frontLeft.set(-.1)
            #robot.drivetrainController.frontRight.set(-.1)
            #robot.drivetrainController.rearLeft.set(-.1)
            #robot.drivetrainController.rearRight.set(-.1)
        else:
            robot.drivetrainController.left.set(0)
            robot.drivetrainController.right.set(0)
            #robot.drivetrainController.frontLeft.set(0)
            #robot.drivetrainController.frontRight.set(0)
            #robot.drivetrainController.rearLeft.set(0)
            #robot.drivetrainController.rearRight.set(0)
            return True
        

    def turnNumDegrees(robot, num):
        print("turnNumDegrees")
        #currentPos = robot.gyro.getAngle()
        numMin = num - .1
        numMax = num + .1
        angle = robot.gyro.getAngle()
        if angle < 0:
            angles + 360
        
        if angle > 360:
            angle - 360
            
        value = abs(angle - num)
        print(angle)

        if angle < numMin or angle > numMax:
            #if value >= 180: #turn left
            if ((value < 0 and abs(value) > 180) or (value > 0 and abs(value) < 180)): #TURN LEFT
                robot.drivetrainController.right.set(0)
                robot.drivetrainController.left.set(.1)
                #robot.drivetrainController.frontLeft.set(-1 * speed)
                #robot.drivetrainController.frontRight.set(-1 * speed)
                #robot.drivetrainController.rearLeft.set(-1 * speed)
                #robot.drivetrainController.rearRight.set(-1 * speed)

            #if value <= 180: #turn right
            elif ((value <= 0 and abs(value) <= 180) or (value >= 0 and abs(value) >= 180)): #TURN RIGHT    
                robot.drivetrainController.right.set(.1)
                robot.drivetrainController.left.set(0)
                #robot.drivetrainController.frontLeft.set(1 * speed)
                #robot.drivetrainController.frontRight.set(1 * speed)
                #robot.drivetrainController.rearLeft.set(1 * speed)
                #robot.drivetrainController.rearRight.set(1 * speed)
        
        else:
            robot.drivetrainController.right.set(0)
            robot.drivetrainController.left.set(0)
            #robot.drivetrainController.frontLeft.set(0)
            #robot.drivetrainController.frontRight.set(0)
            #robot.drivetrainController.rearLeft.set(0)
            #robot.drivetrainController.rearRight.set(0)
            return True

    def ControlPanelDriving(robot):
        #while button held, this runs- ultrasonic check and then encoder driving. use DriveNumInches? slow speed.
        print("dunno problem")
        if robot.AutoTimer.hasPeriodPassed(.1):
            print("got here.")
            value = robot.ultrasonic.getVoltage() * 4.8
            if value >= 2:
                robot.DrivetrainController.left.set(.01)
                robot.DrivetrainController.right.set(.01)
            else:
                robot.drivetrainController.left.set(0)
                robot.drivetrainController.right.set(0)
            
    #Auto Functions
    def robocheckFeet(robot, distance):
        print("robocheckFeet")
        value = robot.ultrasonic.getVoltage() * 4.8
        value /= 12
        if value > distance:
            robot.moveSafe = "safe"
        elif value <= distance:
            robot.moveSafe = "not safe"
            
    #trevor's first gyro code:
    '''run gyro.com
    enter
    return True
if gyro = false:
    dont' run gyro(self) init'''
