FILE(REMOVE_RECURSE
  "../src/corner_detector/msg"
  "../src/corner_detector/srv"
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/Corners.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Corners.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
