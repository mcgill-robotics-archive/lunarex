FILE(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/tf_service_test/srv"
  "CMakeFiles/clean-test-results"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/clean-test-results.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
