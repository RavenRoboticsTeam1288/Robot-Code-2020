import wpilib
from wpilib import Gyro

class utilities():
    def turnNumDegrees(robot, num):
        #currentPos = robot.gyro.getAngle()
        numMin = num - .1
        numMax = num + .1
        angle = robot.gyro.getAngle()
        if angle < 0:
            angles + 360
        
        if angle > 360:
            angle - 360
            
        value = abs(angle - num)
        
        if angle > numMin and angle < numMax: #go forward
            robot.left.set(1)
            robot.right.set(1)

        elif angle < numMin or angle > numMax:
            #if value >= 180: #turn left
            if ((value < 0 and abs(value) > 180) or (value > 0 and abs(value) < 180)): #TURN LEFT
                robot.right.set(1)
                robot.left.set(0)

            #if value <= 180: #turn right
            elif ((value <= 0 and abs(value) <= 180) or (value >= 0 and abs(value) >= 180)): #TURN RIGHT
                robot.right.set(0)
                robot.left.set(1)
