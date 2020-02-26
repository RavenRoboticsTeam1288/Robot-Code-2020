import wpilib

class utilities():
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
            
    #----------------------------------------------------------------------------
    def TimedButton(robot, motor, direction, speed, num, initTime):
        time = robot.timer.getMsClock() / 1000
        if time - initTime < num:
            motor.set(speed * direction)
            return False
        else:
            motor.set(0)
            return True
