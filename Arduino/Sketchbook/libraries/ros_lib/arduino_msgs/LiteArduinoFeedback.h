#ifndef ros_arduino_msgs_LiteArduinoFeedback_h
#define ros_arduino_msgs_LiteArduinoFeedback_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../ros/msg.h"
#include "std_msgs/Header.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Int8.h"

namespace arduino_msgs
{

  class LiteArduinoFeedback : public ros::Msg
  {
    public:
      std_msgs::Header header;
      std_msgs::Bool LF_motor_enable;
      std_msgs::Bool LF_motor_dir;
      std_msgs::Float32 LF_wheel_rpm;
      std_msgs::Int8 LF_motor_cmd;
      std_msgs::Float32 LF_servo_angle;
      std_msgs::Int8 LF_servo_cmd;

    virtual int serialize(unsigned char *outbuffer)
    {
      int offset = 0;
      offset += this->header.serialize(outbuffer + offset);
      offset += this->LF_motor_enable.serialize(outbuffer + offset);
      offset += this->LF_motor_dir.serialize(outbuffer + offset);
      offset += this->LF_wheel_rpm.serialize(outbuffer + offset);
      offset += this->LF_motor_cmd.serialize(outbuffer + offset);
      offset += this->LF_servo_angle.serialize(outbuffer + offset);
      offset += this->LF_servo_cmd.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->header.deserialize(inbuffer + offset);
      offset += this->LF_motor_enable.deserialize(inbuffer + offset);
      offset += this->LF_motor_dir.deserialize(inbuffer + offset);
      offset += this->LF_wheel_rpm.deserialize(inbuffer + offset);
      offset += this->LF_motor_cmd.deserialize(inbuffer + offset);
      offset += this->LF_servo_angle.deserialize(inbuffer + offset);
      offset += this->LF_servo_cmd.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "arduino_msgs/LiteArduinoFeedback"; };

  };

}
#endif