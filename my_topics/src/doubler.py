#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32  # using the package standard / int32 uses as a counter

# initialize node 
rospy.init_node('doubler') 

# call back function calling the message from sub
def callback(msg):
    doubled = Int32()           # data int 
    doubled.data = msg.data * 2 # multiplies by 2 
    pub.publish(doubled)        # publish the message in function pub

sub = rospy.Subscriber('number', Int32, callback)       # describe number msg
pub = rospy.Publisher('doubled', Int32, queue_size=3)   # publish msg and double next msg for the following publish

# keep node running until it terminated 
rospy.spin() 
