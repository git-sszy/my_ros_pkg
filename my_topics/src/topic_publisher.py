#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32   # using rospy and std_msgs to execute the node

# initialize node
rospy.init_node( 
  'topic_publisher'              # publisher is set up as a default name
)

# register a topic
pub = rospy.Publisher( 
  'counter',                     # topic name
  Int32,                         # topic type int 32 from std_msgs
  queue_size=5                   # queue size for keeping buffer, can't be too large
)


rate = rospy.Rate(2)             # sleep in a rate 2 in Hz

# initializing the loop count is 0
count = 0

# loop keeps runninng unless the rospy.is stops
while not rospy.is_shutdown():   
    pub.publish(count)           # publish function with a variable pub
    count += 1                   # increment by 1
    rate.sleep()                 # the loop weight the pospy.sleep according to the hz