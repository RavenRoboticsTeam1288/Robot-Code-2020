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
            robot.drivetrainController.frontLeft.set(-1 * speed1)
            robot.drivetrainController.rearLeft.set(-1 * speed1)
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
            return True

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
            return True

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

    def ultrasonicAim(robot, distFt):
        print("Got to Aim")
        distGoalLow = distFt * 12.0 - 2.0
        distGoalHigh = distFt * 12.0 + 2.0
        print("Dist Goals:")
        print(distGoalHigh)
        print(distGoalLow)
        value = robot.ultrasonic.getVoltage() * 4.8 * 12
        print(value)
        if value > distGoalHigh:
            #robot.left.set(.1)
            #robot.right.set(.1)
            robot.drivetrainController.frontLeft.set(-.2)
            robot.drivetrainController.frontRight.set(.2)
            robot.drivetrainController.rearLeft.set(-.2)
            robot.drivetrainController.rearRight.set(.2)
        elif value < distGoalLow:
            #robot.right.set(-.1)
            #robot.left.set(-.1)
            robot.drivetrainController.frontLeft.set(.2)
            robot.drivetrainController.frontRight.set(-.2)
            robot.drivetrainController.rearLeft.set(.2)
            robot.drivetrainController.rearRight.set(-.2)
        else:
            #robot.right.set(0)
            #robot.left.set(0)
            robot.drivetrainController.frontLeft.set(0)
            robot.drivetrainController.frontRight.set(0)
            robot.drivetrainController.rearLeft.set(0)
            robot.drivetrainController.rearRight.set(0)
            return True

    def turnNumDegrees(robot, num, speed):
        print("Got to TND")
        #currentPos = robot.gyro.getAngle()
        numMin = num - 10
        numMax = num + 10
        angle = robot.gyro.getAngle()
        if angle < 0:
            angle + 360

        if angle > 360:
            angle - 360

        value = abs(angle - num)
        print(angle)

        if angle < numMin or angle > numMax:
            if value >= 180: #turn left
            #if ((value < 0 and abs(value) > 180) or (value > 0 and abs(value) < 180)): #TURN LEFT
                #robot.right.set(0)
                #robot.left.set(direction * speed)
                robot.drivetrainController.frontLeft.set(-1 * speed)
                robot.drivetrainController.frontRight.set(-1 * speed)
                robot.drivetrainController.rearLeft.set(-1 * speed)
                robot.drivetrainController.rearRight.set(-1 * speed)

            if value < 180: #turn right
            #elif ((value <= 0 and abs(value) <= 180) or (value >= 0 and abs(value) >= 180)): #TURN RIGHT
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

    def robocheckFeet(robot, distance):
        print("Got to check")
        value = robot.ultrasonic.getVoltage() * 4.8
        value /= 12
        if value > distance:
            robot.moveSafe = True
        elif value <= distance:
            robot.moveSafe = False

    def portStart(robot):
        print("Port")
        if robot.autostate == 'start': #aim bot w/ ultrasonic
            done = utilities.ultrasonicAim(robot, 10)
            if done:
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            done = utilities.autoShootLow(robot)
            if done:
                robot.autostate = 'move'
        elif robot.autostate == 'move': #move back lil bizz
            #done = utilities.driveNumInches(robot, -1, .5, 48)
            if done:
                robot.autostate = 'done'
        elif robot.autostate == 'done': #cut everything to 0
            return True

    def offStart(robot):
        print("Got to OS")
        if robot.autostate == 'start': #move bot to wall spot
            done = utilities.ultrasonicAim(robot, 5)
            if done:
                robot.autostate = 'turn1'
        elif robot.autostate == 'turn1': #turn 90
            done = utilities.turnNumDegrees(robot, 90, .2)
            if done:
                robot.autostate = 'move'
        elif robot.autostate == 'move': #move bot to shooting locale
            done = utilities.ultrasonicAim(robot, 5.5)
            if done:
                robot.autostate = 'turn2'
        elif robot.autostate == 'turn2': #turn to see bot
            done = utilities.turnNumDegrees(robot, 90, .2)
            if done:
                robot.autostate = 'robocheck'
        elif robot.autostate == 'robocheck': #check for bot
            done = utilities.robocheckFeet(robot, 12)
            print("GOt to check")
            if robot.moveSafe: #robot there
                print("Safe to move")
                done = utilities.turnNumDegrees(robot, 180, .2)
                if done:
                    print("Safe to aim")
                    done = ultrasonicAim(robot, 1)
                    if done:
                        print("Safe to shoot")
                        #done = utilities.autoShootLow(robot)
                        if done:
                            return True
            else: #robot not there
                print("Not STM")
                #done = utilities.driveNumInches(robot, 1, .2, 36)
                done = True
                if done:
                    robot.autostate = 'aim'
            pass
        elif robot.autostate == 'aim': #aim bot w/ ultrasonic
            print("AIMING AGAIN")
            done = utilities.ultrasonicAim(robot, 5)
            if done:
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            #done = utilities.autoShoot(robot)
            print("Got to Shoot")
            robot.autostate = 'move2'
            #if done:
            #   robot.autostate = 'move2'
        elif robot.autostate == 'move2': #move back lil bizz
            #done = utilities.driveNumInches(robot, -1, .5, 12)
            done = True
            if done:
                robot.autostate = 'done'
        elif robot.autostate == 'done': #rest now
            print("Done")
            return True

    def boogieWoogie(robot, num, speed):
        print("Got to TND")
        #currentPos = robot.gyro.getAngle()
        numMin = num - 0
        numMax = num + 0
        angle = robot.gyro.getAngle()
        if angle < 0:
            angle + 360

        if angle > 360:
            angle - 360

        value = abs(angle - num)
        print(angle)

        if angle < numMin or angle > numMax:
            if value >= 180: #turn left
            #if ((value < 0 and abs(value) > 180) or (value > 0 and abs(value) < 180)): #TURN LEFT
                #robot.right.set(0)
                #robot.left.set(direction * speed)
                robot.drivetrainController.frontLeft.set(-1 * speed)
                robot.drivetrainController.frontRight.set(-1 * speed)
                robot.drivetrainController.rearLeft.set(-1 * speed)
                robot.drivetrainController.rearRight.set(-1 * speed)

            if value < 180: #turn right
            #elif ((value <= 0 and abs(value) <= 180) or (value >= 0 and abs(value) >= 180)): #TURN RIGHT
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

    def lastResortStart(robot): #drive off line. last resort if nothing working. /panic hourzz/
        print("Got to LRS")
        #utilities.driveNumInches(robot, 1, .2, 1)
        utilities.boogieWoogie(robot, 1, .2)

    #trevor's first gyro code:
    '''run gyro.com
    enter
    return True
if gyro = false:
    dont' run gyro(self) init'''
