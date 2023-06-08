cmake_minimum_required(VERSION 3.5)
project(ros2_comm)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(Boost REQUIRED)
find_package(zyre REQUIRED)

include_directories(
  include include/
  ${Boost_INCLUDE_DIRS}
)

set(SOURCES
  src/main.cpp
)

set(EXECUTABLE_NAME "ros2_comm")
add_executable(${EXECUTABLE_NAME} ${SOURCES})

find_library(
  LIBFS
  NAMES libstdc++fs.a
  HINTS /usr/lib/gcc/x86_64-linux-gnu/7
  HINTS /usr/lib/gcc/x86_64-linux-gnu/9
REQUIRED)

set(DEPENDENCIES
  "rclcpp"
  "Boost"
  "zyre"
)

target_link_libraries(${EXECUTABLE_NAME} ${ament_LIBRARIES} ${Boost_LIBRARIES} ${LIBFS} zyre)
ament_target_dependencies(${EXECUTABLE_NAME} ${DEPENDENCIES})

install (TARGETS ${EXECUTABLE_NAME}
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()