#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String


if __name__=='__main__':
    rospy.init_node("prime_node")
    rospy.loginfo("Prime no.s are as follows")

    pub=rospy.Publisher("numbering", String, queue_size=10)
    rate=rospy.Rate(5)
    c=0
    n=0
    d=1
    while not rospy.is_shutdown():
        while d<=n:
            if n%d==0:
                c=c+1
            d=d+1
        if c==2:
            pub.publish(rospy.loginfo(n))
            rate.sleep()
        d=1
        c=0
        n=n+1
    rospy.logerr("Node has been Killed")

        
