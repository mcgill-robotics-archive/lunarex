FILE(REMOVE_RECURSE
  "../msg_gen"
  "../msg_gen"
  "../src/arduino_msgs/msg"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/arduino_msgs/msg/__init__.py"
  "../src/arduino_msgs/msg/_ArduinoFeedback.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
