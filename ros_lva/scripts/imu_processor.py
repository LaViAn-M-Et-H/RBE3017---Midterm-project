#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu

def imu_callback(data):
    orientation = data.orientation
    angular_vel = data.angular_velocity
    linear_accel = data.linear_acceleration
    
    rospy.loginfo("IMU Data - Orientation: %s", str(orientation))

if __name__ == '__main__':
    rospy.init_node('imu_processor')
    rospy.Subscriber("/imu/data", Imu, imu_callback)
    rospy.spin()
