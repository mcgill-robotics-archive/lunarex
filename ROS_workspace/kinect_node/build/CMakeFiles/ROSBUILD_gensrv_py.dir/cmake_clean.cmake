FILE(REMOVE_RECURSE
  "../src/kinect_node/srv"
  "../srv_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/kinect_node/srv/__init__.py"
  "../src/kinect_node/srv/_kinectSafeDistance.py"
  "../src/kinect_node/srv/_KinectData.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
