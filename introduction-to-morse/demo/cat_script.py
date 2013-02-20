""" Simple script for the CAT AND MOUSE game tutorial

This will command the CAT, using two semantic cameras, to follow
after the MOUSE robot """
import pymorse

def visible(data):
    if not data:
        return False
    objects = [obj["name"] for obj in data["visible_objects"]]
    return "MOUSE" in objects

with pymorse.Morse() as simu:
    v_w_prev = None
    while True:
        seen_left  = visible(simu.cat.cameraL.last())
        seen_right = visible(simu.cat.cameraR.last())
        if seen_left and seen_right:
            v_w = {"v": 2, "w": 0}
        elif seen_left:
            v_w = {"v": 1.5, "w": 1}
        elif seen_right:
            v_w = {"v": 1.5, "w": -1}
        else:
            v_w = {"v": 0, "w": -1}

        if v_w != v_w_prev:
            simu.cat.motion.publish(v_w)
            v_w_prev = v_w

