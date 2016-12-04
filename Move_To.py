from naoqi import ALProxy
from naoqi import ALBroker

IP = "172.18.8.98"
PORT = 9559



myBroker = ALBroker("myBroker",
                            "0.0.0.0",  # listen to anyone
                            0,  # find a free port and use it
                            IP,  # parent broker IP
                            PORT)  # parent broker port


motion = ALProxy("ALMotion", IP, PORT)
motion.moveInit()
motion.moveTo(0, 0.1, 0)