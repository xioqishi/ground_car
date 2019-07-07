#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time
import random


def send_go():
    b = random.randint(0,9)
    if (b > 5 ):
        a = 'forwards'
    else
        a = 'backwards'
    return a



def distance_sonic():
    pub = rospy.Publisher('command',String, queue_size=20)
    rospy.init_node('distance_sonic', anonymous = True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        control_wheels = send_go()
        pub.publish(control_wheels)
        rate.sleep()


if __name__ == "__main__":
    try:
        distance_sonic()
    except rospy.ROSInterruptException:
        pass

