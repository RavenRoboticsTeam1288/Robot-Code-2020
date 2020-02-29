from cscore import CameraServer

def main():
	cs = CameraServer.getInstance()
	cs.enableLogging()

	usb1 = cs.startAutomaticCapture(dev=0) #if this doesn't work go and change the ids to the system ids in linux/roboRIO
	usb2 = cs.startAutomaticCapture(dev=1)

	cs.waitForever()
