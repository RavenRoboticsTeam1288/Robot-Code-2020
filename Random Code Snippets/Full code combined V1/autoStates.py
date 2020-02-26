import wpilib
class autoStates():
    def portStart(robot): #Ideal Start™
        if robot.autostate == 'start': #gotz to drivezz
            #done = utilities.DriveNumInches(MyRobot, 1, .5, 24)
            #if done:
            print("autoStart")
            done = utilities.turnNumDegrees(robot, 45, .5)
            if done:
                robot.autostate = 'done'
        elif robot.autostate == 'aim':
            done = utilities.ultrasonicAim(robot, 2)
            if done:
                robot.autostate = 'shoot'
        elif robot.autostate == 'shoot':
            done = utilities.autoShoot('fix here')
        elif robot.autostate == 'done': #says auto is complete, you can rest until teleop
            return True

    def midStart(robot): #First alternate Start™
        if autostate == 'start': #gotz to drivez
            pass #gyro
        elif autostate == 'move':
            print("midStart")
            done = utilities.DriveNumInches(MyRobot, 1, .5, 48)
            if done:
                autostate = 'aim'
        elif autostate == 'aim':
            done = utilities.ultrasonicAim(MyRobot, 'FIX HERE')
            if done:
                autostate = 'shoot'
        elif autostate == 'shoot':
            pass #shooting auto code
        elif autostate == 'done': #says auto is complete, you can rest until teleop
            return True

    def farStart(robot): #second alternate start™
        if autostate == 'start': #gotz to drivez
            pass #gyro
        elif autostate == 'move':
            print("farStart")
            done = utilities.DriveNumInches(robot, 1, .5, (30 * 12))
            if done:
                autostate = 'aim'
        elif autostate == 'aim':
            done = utilities.ultrasonicAim(robot, 'FIX HERE')
            if done:
                autostate = 'shoot'
        elif autostate == 'shoot':
            pass #shooting auto code
        elif autostate == 'done': #says auto is complete, you can rest until teleop
            return True
