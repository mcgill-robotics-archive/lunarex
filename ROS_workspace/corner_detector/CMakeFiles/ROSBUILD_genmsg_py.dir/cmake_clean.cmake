FILE(REMOVE_RECURSE
  "msg_gen"
  "srv_gen"
  "src/corner_detector/msg"
  "src/corner_detector/srv"
  "msg_gen"
  "srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "src/corner_detector/msg/__init__.py"
  "src/corner_detector/msg/_Corners.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
