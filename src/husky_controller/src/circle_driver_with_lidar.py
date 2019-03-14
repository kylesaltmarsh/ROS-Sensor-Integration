#!/usr/bin/env python
import sys
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def get_lidar_min(msg):
    global lidar_min
    lidar_min = min(msg.ranges)

def move_in_circles():
    rospy.init_node('husky_controller')
    pub = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=100)
    rate = rospy.Rate(10)
    vel_msg = Twist()

    print('Doing a safe burnout...')
    
    while not rospy.is_shutdown():
        vel_msg.linear.x = 5.0
        vel_msg.angular.z = 0.3

        print(lidar_min)
        if lidar_min < 0.5:
            sys.exit()

        pub.publish(vel_msg)
        rate.sleep()

if __name__=='__main__':
    try:
        estop = rospy.Subscriber('/scan', LaserScan, get_lidar_min)
        move_in_circles()
    except rospy.ROSInterruptException: pass
