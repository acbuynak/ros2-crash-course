cmake_minimum_required(VERSION 3.5)
project(golf_club_support)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch meshes urdf rviz
  DESTINATION share/${PROJECT_NAME})

ament_package()