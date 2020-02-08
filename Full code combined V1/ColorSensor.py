import wpilib
import ctre


class ColorSensor:
        def __init__(self):
            self.sensor = None
        def setSensor(self, sensor):
            self.sensor = sensor
        def getColor(self):
            assert self.sensor != None
            c = self.sensor.getColor()
            #return str(str(c.red) + "," + str(c.green) + "," + str(c.blue))
            out = ""
            maptable = {"red" : [0.564, 0.321, 0.115], "green" : [0.150, 0.600, 0.248], "blue" : [0.110, 0.422, 0.469], "yellow" : [0.324, 0.568, 0.108]}
            costs = dict()
            for name in maptable:
                test = maptable[name]
                cost = 0
                cost += (c.red - test[0])**2
                cost += (c.green - test[1])**2
                cost += (c.blue - test[2])**2
                costs[name] = cost
            min_cost = min(costs.values())
            results = [a for a in costs if costs[a] == min_cost]
            return results[0]
