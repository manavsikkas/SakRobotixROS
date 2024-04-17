#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
if __name__=='__main__':
    rospy.init_node("manav_node")
    rospy.loginfo("Node has started.")

    pub=rospy.Publisher("chatbox", String, queue_size=10)
    rate=rospy.Rate(5)
    while not rospy.is_shutdown():
        pub.publish(rospy.loginfo("Hello! Manav this side."))
        rate.sleep()
    rospy.logerr("Node has been Killed")