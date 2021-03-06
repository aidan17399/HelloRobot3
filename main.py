from gopigo import *
import time


class Piggy(object):

    def __init__(self):
        print("i am alive")

    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15) #  stpre the distance reading
        if look >80:
            fwd()
            time.sleep(1)
            stop()

    def cruise(self):
        """drive forward, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)

    def servo_sweep(self):
        """loops in a 120 degree arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)


    def cha_cha(self):
         for x in range(5):
             right_rot()
             time.sleep(.5)
             left_rot()
             time.sleep(.5)
             stop()

p = Piggy()


