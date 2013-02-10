# Install script for directory: /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/lunarex/nicksebtemp/stage")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "RELEASE")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/stage/assets" TYPE FILE FILES
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/question_mark.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/red.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/stall.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/blue.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/mainspower.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/mains.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/death.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/stagelogo.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/logo.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/green.png"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/rgb.txt"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/stage" TYPE FILE FILES "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/assets/rgb.txt")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
