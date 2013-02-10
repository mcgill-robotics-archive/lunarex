# Install script for directory: /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds

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
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/stage/worlds" TYPE FILE FILES
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/lsp_test.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/wavefront-remote.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/vfh.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/autolab.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/everything.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/simple.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/test.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/uoa_robotics_lab.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/wifi.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/mbicp.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/wavefront.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/amcl-sonar.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/nd.cfg"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/pioneer_flocking.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/everything.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/gsh-simple.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/fasr.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/mbicp.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/fasr_plan.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/sensor_noise_module_demo.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/wifi.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/lsp_test.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/uoa_robotics_lab.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/pioneer_walle.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/autolab.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/large.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/fasr2.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/SFU.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/simple.world"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/objects.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/walle.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/uoa_robotics_lab_models.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/beacons.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/ubot.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/chatterbox.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/map.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/pioneer.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/pantilt.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/irobot.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/sick.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/hokuyo.inc"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/worldgen.sh"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/test.sh"
    "/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/worlds/cfggen.sh"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  INCLUDE("/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/worlds/benchmark/cmake_install.cmake")
  INCLUDE("/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/worlds/bitmaps/cmake_install.cmake")
  INCLUDE("/home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/worlds/wifi/cmake_install.cmake")

ENDIF(NOT CMAKE_INSTALL_LOCAL_ONLY)

