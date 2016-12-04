# Choregraphe bezier export in Python.
from naoqi import ALProxy
from naoqi import ALBroker

IP = "172.19.8.207"

# Choregraphe bezier export in Python.

names = list()
times = list()
keys = list()

names.append("RElbowRoll")
times.append([2.9])
keys.append([[0.246087, [3, -0.966667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([2.9])
keys.append([[1.34019, [3, -0.966667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([2.9])
keys.append([[0.06, [3, -0.966667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([2.9])
keys.append([[0.286506, [3, -0.966667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([2.9])
keys.append([[0.00656497, [3, -0.966667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([2.9])
keys.append([[1.81453, [3, -0.966667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err



def do3():
 try:
   myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       IP,         # parent broker IP
       9559)       # parent broker port
   motion = ALProxy("ALMotion", IP, 9559)
   motion = ALProxy("ALMotion")
   motion.angleInterpolationBezier(names, times, keys)
 except BaseException, err:
   print err


