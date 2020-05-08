#!/usr/bin/env python
import rospy
from rico_topics.msg import Complex   # import Complex 

# callback function is going to print the info of the node
def callback(msg):
    print 'Real:', msg.real           # print real msg
    print 'Imaginary:', msg.imaginary # print imag msg
    print                             # blank line

# initialize the node and named it message_subscriber
rospy.init_node('message_subscriber') 

# register the topic and scribe the msg to the Complex topic 
sub = rospy.Subscriber( 
  'complex',                  # topic name 'complex', the same as it in msg publisher
   Complex,                   # custom type Complex field
  callback                    # callback function and return the value around 2 hz to the function callback
)

rospy.spin()                  # keep node running until shut down