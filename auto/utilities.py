import wpilib
from wpilib import Encoder
from wpilib import Ultrasonic
import ctre
import wpilib

class utilities():
    def driveNumInches(robot, direction, speed1, num):
        print("Got to DNI")
        ticksNeeded = num * (100/2.67)
        if robot.encoderLeft.get() < ticksNeeded:
            #robot.left.set(speed1)
            robot.drivetrainController.frontLeft.set(speed1)
            robot.drivetrainController.rearLeft.set(speed1)
        else:
            #robot.left.set(0)
            robot.drivetrainController.frontLeft.set(0)
            robot.drivetrainController.rearLeft.set(0)
            robot.drivetrainController.encoderLeft.reset()
        if robot.encoderRight.get() < ticksNeeded:
            #robot.right.set(speed1)
            robot.drivetrainController.frontRight.set(speed1)
            robot.drivetrainController.rearRight.set(speed1)
        else:
            #robot.right.set(0)
            robot.drivetrainController.frontRight.set(0)
            robot.drivetrainController.rearRight.set(0)
            robot.drivetrainController.encoderRight.reset()
        if robot.encoderRight.get() >= ticksNeeded and encoder.Left.get() >= ticksNeeded:
            return True

    def ultrasonicAim(robot, distFt):
        distGoalLow = distFt * 12
        distGoalLow += -2
        distGoalHigh = distFt * 12
        distGoalHigh += 2
        value = getVoltage() * 4.8
        if value > distGoalHigh:
            #robot.left.set(.1)
            #robot.right.set(.1)
            robot.drivetrainController.frontLeft.set(.1)
            robot.drivetrainController.frontRight.set(.1)
            robot.drivetrainController.rearLeft.set(.1)
            robot.drivetrainController.rearRight.set(.1)
        elif value < distGoalLow:
            #robot.right.set(-.1)
            #robot.left.set(-.1)
            robot.drivetrainController.frontLeft.set(-.1)
            robot.drivetrainController.frontRight.set(-.1)
            robot.drivetrainController.rearLeft.set(-.1)
            robot.drivetrainController.rearRight.set(-.1)
        else:
            #robot.right.set(0)
            #robot.left.set(0)
            robot.drivetrainController.frontLeft.set(0)
            robot.drivetrainController.frontRight.set(0)
            robot.drivetrainController.rearLeft.set(0)
            robot.drivetrainController.rearRight.set(0)
            return True

    def turnNumDegrees(robot, num, speed):
        angle = robot.gyro.getAngle()
        angle = angle % 360.0
        if angle < 0.0:
            angle = angle + 360.0
        print(angle)

        goalMin = num - .5
        goalMax = num + .5


        if angle > goalMax:
            #robot.right.set(0)
            #robot.left.set(direction * speed)
            robot.drivetrainController.frontLeft.set(-1 * speed)
            robot.drivetrainController.frontRight.set(-1 * speed)
            robot.drivetrainController.rearLeft.set(-1 * speed)
            robot.drivetrainController.rearRight.set(-1 * speed)

        elif angle < goalMin:
            #robot.right.set(direction * speed)
            #robot.left.set(0)
            robot.drivetrainController.frontLeft.set(1 * speed)
            robot.drivetrainController.frontRight.set(1 * speed)
            robot.drivetrainController.rearLeft.set(1 * speed)
            robot.drivetrainController.rearRight.set(1 * speed)

        else:
            #robot.right.set(0)
            #robot.left.set(0)
            robot.drivetrainController.frontLeft.set(0)
            robot.drivetrainController.frontRight.set(0)
            robot.drivetrainController.rearLeft.set(0)
            robot.drivetrainController.rearRight.set(0)
            return True

    #trevor's first gyro code:
    '''run gyro.com
    enter
    return True
if gyro = false:
    dont' run gyro(self) init'''
