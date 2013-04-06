from morse.builder import *

robot = ATRV()
robot.translate(z=0.2)

waypoint = Waypoint()
robot.append(waypoint)
waypoint.add_service('socket')

victim_detector = SearchAndRescue()
robot.append(victim_detector)
victim_detector.translate(x=0.5, z=1.0)
victim_detector.add_service('socket')
victim_detector.properties( Heal_range=2.0, Abilities="1,2,3,4,5",
                            Angle = 180.0, Distance = 2.0, ObstacleAvoidance = True)

pose = Pose()
robot.append(pose)
pose.configure_service('socket')

env = Environment('outdoors')
env.add_service('socket')

victim = Victim()
victim.translate(x=10.0, y=0.0)

victim2 = Victim()
victim2.translate(x=10.0, y=-10.0)

victim3 = Victim()
victim3.translate(x=15.0, y=-15.0)
