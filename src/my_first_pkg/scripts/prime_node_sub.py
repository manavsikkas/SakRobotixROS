#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def pub_call(text):
    rospy.loginfo(text.data)

    

if __name__ == '__main__':
    rospy.init_node("prime_node_sub")
    rospy.Subscriber("numbering", String, pub_call)
    rospy.spin()
    rospy.logerr("The connection is severed")