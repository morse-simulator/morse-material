from morse.builder import *

robot = ATRV()
pose = Pose()
robot.append(pose)
pose.add_stream('socket')
keyboard = Keyboard()
robot.append(keyboard)
pose.alter('Noise', pos_std=.5, rot_std=0, _2D='True')

perfect_pose = Pose()
robot.append(perfect_pose)
perfect_pose.add_stream('socket')

env = Environment("outdoors")
