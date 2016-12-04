import argparse
from naoqi import ALProxy
from naoqi import ALBroker
import time

IP = "172.19.8.207"
PORT = 9559

def main1(robotIP, PORT):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    #motionProxy.wakeUp()
    #time.sleep(5)

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)
    time.sleep(2)

    # Send robot to First Position
    #postureProxy.goToPosture("right_hand_extended", 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="172.19.8.207",#---modify here to update tha IP---"192.168.0.125"
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,#---modify here to update port---9559
                        help="Robot port number")

    args = parser.parse_args()
    main1(args.ip, args.port)

#---first pos
import normal_pos
#normal_pos.do()
normal_pos.do1()
time.sleep(5)

#---Take picture
path="/home/nao/Demo_SD/Pictures"
name="picture"

tts = ALProxy("ALTextToSpeech", IP, PORT)
#tts.say("I will take a picture")
import run_search_comand as run

tts.say("I will take a picture")
pictureCapture = ALProxy("ALPhotoCapture")
pictureCapture.takePicture(path,name)
time.sleep(2)
run.do()

