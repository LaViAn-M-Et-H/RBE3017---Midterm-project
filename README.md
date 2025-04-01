# RBE3017---Midterm-project
Dự án giữa kỳ môn Lập trình Robot với ROS (RBE3017) - UET

## Đề tài dự án
Thiết kế một robot AGV gồm có xe và tay máy. Xe được điều khiển bằng cơ chế điều hướng Ackermann Steering (về sau đổi thành Differential Drive). Tay máy hai khớp gồm một khớp quay và một khớp tịnh tiến. Trên robot có gắn ba loại cảm biến: Lidar, IMU và Encoder.

## Yêu cầu các gói
* ROS Noetic
* Gazebo
* RViz
* Các gói điều khiển bổ sung trong gazebo-ros và rviz
  - robot_state_publisher
  - joint_state_publisher_gui
  - gazebo_ros
  - controller_manager
  - joint_state_controller
  - position_controllers
  - effort_controllers

# Hướng dẫn sử dụng

## 1. Tạo package và source về nguồn
```bash
cd catkin_ws
catkin_make
source devel/setup.bash
```

## 2. Khởi chạy mô phỏng và điều khiển
Chạy hiển thị đồng thời trên cả Gazebo và RViz

```bash
roslaunch ros_lva gazebo.launch
```

