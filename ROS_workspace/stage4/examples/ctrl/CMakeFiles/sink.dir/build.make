# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4

# Include any dependencies generated for this target.
include examples/ctrl/CMakeFiles/sink.dir/depend.make

# Include the progress variables for this target.
include examples/ctrl/CMakeFiles/sink.dir/progress.make

# Include the compile flags for this target's objects.
include examples/ctrl/CMakeFiles/sink.dir/flags.make

examples/ctrl/CMakeFiles/sink.dir/sink.o: examples/ctrl/CMakeFiles/sink.dir/flags.make
examples/ctrl/CMakeFiles/sink.dir/sink.o: Stage/examples/ctrl/sink.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object examples/ctrl/CMakeFiles/sink.dir/sink.o"
	cd /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/sink.dir/sink.o -c /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/examples/ctrl/sink.cc

examples/ctrl/CMakeFiles/sink.dir/sink.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sink.dir/sink.i"
	cd /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/examples/ctrl/sink.cc > CMakeFiles/sink.dir/sink.i

examples/ctrl/CMakeFiles/sink.dir/sink.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sink.dir/sink.s"
	cd /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/examples/ctrl/sink.cc -o CMakeFiles/sink.dir/sink.s

examples/ctrl/CMakeFiles/sink.dir/sink.o.requires:
.PHONY : examples/ctrl/CMakeFiles/sink.dir/sink.o.requires

examples/ctrl/CMakeFiles/sink.dir/sink.o.provides: examples/ctrl/CMakeFiles/sink.dir/sink.o.requires
	$(MAKE) -f examples/ctrl/CMakeFiles/sink.dir/build.make examples/ctrl/CMakeFiles/sink.dir/sink.o.provides.build
.PHONY : examples/ctrl/CMakeFiles/sink.dir/sink.o.provides

examples/ctrl/CMakeFiles/sink.dir/sink.o.provides.build: examples/ctrl/CMakeFiles/sink.dir/sink.o

# Object files for target sink
sink_OBJECTS = \
"CMakeFiles/sink.dir/sink.o"

# External object files for target sink
sink_EXTERNAL_OBJECTS =

examples/ctrl/sink.so: examples/ctrl/CMakeFiles/sink.dir/sink.o
examples/ctrl/sink.so: libstage/libstage.so.4.1.1
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libGLU.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libGL.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libSM.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libICE.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libX11.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libXext.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libltdl.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libjpeg.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libpng.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libz.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libGL.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libSM.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libICE.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libX11.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libXext.so
examples/ctrl/sink.so: /usr/lib/i386-linux-gnu/libm.so
examples/ctrl/sink.so: examples/ctrl/CMakeFiles/sink.dir/build.make
examples/ctrl/sink.so: examples/ctrl/CMakeFiles/sink.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared module sink.so"
	cd /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sink.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/ctrl/CMakeFiles/sink.dir/build: examples/ctrl/sink.so
.PHONY : examples/ctrl/CMakeFiles/sink.dir/build

examples/ctrl/CMakeFiles/sink.dir/requires: examples/ctrl/CMakeFiles/sink.dir/sink.o.requires
.PHONY : examples/ctrl/CMakeFiles/sink.dir/requires

examples/ctrl/CMakeFiles/sink.dir/clean:
	cd /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl && $(CMAKE_COMMAND) -P CMakeFiles/sink.dir/cmake_clean.cmake
.PHONY : examples/ctrl/CMakeFiles/sink.dir/clean

examples/ctrl/CMakeFiles/sink.dir/depend:
	cd /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/Stage/examples/ctrl /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4 /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl /home/lunarex/McGill_LunarEx_2013/ROS_workspace/stage4/examples/ctrl/CMakeFiles/sink.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/ctrl/CMakeFiles/sink.dir/depend

