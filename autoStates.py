import wpilib
from utilities import utilities

class AutoStates():
    def portStart(robot):
        if robot.autostate == 'start': #aim bot w/ ultrasonic
            done = utilities.ultrasonicAim(robot, 10)
            if done:
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            done = Shooter.autoShootLow(robot)
            if done:
                robot.autostate = 'move'
        elif robot.autostate == 'move': #move back lil bizz
            done = utilities.driveNumInches(robot, -1, .5, 48)
            if done:
                robot.autostate = 'done'
        elif robot.autostate == 'done': #cut everything to 0
            return True

    def offStart(robot):
        if robot.autostate == 'start': #move bot to wall spot
            done = utilities.ultrasonicAim(robot, 5)
            if done:
                robot.autostate = 'turn1'
        elif robot.autostate == 'turn1': #turn 90
            done = utilities.turnNumDegrees(robot, 90)
            if done:
                robot.autostate = 'move'
        elif robot.autostate == 'move': #move bot to shooting locale
            done = utilities.ultrasonicAim(robot, 5.5)
            if done:
                robot.autostate = 'turn2'
        elif robot.autostate == 'turn2': #turn to see bot
            done = utilities.turnNumDegrees(robot, 90)
            if done:
                robot.autostate = 'robocheck'
        elif robot.autostate == 'robocheck': #check for bot
            done = utilities.robocheckFeet(robot, 12)
            if self.moveSafe: #robot not there
                done = utilities.turnNumDegrees(robot, 180)
                if done:
                    done = ultrasonicAim(robot, 1)
                    if done:
                        done = Shooter.autoShootLow(robot)
                        if done:
                            return True
            else: #robot there
                done = utilities.driveNumInches(robot, 1, .5, 108)
                if done:
                    robot.autostate = 'aim'
            pass
        elif robot.autostate == 'aim': #aim bot w/ ultrasonic
            done = utilities.ultrasonicAim(robot, 10)
            if done:
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            done = Shooter.autoShoot(robot)
            if done:
                robot.autostate = 'move2'
        elif robot.autostate == 'move2': #move back lil bizz
            done = utilities.driveNumInches(robot, -1, .5, 48)
            if done:
                robot.autostate = 'move2'
        elif robot.autostate == 'done': #rest now
            return True

    def lastResortStart(robot): #drive off line. last resort if nothing working. /panic hourzz/
        utilities.driveNumInches(robot, 1, .1, 1)
    
