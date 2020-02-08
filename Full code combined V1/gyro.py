import wpilib
from wpilib import Gyro

class gyro():
    def turnNumDegrees(robot, num, speed):
        angle = robot.gyro.getAngle()
        angle = angle % 360.0
        if angle < 0.0:
            angle = angle + 360.0
        print(angle)

        goalMin = num - .5
        goalMax = num + .5


        if angle > goalMax:
            robot.right.set(0)
            robot.left.set(direction * speed)
            #robot.drivetrainController.frontLeft.set(-1 * speed)
            #robot.drivetrainController.frontRight.set(-1 * speed)
            #robot.drivetrainController.rearLeft.set(-1 * speed)
            #robot.drivetrainController.rearRight.set(-1 * speed)

        elif angle < goalMin:
            robot.right.set(direction * speed)
            robot.left.set(0)
            #robot.drivetrainController.frontLeft.set(1 * speed)
            #robot.drivetrainController.frontRight.set(1 * speed)
            #robot.drivetrainController.rearLeft.set(1 * speed)
            #robot.drivetrainController.rearRight.set(1 * speed)

        else:
            robot.right.set(0)
            robot.left.set(0)
            #robot.drivetrainController.frontLeft.set(0)
            #robot.drivetrainController.frontRight.set(0)
            #robot.drivetrainController.rearLeft.set(0)
            #robot.drivetrainController.rearRight.set(0)
            return True
