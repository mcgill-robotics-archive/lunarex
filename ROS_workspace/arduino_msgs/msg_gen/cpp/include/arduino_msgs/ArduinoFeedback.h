/* Auto-generated by genmsg_cpp for file /home/ernie/McGill_LunarEx_2013/ROS_workspace/arduino_msgs/msg/ArduinoFeedback.msg */
#ifndef ARDUINO_MSGS_MESSAGE_ARDUINOFEEDBACK_H
#define ARDUINO_MSGS_MESSAGE_ARDUINOFEEDBACK_H
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
#include "std_msgs/Float32.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Int16.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Int16.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Int16.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Int16.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"

namespace arduino_msgs
{
template <class ContainerAllocator>
struct ArduinoFeedback_ {
  typedef ArduinoFeedback_<ContainerAllocator> Type;

  ArduinoFeedback_()
  : header()
  , linSpeed()
  , angSpeed()
  , LF_direction()
  , LF_servo_angle()
  , LF_servo_pwm()
  , LF_wheel_rpm()
  , LF_motor_signal()
  , RF_direction()
  , RF_servo_angle()
  , RF_servo_pwm()
  , RF_wheel_rpm()
  , RF_motor_signal()
  , LR_direction()
  , LR_servo_angle()
  , LR_servo_pwm()
  , LR_wheel_rpm()
  , LR_motor_signal()
  , RR_direction()
  , RR_servo_angle()
  , RR_servo_pwm()
  , RR_wheel_rpm()
  , RR_motor_signal()
  {
  }

  ArduinoFeedback_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , linSpeed(_alloc)
  , angSpeed(_alloc)
  , LF_direction(_alloc)
  , LF_servo_angle(_alloc)
  , LF_servo_pwm(_alloc)
  , LF_wheel_rpm(_alloc)
  , LF_motor_signal(_alloc)
  , RF_direction(_alloc)
  , RF_servo_angle(_alloc)
  , RF_servo_pwm(_alloc)
  , RF_wheel_rpm(_alloc)
  , RF_motor_signal(_alloc)
  , LR_direction(_alloc)
  , LR_servo_angle(_alloc)
  , LR_servo_pwm(_alloc)
  , LR_wheel_rpm(_alloc)
  , LR_motor_signal(_alloc)
  , RR_direction(_alloc)
  , RR_servo_angle(_alloc)
  , RR_servo_pwm(_alloc)
  , RR_wheel_rpm(_alloc)
  , RR_motor_signal(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _linSpeed_type;
   ::std_msgs::Float32_<ContainerAllocator>  linSpeed;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _angSpeed_type;
   ::std_msgs::Float32_<ContainerAllocator>  angSpeed;

  typedef  ::std_msgs::Bool_<ContainerAllocator>  _LF_direction_type;
   ::std_msgs::Bool_<ContainerAllocator>  LF_direction;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _LF_servo_angle_type;
   ::std_msgs::Int8_<ContainerAllocator>  LF_servo_angle;

  typedef  ::std_msgs::Int16_<ContainerAllocator>  _LF_servo_pwm_type;
   ::std_msgs::Int16_<ContainerAllocator>  LF_servo_pwm;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _LF_wheel_rpm_type;
   ::std_msgs::Float32_<ContainerAllocator>  LF_wheel_rpm;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _LF_motor_signal_type;
   ::std_msgs::Int8_<ContainerAllocator>  LF_motor_signal;

  typedef  ::std_msgs::Bool_<ContainerAllocator>  _RF_direction_type;
   ::std_msgs::Bool_<ContainerAllocator>  RF_direction;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _RF_servo_angle_type;
   ::std_msgs::Int8_<ContainerAllocator>  RF_servo_angle;

  typedef  ::std_msgs::Int16_<ContainerAllocator>  _RF_servo_pwm_type;
   ::std_msgs::Int16_<ContainerAllocator>  RF_servo_pwm;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _RF_wheel_rpm_type;
   ::std_msgs::Float32_<ContainerAllocator>  RF_wheel_rpm;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _RF_motor_signal_type;
   ::std_msgs::Int8_<ContainerAllocator>  RF_motor_signal;

  typedef  ::std_msgs::Bool_<ContainerAllocator>  _LR_direction_type;
   ::std_msgs::Bool_<ContainerAllocator>  LR_direction;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _LR_servo_angle_type;
   ::std_msgs::Int8_<ContainerAllocator>  LR_servo_angle;

  typedef  ::std_msgs::Int16_<ContainerAllocator>  _LR_servo_pwm_type;
   ::std_msgs::Int16_<ContainerAllocator>  LR_servo_pwm;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _LR_wheel_rpm_type;
   ::std_msgs::Float32_<ContainerAllocator>  LR_wheel_rpm;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _LR_motor_signal_type;
   ::std_msgs::Int8_<ContainerAllocator>  LR_motor_signal;

  typedef  ::std_msgs::Bool_<ContainerAllocator>  _RR_direction_type;
   ::std_msgs::Bool_<ContainerAllocator>  RR_direction;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _RR_servo_angle_type;
   ::std_msgs::Int8_<ContainerAllocator>  RR_servo_angle;

  typedef  ::std_msgs::Int16_<ContainerAllocator>  _RR_servo_pwm_type;
   ::std_msgs::Int16_<ContainerAllocator>  RR_servo_pwm;

  typedef  ::std_msgs::Float32_<ContainerAllocator>  _RR_wheel_rpm_type;
   ::std_msgs::Float32_<ContainerAllocator>  RR_wheel_rpm;

  typedef  ::std_msgs::Int8_<ContainerAllocator>  _RR_motor_signal_type;
   ::std_msgs::Int8_<ContainerAllocator>  RR_motor_signal;


  typedef boost::shared_ptr< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ArduinoFeedback
typedef  ::arduino_msgs::ArduinoFeedback_<std::allocator<void> > ArduinoFeedback;

typedef boost::shared_ptr< ::arduino_msgs::ArduinoFeedback> ArduinoFeedbackPtr;
typedef boost::shared_ptr< ::arduino_msgs::ArduinoFeedback const> ArduinoFeedbackConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace arduino_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "897055af1a9b4d2b502796702e4743ce";
  }

  static const char* value(const  ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x897055af1a9b4d2bULL;
  static const uint64_t static_value2 = 0x502796702e4743ceULL;
};

template<class ContainerAllocator>
struct DataType< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "arduino_msgs/ArduinoFeedback";
  }

  static const char* value(const  ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
std_msgs/Float32 linSpeed\n\
std_msgs/Float32 angSpeed\n\
\n\
#std_msgs/Bool LF_enable\n\
std_msgs/Bool LF_direction\n\
std_msgs/Int8 LF_servo_angle\n\
std_msgs/Int16 LF_servo_pwm\n\
std_msgs/Float32 LF_wheel_rpm\n\
std_msgs/Int8 LF_motor_signal\n\
\n\
#std_msgs/Bool RF_enable\n\
std_msgs/Bool RF_direction\n\
std_msgs/Int8 RF_servo_angle\n\
std_msgs/Int16 RF_servo_pwm\n\
std_msgs/Float32 RF_wheel_rpm\n\
std_msgs/Int8 RF_motor_signal\n\
\n\
#std_msgs/Bool LR_enable\n\
std_msgs/Bool LR_direction\n\
std_msgs/Int8 LR_servo_angle\n\
std_msgs/Int16 LR_servo_pwm\n\
std_msgs/Float32 LR_wheel_rpm\n\
std_msgs/Int8 LR_motor_signal\n\
\n\
#std_msgs/Bool RR_enable\n\
std_msgs/Bool RR_direction\n\
std_msgs/Int8 RR_servo_angle\n\
std_msgs/Int16 RR_servo_pwm\n\
std_msgs/Float32 RR_wheel_rpm\n\
std_msgs/Int8 RR_motor_signal\n\
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
MSG: std_msgs/Float32\n\
float32 data\n\
================================================================================\n\
MSG: std_msgs/Bool\n\
bool data\n\
================================================================================\n\
MSG: std_msgs/Int8\n\
int8 data\n\
\n\
================================================================================\n\
MSG: std_msgs/Int16\n\
int16 data\n\
\n\
";
  }

  static const char* value(const  ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.linSpeed);
    stream.next(m.angSpeed);
    stream.next(m.LF_direction);
    stream.next(m.LF_servo_angle);
    stream.next(m.LF_servo_pwm);
    stream.next(m.LF_wheel_rpm);
    stream.next(m.LF_motor_signal);
    stream.next(m.RF_direction);
    stream.next(m.RF_servo_angle);
    stream.next(m.RF_servo_pwm);
    stream.next(m.RF_wheel_rpm);
    stream.next(m.RF_motor_signal);
    stream.next(m.LR_direction);
    stream.next(m.LR_servo_angle);
    stream.next(m.LR_servo_pwm);
    stream.next(m.LR_wheel_rpm);
    stream.next(m.LR_motor_signal);
    stream.next(m.RR_direction);
    stream.next(m.RR_servo_angle);
    stream.next(m.RR_servo_pwm);
    stream.next(m.RR_wheel_rpm);
    stream.next(m.RR_motor_signal);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ArduinoFeedback_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::arduino_msgs::ArduinoFeedback_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "linSpeed: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.linSpeed);
    s << indent << "angSpeed: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.angSpeed);
    s << indent << "LF_direction: ";
s << std::endl;
    Printer< ::std_msgs::Bool_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_direction);
    s << indent << "LF_servo_angle: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_servo_angle);
    s << indent << "LF_servo_pwm: ";
s << std::endl;
    Printer< ::std_msgs::Int16_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_servo_pwm);
    s << indent << "LF_wheel_rpm: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_wheel_rpm);
    s << indent << "LF_motor_signal: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.LF_motor_signal);
    s << indent << "RF_direction: ";
s << std::endl;
    Printer< ::std_msgs::Bool_<ContainerAllocator> >::stream(s, indent + "  ", v.RF_direction);
    s << indent << "RF_servo_angle: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.RF_servo_angle);
    s << indent << "RF_servo_pwm: ";
s << std::endl;
    Printer< ::std_msgs::Int16_<ContainerAllocator> >::stream(s, indent + "  ", v.RF_servo_pwm);
    s << indent << "RF_wheel_rpm: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.RF_wheel_rpm);
    s << indent << "RF_motor_signal: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.RF_motor_signal);
    s << indent << "LR_direction: ";
s << std::endl;
    Printer< ::std_msgs::Bool_<ContainerAllocator> >::stream(s, indent + "  ", v.LR_direction);
    s << indent << "LR_servo_angle: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.LR_servo_angle);
    s << indent << "LR_servo_pwm: ";
s << std::endl;
    Printer< ::std_msgs::Int16_<ContainerAllocator> >::stream(s, indent + "  ", v.LR_servo_pwm);
    s << indent << "LR_wheel_rpm: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.LR_wheel_rpm);
    s << indent << "LR_motor_signal: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.LR_motor_signal);
    s << indent << "RR_direction: ";
s << std::endl;
    Printer< ::std_msgs::Bool_<ContainerAllocator> >::stream(s, indent + "  ", v.RR_direction);
    s << indent << "RR_servo_angle: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.RR_servo_angle);
    s << indent << "RR_servo_pwm: ";
s << std::endl;
    Printer< ::std_msgs::Int16_<ContainerAllocator> >::stream(s, indent + "  ", v.RR_servo_pwm);
    s << indent << "RR_wheel_rpm: ";
s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.RR_wheel_rpm);
    s << indent << "RR_motor_signal: ";
s << std::endl;
    Printer< ::std_msgs::Int8_<ContainerAllocator> >::stream(s, indent + "  ", v.RR_motor_signal);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ARDUINO_MSGS_MESSAGE_ARDUINOFEEDBACK_H

