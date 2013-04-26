/* Auto-generated by genmsg_cpp for file /home/lunarex/McGill_LunarEx_2013/ROS_workspace/arduino_msgs/msg/LiteArduinoFeedback.msg */
#ifndef ARDUINO_MSGS_MESSAGE_LITEARDUINOFEEDBACK_H
#define ARDUINO_MSGS_MESSAGE_LITEARDUINOFEEDBACK_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"

namespace arduino_msgs
{
template <class ContainerAllocator>
struct LiteArduinoFeedback_ {
  typedef LiteArduinoFeedback_<ContainerAllocator> Type;

  LiteArduinoFeedback_()
  : header()
  , LF_motor_enable()
  , LF_motor_dir()
  , LF_wheel_rpm()
  , LF_motor_cmd()
  , LF_servo_angle()
  , LF_servo_cmd()
  {
  }

  LiteArduinoFeedback_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , LF_motor_enable(_alloc)
  , LF_motor_dir(_alloc)
  , LF_wheel_rpm(_alloc)
  , LF_motor_cmd(_alloc)
  , LF_servo_angle(_alloc)
  , LF_servo_cmd(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::std_msgs::Bool_<ContainerAllocator>  _LF_motor_enable_type;
   ::std_msgs::Bool_<ContainerAllocator>  LF_motor_enable;

  typedef  ::std_msgs::Bool_<ContainerAllocator>  _LF_motor_dir_type;
   ::std_msgs::Bool_<ContainerAllocator>  LF_motor_dir;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _LF_wheel_rpm_type;
   ::std_msgs::Float32_<ContainerAllocator>  LF_wheel_rpm;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _LF_motor_cmd_type;
   ::std_msgs::Int8_<ContainerAllocator>  LF_motor_cmd;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _LF_servo_angle_type;
   ::std_msgs::Float32_<ContainerAllocator>  LF_servo_angle;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _LF_servo_cmd_type;
   ::std_msgs::Int8_<ContainerAllocator>  LF_servo_cmd;


  typedef boost::shared_ptr< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct LiteArduinoFeedback
typedef  ::arduino_msgs::LiteArduinoFeedback_<std::allocator<void> > LiteArduinoFeedback;

typedef boost::shared_ptr< ::arduino_msgs::LiteArduinoFeedback> LiteArduinoFeedbackPtr;
typedef boost::shared_ptr< ::arduino_msgs::LiteArduinoFeedback const> LiteArduinoFeedbackConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace arduino_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0ddc16df7b8b5e66b3f5a490e721c6f0";
  }

  static const char* value(const  ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0ddc16df7b8b5e66ULL;
  static const uint64_t static_value2 = 0xb3f5a490e721c6f0ULL;
};

template<class ContainerAllocator>
struct DataType< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "arduino_msgs/LiteArduinoFeedback";
  }

  static const char* value(const  ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
std_msgs/Bool LF_motor_enable\n\
std_msgs/Bool LF_motor_dir\n\
std_msgs/Float32 LF_wheel_rpm\n\
std_msgs/Int8 LF_motor_cmd\n\
\n\
std_msgs/Float32 LF_servo_angle\n\
std_msgs/Int8 LF_servo_cmd\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: std_msgs/Bool\n\
bool data\n\
================================================================================\n\
MSG: std_msgs/Float32\n\
float32 data\n\
================================================================================\n\
MSG: std_msgs/Int8\n\
int8 data\n\
\n\
";
  }

  static const char* value(const  ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.LF_motor_enable);
    stream.next(m.LF_motor_dir);
    stream.next(m.LF_wheel_rpm);
    stream.next(m.LF_motor_cmd);
    stream.next(m.LF_servo_angle);
    stream.next(m.LF_servo_cmd);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct LiteArduinoFeedback_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::arduino_msgs::LiteArduinoFeedback_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "LF_motor_enable: ";
s << std::endl;
    Printer< ::std_msgs::Bool_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_motor_enable);
    s << indent << "LF_motor_dir: ";
s << std::endl;
    Printer< ::std_msgs::Bool_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_motor_dir);
    s << indent << "LF_wheel_rpm: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_wheel_rpm);
    s << indent << "LF_motor_cmd: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_motor_cmd);
    s << indent << "LF_servo_angle: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_servo_angle);
    s << indent << "LF_servo_cmd: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_servo_cmd);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ARDUINO_MSGS_MESSAGE_LITEARDUINOFEEDBACK_H

