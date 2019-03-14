#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

#a function to generate the random number
def move_in_circles():
    rospy.init_node('husky_controller')
    pub=rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=100)
    rate= rospy.Rate(10)
    vel_msg = Twist()

    print('Doing burnout...')

    while not rospy.is_shutdown():
        vel_msg.linear.x = 5.0
        vel_msg.angular.z = 0.5
        pub.publish(vel_msg)
        rate.sleep()
    

if __name__=='__main__':
    try:
        #Testing our function
        move_in_circles()
    except rospy.ROSInterruptException: pass


