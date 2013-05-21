FILE(REMOVE_RECURSE
  "../src/kinect_node/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/kinectSafeDistance.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_kinectSafeDistance.lisp"
  "../srv_gen/lisp/KinectData.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_KinectData.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
