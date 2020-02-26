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

    def AutoShoot(robot):
        robot.Flywheel.set(.5)
        if robot.ShootTimer.get() < robot.WaitTime:
            robot.ConveyorMotor1.set(.1)
            robot.ConveyorMotor2.set(.1)
        elif robot.ShootTimer.get() < robot.WaitTime + .5:
            robot.ConveyorMotor1.set(0)
            robot.ConveyorMotor2.set(0)
        else:
            robot.WaitTime += 1
            
        if robot.ShootTimer.get() > 5:
            robot.Flywheel.set(0)
            robot.ConveyorMotor1.set(0)
            robot.ConveyorMotor2.set(0)
            robot.ShootTimer.stop()
            robot.ShootTimer.reset()
            robot.AutoShoot = False
            robot.WaitTime = .5

        if robot.PrintTimer.hasPeriodPassed(1):
            print(int(robot.ShootTimer.get()))

    def AutoShootLow(robot):
        robot.Flywheel.set(.2)
        if robot.ShootTimer.get() < robot.WaitTime:
            robot.ConveyorMotor1.set(.1)
            robot.ConveyorMotor2.set(.1)
        elif robot.ShootTimer.get() < robot.WaitTime + .5:
            robot.ConveyorMotor1.set(0)
            robot.ConveyorMotor2.set(0)
        else:
            robot.WaitTime += 1
            
        if robot.ShootTimer.get() > 5:
            robot.Flywheel.set(0)
            robot.ConveyorMotor1.set(0)
            robot.ConveyorMotor2.set(0)
            robot.ShootTimer.stop()
            robot.ShootTimer.reset()
            robot.AutoShootLow = False
            robot.WaitTime = .5

        if robot.PrintTimer.hasPeriodPassed(1):
            print(int(robot.ShootTimer.get()))


    def BallIndex(robot):
        robot.ConveyorMotor1.set(.1)
        robot.ConveyorMotor2.set(.1)
        if robot.Conveyor1Encoder.get() >= robot.ConveyorIndex and robot.Conveyor2Encoder.get() >= robot.ConveyorIndex:
            robot.ConveyorMotor1.set(0)
            robot.ConveyorMotor2.set(0)
            robot.IndexTimer.stop()
            robot.IndexTimer.reset()
            robot.IndexRunning = False
            print("Ball Indexed")

        if robot.PrintTimer.hasPeriodPassed(1):
            print(int(robot.IndexTimer.get()))
            
    #Auto Functions
    def DriveNumSecs(robot, direction, speed1, num):
        if robot.AutoTimer.get() < 3:
            robot.rightFrontMotor.set(speed1)
        else:
            robot.rightFrontMotor.set(0)
            robot.AutoTimer.stop()
            robot.AutoTimer.reset()
            robot.State = 2


    #trevor's first gyro code:
    '''run gyro.com
    enter
    return True
if gyro = false:
    dont' run gyro(self) init'''
