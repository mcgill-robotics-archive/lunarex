#ifndef ros_arduino_msgs_ArduinoFeedback_h
#define ros_arduino_msgs_ArduinoFeedback_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../ros/msg.h"
#include "std_msgs/Header.h"
#include "std_msgs/Float32.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Int8.h"
#include "std_msgs/Int16.h"

namespace arduino_msgs
{

  class ArduinoFeedback : public ros::Msg
  {
    public:
      std_msgs::Header header;
      std_msgs::Float32 linSpeed;
      std_msgs::Float32 angSpeed;
      std_msgs::Bool LF_motor_enable;
      std_msgs::Bool LF_motor_dir;
      std_msgs::Float32 LF_wheel_rpm;
      std_msgs::Int8 LF_motor_cmd;
      std_msgs::Int8 LF_servo_angle;
      std_msgs::Int16 LF_servo_cmd;
      std_msgs::Bool RF_motor_enable;
      std_msgs::Bool RF_motor_dir;
      std_msgs::Float32 RF_wheel_rpm;
      std_msgs::Int8 RF_motor_cmd;
      std_msgs::Int8 RF_servo_angle;
      std_msgs::Int16 RF_servo_cmd;
      std_msgs::Bool LR_motor_enable;
      std_msgs::Bool LR_motor_dir;
      std_msgs::Float32 LR_wheel_rpm;
      std_msgs::Int8 LR_motor_cmd;
      std_msgs::Int8 LR_servo_angle;
      std_msgs::Int16 LR_servo_cmd;
      std_msgs::Bool RR_motor_enable;
      std_msgs::Bool RR_motor_dir;
      std_msgs::Float32 RR_wheel_rpm;
      std_msgs::Int8 RR_motor_cmd;
      std_msgs::Int8 RR_servo_angle;
      std_msgs::Int16 RR_servo_cmd;

    virtual int serialize(unsigned char *outbuffer)
    {
      int offset = 0;
      offset += this->header.serialize(outbuffer + offset);
      offset += this->linSpeed.serialize(outbuffer + offset);
      offset += this->angSpeed.serialize(outbuffer + offset);
      offset += this->LF_motor_enable.serialize(outbuffer + offset);
      offset += this->LF_motor_dir.serialize(outbuffer + offset);
      offset += this->LF_wheel_rpm.serialize(outbuffer + offset);
      offset += this->LF_motor_cmd.serialize(outbuffer + offset);
      offset += this->LF_servo_angle.serialize(outbuffer + offset);
      offset += this->LF_servo_cmd.serialize(outbuffer + offset);
      offset += this->RF_motor_enable.serialize(outbuffer + offset);
      offset += this->RF_motor_dir.serialize(outbuffer + offset);
      offset += this->RF_wheel_rpm.serialize(outbuffer + offset);
      offset += this->RF_motor_cmd.serialize(outbuffer + offset);
      offset += this->RF_servo_angle.serialize(outbuffer + offset);
      offset += this->RF_servo_cmd.serialize(outbuffer + offset);
      offset += this->LR_motor_enable.serialize(outbuffer + offset);
      offset += this->LR_motor_dir.serialize(outbuffer + offset);
      offset += this->LR_wheel_rpm.serialize(outbuffer + offset);
      offset += this->LR_motor_cmd.serialize(outbuffer + offset);
      offset += this->LR_servo_angle.serialize(outbuffer + offset);
      offset += this->LR_servo_cmd.serialize(outbuffer + offset);
      offset += this->RR_motor_enable.serialize(outbuffer + offset);
      offset += this->RR_motor_dir.serialize(outbuffer + offset);
      offset += this->RR_wheel_rpm.serialize(outbuffer + offset);
      offset += this->RR_motor_cmd.serialize(outbuffer + offset);
      offset += this->RR_servo_angle.serialize(outbuffer + offset);
      offset += this->RR_servo_cmd.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->header.deserialize(inbuffer + offset);
      offset += this->linSpeed.deserialize(inbuffer + offset);
      offset += this->angSpeed.deserialize(inbuffer + offset);
      offset += this->LF_motor_enable.deserialize(inbuffer + offset);
      offset += this->LF_motor_dir.deserialize(inbuffer + offset);
      offset += this->LF_wheel_rpm.deserialize(inbuffer + offset);
      offset += this->LF_motor_cmd.deserialize(inbuffer + offset);
      offset += this->LF_servo_angle.deserialize(inbuffer + offset);
      offset += this->LF_servo_cmd.deserialize(inbuffer + offset);
      offset += this->RF_motor_enable.deserialize(inbuffer + offset);
      offset += this->RF_motor_dir.deserialize(inbuffer + offset);
      offset += this->RF_wheel_rpm.deserialize(inbuffer + offset);
      offset += this->RF_motor_cmd.deserialize(inbuffer + offset);
      offset += this->RF_servo_angle.deserialize(inbuffer + offset);
      offset += this->RF_servo_cmd.deserialize(inbuffer + offset);
      offset += this->LR_motor_enable.deserialize(inbuffer + offset);
      offset += this->LR_motor_dir.deserialize(inbuffer + offset);
      offset += this->LR_wheel_rpm.deserialize(inbuffer + offset);
      offset += this->LR_motor_cmd.deserialize(inbuffer + offset);
      offset += this->LR_servo_angle.deserialize(inbuffer + offset);
      offset += this->LR_servo_cmd.deserialize(inbuffer + offset);
      offset += this->RR_motor_enable.deserialize(inbuffer + offset);
      offset += this->RR_motor_dir.deserialize(inbuffer + offset);
      offset += this->RR_wheel_rpm.deserialize(inbuffer + offset);
      offset += this->RR_motor_cmd.deserialize(inbuffer + offset);
      offset += this->RR_servo_angle.deserialize(inbuffer + offset);
      offset += this->RR_servo_cmd.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "arduino_msgs/ArduinoFeedback"; };

  };

}
#endif