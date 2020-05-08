#!/usr/bin/env python
import rospy
from rico_topics.msg import Complex            # messge type Complex are imported by rico msg package
from random import random                      # import random for the complex number

# initialize the node and named as message publisher
rospy.init_node('message_publisher')          

# using publisher to register the topic
pub = rospy.Publisher(            
  'complex',                         # named 'Complex'
  Complex,                           # custom message type imported
  queue_size=3                       # queue size (can be less than 3)
)

# set up rate equal to 2 hz
rate = rospy.Rate(2)                   

# using while loop to execute and the loop will stop when it stops in ternimal
while not rospy.is_shutdown():    
   
  msg = Complex()                    # create msgs in the type of Complex
  msg.real = random()                # assign value of real
  msg.imaginary = random()           # assign value of imaginary

  pub.publish(msg)                   # publish and return the msgs to pub function
  rate.sleep()                       # the node go to asleep to keep the 2 hz goes