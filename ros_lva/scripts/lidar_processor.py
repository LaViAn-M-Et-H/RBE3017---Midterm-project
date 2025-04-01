#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def lidar_callback(data):
    rospy.loginfo("Nhận dữ liệu LiDAR với %d điểm", len(data.ranges))

if __name__ == '__main__':
    rospy.init_node('lidar_processor')
    rospy.Subscriber("/scan", LaserScan, lidar_callback)
    rospy.spin()
