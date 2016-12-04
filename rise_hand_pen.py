
from naoqi import ALProxy
IP = "192.168.0.125"

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1, 2])
keys.append([[-0.17, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.17, [3, -0.333333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([1, 2])
keys.append([[0, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([1, 2])
keys.append([[0.09, [3, -0.333333, 0], [3, 0.333333, 0]], [0.09, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([1, 2])
keys.append([[-0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.13, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([1, 2])
keys.append([[-0.410929, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.410929, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([1, 2])
keys.append([[-1.19386, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.19386, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1, 2])
keys.append([[0.3, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([1, 2])
keys.append([[0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [0.13, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([1, 2])
keys.append([[0.1, [3, -0.333333, 0], [3, 0.333333, 0]], [0.1, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([1, 2])
keys.append([[-0.17, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.17, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([1, 2])
keys.append([[-0.09, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.09, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([1, 2])
keys.append([[1.4712, [3, -0.333333, 0], [3, 0.333333, 0]], [1.4468, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([1, 2])
keys.append([[0.184555, [3, -0.333333, 0], [3, 0.333333, 0]], [0.217065, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1, 2])
keys.append([[0.0999997, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0999997, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([1, 2])
keys.append([[0.09, [3, -0.333333, 0], [3, 0.333333, 0]], [0.09, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([1, 2])
keys.append([[0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [0.13, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([1, 2])
keys.append([[0.410929, [3, -0.333333, 0], [3, 0.333333, 0]], [0.410929, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1, 2])
keys.append([[1.19386, [3, -0.333333, 0], [3, 0.333333, 0]], [2.08197, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1, 2])
keys.append([[0.3, [3, -0.333333, 0], [3, 0.333333, 0]], [0.86, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([1, 2])
keys.append([[0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [0.13, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([1, 2])
keys.append([[-0.1, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.1, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([1, 2])
keys.append([[-0.17, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.17, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([1, 2])
keys.append([[-0.09, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.09, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1, 2])
keys.append([[1.4712, [3, -0.333333, 0], [3, 0.333333, 0]], [0.403929, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1, 2])
keys.append([[-0.184555, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0879278, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1, 2])
keys.append([[0.0999997, [3, -0.333333, 0], [3, 0.333333, 0]], [1.17641, [3, -0.333333, 0], [3, 0, 0]]])
def do2():
 try:
   motion = ALProxy("ALMotion", IP, 9559)
   motion = ALProxy("ALMotion")
   motion.angleInterpolationBezier(names, times, keys)

 except BaseException, err:
   print err
