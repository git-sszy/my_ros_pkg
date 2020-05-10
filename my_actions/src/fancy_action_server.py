#! /usr/bin/env python
import rospy
import time       # for regular Python timing
import actionlib  # for actions
from rico_actions.msg import \
    TimerAction, TimerGoal, TimerResult, TimerFeedback  # for action's message type

# define a action function to serve 
def do_timer(goal): 

    start_time = time.time()  # start time
    update_count = 0          #initialize the count 
    if goal.time_to_wait.to_sec() > 60.0: # check if the clients' request duration over 60 secs or not
        result = TimerResult()            # create a result object
        result.time_elapsed = rospy.Duration.from_sec(    # calculate the duration by subtract start time from current time
            time.time() - start_time)
        result.updates_sent = update_count # set the results 
        server.set_aborted(result, "Aborted: too long to wait")  # if the duration over 60 secs, aborted
        return 

# if the goal duration does not reach, started in the timer while loop 
    while (time.time()-start_time) < goal.time_to_wait.to_sec():
    
        if server.is_preempt_requested(): # check whether the client cancelled the request
            result = TimerResult()        # create result object
            result.time_elapsed = rospy.Duration.from_sec(  # calculate the time duration
                time.time() - start_time)
            result.updates_sent = update_count   # set the result 
            server.set_preempted(result, "Timer preempted") # return the result with 'Timer preempted'
            return

# if the client did not withdraw the feedback
        feedback = TimerFeedback()    # set up feedback object 
        feedback.time_elapsed = rospy.Duration.from_sec(  # field to calculate time duration and remains
            time.time() - start_time)
        feedback.time_remaining = \
            goal.time_to_wait - feedback.time_elapsed
        server.publish_feedback(feedback)   # publish feedback 
        update_count += 1         # increment by 1
        time.sleep(1.0)           # stop sec

# when the goal is met, publish the result 
    result = TimerResult()        #set up result object     
    result.time_elapsed = rospy.Duration.from_sec(
        time.time() - start_time)
    result.updates_sent = update_count    # set up result 
    server.set_succeeded(result, "Timer completed successfully")   # return the result 

# initialize node 
rospy.init_node('timer_action_server')    
server = actionlib.SimpleActionServer(     
    'timer', TimerAction, do_timer, False  # named as 'timer', msg type, action function, autostart server = false
)

# start action
server.start()  #start serve
rospy.spin()    # waiting for the client requests