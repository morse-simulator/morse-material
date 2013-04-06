from pymorse import Morse
from time import sleep

with Morse() as morse:
    victim_detector = morse.robot.victim_detector
    waypoint = morse.robot.waypoint
    pose = morse.robot.pose

    go = waypoint.goto(10.0, 0.0, 0.0, 1.0, 1.0)
    for i in range(0, 3):
        print("Position %s status %s\n" % (
                pose.get_local_data().result(), waypoint.get_status().result()))
        sleep(1.0)
    go.result()

    print("Position %s status %s\n" % (
                pose.get_local_data(), waypoint.get_status()))
    victim_detector.heal().result()

    waypoint.goto(10.0, -10.0, 0.0, 1.0, 2.0).result()
    victim_detector.heal().result()

    waypoint.goto(15, -15.0, 0.0, 1.0, 2.0).result()
    victim_detector.heal().result()

    waypoint.goto(0.0, 0.0, 0.0, 0.5, 2.0).result()
