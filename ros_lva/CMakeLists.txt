cmake_minimum_required(VERSION 3.0.2)
project(ros_lva)

# Tìm các package cần thiết (bổ sung sensor_msgs và message_generation)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  gazebo_ros
  controller_manager
  joint_state_controller
  effort_controllers
  position_controllers
  tf
  robot_state_publisher
  rviz
  joint_state_publisher_gui
)

# Tìm roslaunch để kiểm tra launch file
find_package(roslaunch REQUIRED)

# Khai báo message/services/actions (nếu cần)
# add_message_files(
#   FILES
#   YourMessage.msg
# )
# add_service_files(
#   FILES
#   YourService.srv
# )
# generate_messages(
#   DEPENDENCIES
#   std_msgs
#   sensor_msgs
# )

# Khai báo package và dependency
catkin_package(
  CATKIN_DEPENDS 
    roscpp 
    std_msgs 
    sensor_msgs
    gazebo_ros 
    controller_manager 
    joint_state_controller
    effort_controllers
    position_controllers 
    tf 
    robot_state_publisher
  DEPENDS 
    urdf
)

# Thêm include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

# Cài đặt Python scripts
catkin_install_python(
  PROGRAMS 
    scripts/lidar_processor.py 
    scripts/imu_processor.py 
    scripts/encoder_processor.py
    scripts/arm_teleop.py
    scripts/teleop_wasd.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Cài đặt các thư mục
install(DIRECTORY 
  config/
  launch/
  meshes/
  urdf/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Nếu có node C++ (ví dụ)
# add_executable(your_node src/your_node.cpp)
# target_link_libraries(your_node ${catkin_LIBRARIES})
# add_dependencies(your_node ${${PROJECT_NAME}_EXPORTED_TARGETS})
