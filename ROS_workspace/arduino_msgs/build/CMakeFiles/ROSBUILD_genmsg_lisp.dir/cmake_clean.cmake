FILE(REMOVE_RECURSE
  "../msg_gen"
  "../msg_gen"
  "../src/arduino_msgs/msg"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/LiteArduinoFeedback.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_LiteArduinoFeedback.lisp"
  "../msg_gen/lisp/ArduinoFeedback.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ArduinoFeedback.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
