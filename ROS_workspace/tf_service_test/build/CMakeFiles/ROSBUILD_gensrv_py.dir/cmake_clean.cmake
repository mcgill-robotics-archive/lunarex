FILE(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/tf_service_test/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/tf_service_test/srv/__init__.py"
  "../src/tf_service_test/srv/_TestSrv.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
