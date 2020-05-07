#!/usr/bin/env python
import rospy                            # python pkg rospy
from std_msgs.msg import Int32          # ros pkg std msgs and int32 type

def callback(msg):                      # callback for receiving messages from subscriber 
  print(msg.data)                       # take the msg and unpack the data to print it to terminal

rospy.init_node('topic_subscriber')     # initialize node 'init_node' which is the same as publishers

# register the node and subcribe the topic 'counter' with the type Int32 whichs calls the function call back above
sub = rospy.Subscriber('counter', Int32, callback) 

# the node keeps running till it stopped in terminal 
rospy.spin() 