#! /usr/bin/env python
import rospy
import time         # for regular Python timing
import actionlib    # for actions!
from rico_actions.msg import \
        TimerAction, TimerGoal, TimerResult, TimerFeedback  # action types

# set up feedback callback function for client request 
def the_feedback_cb(feedback): 
    print('[Feedback] Time elapsed: %f' %   # setup time elapsed function and calculated by 'to_sec' method
    	(feedback.time_elapsed.to_sec()))
    print('[Feedback] Time remaining: %f' % # setup time remaining function and calculated by 'to_sec' method
    	(feedback.time_remaining.to_sec()))

# initialize node 
rospy.init_node('timer_action_client') # named node 'timer_action_client'

# register client
client = actionlib.SimpleActionClient( 
    'timer',        # named action server 'timer'
    TimerAction 	# action message type
)

# wait for action server
client.wait_for_server()   

# set up goal object
goal = TimerGoal() 

# set field and set up duration is 5 secs        	
goal.time_to_wait = rospy.Duration.from_sec(5.0) 

# Uncomment this line to test server-side abort:
# goal.time_to_wait = rospy.Duration.from_sec(500.0)   # while the client request duration is over 60 sec, the server will abort the request

# send goal 
client.send_goal(goal, feedback_cb=the_feedback_cb ) 
# Uncomment these lines to test goal preemption:
# time.sleep(3.0)           # sleep every 3 secs
# client.cancel_goal()      # cancel the goal

# wait for action server to finish
client.wait_for_result() 

# print results
print('[Result] State: %d' % (client.get_state()))       # print states
print('[Result] Status: %s' % (client.get_goal_status_text()))     #print status

# check for whether get the result
if client.get_result():
    print('[Result] Time elapsed: %f' %
        (client.get_result().time_elapsed.to_sec()))
    print('[Result] Updates sent: %d' % 
        (client.get_result().updates_sent))