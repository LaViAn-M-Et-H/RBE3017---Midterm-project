#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState

def joint_state_callback(msg):
    joints_to_display = ['motor_1_joint', 'motor_2_joint', 'motor_3_joint', 'motor_4_joint']
    for i, joint_name in enumerate(msg.name):
        if joint_name in joints_to_display:
            position = msg.position[i]
            velocity = msg.velocity[i] if i < len(msg.velocity) else 0.0 
            rospy.loginfo("%s: Position = %.3f rad, Velocity = %.3f rad/s", joint_name, position, velocity)

def encoder_display():
    rospy.init_node('encoder_processor', anonymous=True)
    rospy.Subscriber('/joint_states', JointState, joint_state_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        encoder_display()
    except rospy.ROSInterruptException:
        pass
