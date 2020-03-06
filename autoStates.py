import wpilib
from utilities import utilities
from Shooter import ShooterController

class AutoStates():
    def portStart(robot):
        if robot.autostate == 'Test': #aim bot w/ ultrasonic
            done = utilities.ultrasonicAim(robot, 10)
            if done:
                print("PortStart 1 - start")
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            done = ShooterController.AutoShooting(robot)
            if done:
                print("PortStart 2 - shoot")
                robot.autostate = 'move'
        elif robot.autostate == 'move': #move back lil bizz
            done = utilities.driveNumInches(robot, -1, .5, 48)
            if done:
                print("PortStart 3 - move")
                robot.autostate = 'done'
        elif robot.autostate == 'done': #cut everything to 0
            print("PortStart 4 - done")
            return True

def lastResortStart(robot): #drive off line. last resort if nothing working. /panic hourzz/
        utilities.driveNumInches(robot, 1, .1, 36)
        print("PANIC!! but this is actually right")
        return True
