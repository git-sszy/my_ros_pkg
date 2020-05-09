#!/usr/bin/env python
import rospy
from rico_services.srv import WordCount, WordCountResponse # custom service & <srv type> response service function 

# set up count_words function for word's character count and take them from request
def count_words(request):
  return len(request.words.split()) # request is going to separate the words into characters and convert into a length number of word

# initialize the node 
rospy.init_node('service_server')

# register service 
service = rospy.Service( 
  'word_count', # service named "word_count"
  WordCount,    # service type
  count_words   # function called by count_words
)

rospy.spin()    # waiting for the request