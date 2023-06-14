cmake_minimum_required(VERSION 3.8)
project(ros2_comm_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/PubTopic.msg"
  "msg/ReqService.msg"
  "msg/ResService.msg"
  "msg/RobotInfo.msg"
  "msg/SubTopic.msg"
)

set(srv_files
  "srv/ControlGroup.srv"
  "srv/ControlId.srv"
  "srv/ControlIdAll.srv"
  "srv/ControlIdGroup.srv"
  "srv/Info.srv"
  "srv/InfoId.srv"
  "srv/InfoList.srv"
  "srv/ListGroup.srv"
  "srv/ListGroupId.srv"
  "srv/ListType.srv"
  "srv/ListTypeId.srv"
  "srv/Load.srv"
  "srv/LoadPubTopic.srv"
  "srv/LoadReqService.srv"
  "srv/LoadResService.srv"
  "srv/LoadSubTopic.srv"
  "srv/SetType.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files}
  DEPENDENCIES builtin_interfaces
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_dependencies(rosidl_default_runtime)

ament_package()
