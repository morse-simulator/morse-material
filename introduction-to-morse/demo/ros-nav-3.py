from morse.builder import *
from morse.builder.robots.pr2 import PR2

# A 'naked' PR2 robot to the scene
james = PR2()
james.translate(x=2.5, y=3.2, z=0.0)

pr2_posture = Sensor('pr2_posture')
james.append(pr2_posture)
pr2_posture.configure_mw('ros')

sick = Sensor('sick')
sick.translate(x=0.275, z=0.252)
james.append(sick)
sick.properties(Visible_arc = False)
sick.properties(laser_range = 30.0)
sick.properties(resolution = 1.0)
sick.properties(scan_window = 180.0)
sick.configure_mw('ros')

# An odometry sensor to get odometry information
odometry = Sensor('odometry')
james.append(odometry)
odometry.configure_mw('ros')

# Keyboard control
keyboard = Actuator('keyboard')
keyboard.name = 'keyboard_control'
james.append(keyboard)

motion_controller = Actuator('xy_omega')
james.append(motion_controller)
motion_controller.configure_mw('ros')

# Set the environment
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
