from morse.builder import *
from morse.builder.robots.pr2 import PR2

# A 'naked' PR2 robot to the scene
james = PR2()
james.translate(x=2.5, y=3.2, z=0.0)

pr2_posture = Sensor('pr2_posture')
james.append(pr2_posture)
pr2_posture.configure_mw('ros')

# An odometry sensor to get odometry information
odometry = Sensor('odometry')
james.append(odometry)
odometry.configure_mw('ros')

# Keyboard control
keyboard = Actuator('keyboard')
keyboard.name = 'keyboard_control'
james.append(keyboard)

# Set the environment
env = Environment('tum_kitchen/tum_kitchen')
env.aim_camera([1.0470, 0, 0.7854])
