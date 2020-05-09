#!/usr/bin/env python
import rospy
from rico_services.srv import WordCount
import sys     # provide for args

# initialze node and named service_client
rospy.init_node('service_client')

# set up function waiting for service word_count
rospy.wait_for_service('word_count') 
word_counter = rospy.ServiceProxy(    # set up proxy
  'word_count',                       # service named 'word_count' the same in server
  WordCount                           # service type imported
)

words = ' '.join(sys.argv[1:])   # parse args -- call the word_counter function and in the command list the args one another with a space
word_count = word_counter(words) # get the words from word_counter in server

print(words+'--> has '+str(word_count.count)+' words') # print our the words and the number of the length