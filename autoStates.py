import wpilib
from utilities import utilities
from Shooter import ShooterController

class AutoStates():
    def portStart(robot):
        if robot.autostate == 'start': #aim bot w/ ultrasonic
            done = utilities.ultrasonicAim(robot, 10)
            if done:
                print("PortStart 1 - start")
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            done = Shooter.autoShootLow(robot)
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

    def offStart(robot):
        print("Got to starting")
        if robot.autostate == 'Test':
            print("Format is: [Start] [section] - [completed action]")
            done = utilities.ultrasonicAim(robot, 5)
            if done:
                print("OffStart 1 - start")
                robot.autostate = 'turn1'
        elif robot.autostate == 'turn1': #turn 90
            print("die")
            done = utilities.turnNumDegrees(robot, 90)
            if done:
                print("OffStart 2 - turn1")
                robot.autostate = 'move'
        elif robot.autostate == 'move': #move bot to shooting locale
            done = utilities.ultrasonicAim(robot, 5.5)
            if done:
                print("OffStart 3 - move")
                robot.autostate = 'turn2'
        elif robot.autostate == 'turn2': #turn to see bot
            done = utilities.turnNumDegrees(robot, 90)
            if done:
                print("OffStart 4 - turn2")
                robot.autostate = 'robocheck'
        elif robot.autostate == 'robocheck': #check for bot
            done = utilities.robocheckFeet(robot, 12)
            if robot.moveSafe: #robot not there
                print("OffStart Move Safe")
                done = utilities.turnNumDegrees(robot, 180)
                if done:
                    print("OffStart Move Safe 2 - turn")
                    done = ultrasonicAim(robot, 1)
                    if done:
                        print("OffStart Move Safe 3 - aim")
                        done = Shooter.autoShootLow(robot) #when it breaks on thursday put the prints in the functions themselves.
                        if done:
                            print("OffStart Move Safe 4 - shoot")
                            return True
            else: #robot there
                done = utilities.driveNumInches(robot, 1, .5, 108)
                if done:
                    print("OffStart Move Not Safe - drive")
                    robot.autostate = 'aim'
            pass
        elif robot.autostate == 'aim': #aim bot w/ ultrasonic
            done = utilities.ultrasonicAim(robot, 10)
            if done:
                print("Offstart 5 - aim")
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot': #shoot balls
            done = ShooterController.AutoShooting(robot)
            if done:
                print("Offstart 6 - shoot")
                robot.autostate = 'move2'
        elif robot.autostate == 'move2': #move back lil bizz
            done = utilities.driveNumInches(robot, -1, .5, 48)
            if done:
                print("Offstart 7 - move2")
                robot.autostate = 'move2'
        elif robot.autostate == 'done': #rest now
            print("Offstart 8 - done")
            return True

    def lastResortStart(robot): #drive off line. last resort if nothing working. /panic hourzz/
        utilities.driveNumInches(robot, 1, .1, 1)
        print("PANIC!! but this is actually right")
        return True

