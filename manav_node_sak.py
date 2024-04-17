#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def pub_call(text):
    rospy.loginfo("Hello Manav! You are now connected with Sak Robotix Lab")

if __name__ == '__main__':
    rospy.init_node("manav_node_sak")
    rospy.Subscriber("chatbox", String, pub_call)
    rospy.spin()
    rospy.logerr("The connection is severed")