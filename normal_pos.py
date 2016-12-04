from naoqi import ALProxy
from naoqi import ALBroker

import time

IP = "172.19.8.207"
PORT = 9559

# global Head_front
# global Head_rear
# global Head_middle
# global head_pressed


# Choregraphe bezier export in Python.

names = list()
times = list()
keys = list()

names.append("RElbowRoll")
times.append([0.8])
keys.append([[0.246087, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.8])
keys.append([[1.34019, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.8])
keys.append([[0.81, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.8])
keys.append([[0.286506, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.8])
keys.append([[0.00656497, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.8])
keys.append([[1.81453, [3, -0.266667, 0], [3, 0, 0]]])






# global head_pressed
head_pressed = 0
loop = 0


# ---asking for the pen
def do():
    tts = ALProxy("ALTextToSpeech", IP, PORT)
    tts.say("Give me the pen please")
    time.sleep(2)


def do1():
    try:
        myBroker = ALBroker("myBroker",
                            "0.0.0.0",  # listen to anyone
                            0,  # find a free port and use it
                            IP,  # parent broker IP
                            PORT)  # parent broker port



    except BaseException, err:
        print err
        # ---proxy for motion
    motion = ALProxy("ALMotion", IP, PORT)
    motion = ALProxy("ALMotion")

    #postureProxy = ALProxy("ALRobotPosture", IP, PORT)
    #postureProxy.goToPosture("right_hand_extended", 1)

    do()

    # ---proxy for senzor(memory)
    memoryProxy = ALProxy("ALMemory", IP, PORT)
    while loop == 0:

        Head_front = memoryProxy.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
        Head_rear = memoryProxy.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
        Head_middle = memoryProxy.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
        if Head_front == 1.0:
            global head_pressed #Primary error guilt
            head_pressed = 1
            global loop
            loop = 1
        if Head_middle == 1.0:
            global head_pressed
            head_pressed = 1
            global loop
            loop = 1
        if Head_rear == 1.0:
            global head_pressed
            head_pressed = 1
            global loop
            loop = 1

        motion.angleInterpolationBezier(names, times, keys)
        time.sleep(0.02)

    if loop == 1:
        tts = ALProxy("ALTextToSpeech", IP, PORT)
        tts.say("Thank you")
        import close_hand
        close_hand.do3()
