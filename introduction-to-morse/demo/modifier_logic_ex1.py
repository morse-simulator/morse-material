from pymorse import Morse
from time import sleep

with Morse() as m:
    pose = m.robot.pose
    perfect_pose = m.robot.perfect_pose

    while True:
        pose_ = pose.get()
        perfect_pose_ = perfect_pose.get()
        for i in ['x', 'y', 'z', 'yaw', 'pitch', 'roll']:
            print('pose.%s : %f, perfect_pose.%s : %f, diff %f' % 
                  (i, pose_[i], i, perfect_pose_[i], 
                  pose_[i] - perfect_pose_[i]))
        sleep(1.0)
