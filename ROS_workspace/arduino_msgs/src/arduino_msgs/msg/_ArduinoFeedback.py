"""autogenerated by genpy from arduino_msgs/ArduinoFeedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class ArduinoFeedback(genpy.Message):
  _md5sum = "9c21fb0eb2b954841570cb63aabdb737"
  _type = "arduino_msgs/ArduinoFeedback"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

std_msgs/Float32 linSpeed
std_msgs/Float32 angSpeed

std_msgs/Bool LF_motor_enable
std_msgs/Bool LF_motor_dir
std_msgs/Int8 LF_servo_angle
std_msgs/Int16 LF_servo_cmd
std_msgs/Float32 LF_wheel_rpm
std_msgs/Int8 LF_motor_signal

std_msgs/Bool RF_motor_enable
std_msgs/Bool RF_motor_dir
std_msgs/Int8 RF_servo_angle
std_msgs/Int16 RF_servo_cmd
std_msgs/Float32 RF_wheel_rpm
std_msgs/Int8 RF_motor_signal

std_msgs/Bool LR_motor_enable
std_msgs/Bool LR_motor_dir
std_msgs/Int8 LR_servo_angle
std_msgs/Int16 LR_servo_cmd
std_msgs/Float32 LR_wheel_rpm
std_msgs/Int8 LR_motor_signal

std_msgs/Bool RR_motor_enable
std_msgs/Bool RR_motor_dir
std_msgs/Int8 RR_servo_angle
std_msgs/Int16 RR_servo_cmd
std_msgs/Float32 RR_wheel_rpm
std_msgs/Int8 RR_motor_signal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: std_msgs/Float32
float32 data
================================================================================
MSG: std_msgs/Bool
bool data
================================================================================
MSG: std_msgs/Int8
int8 data

================================================================================
MSG: std_msgs/Int16
int16 data

"""
  __slots__ = ['header','linSpeed','angSpeed','LF_motor_enable','LF_motor_dir','LF_servo_angle','LF_servo_cmd','LF_wheel_rpm','LF_motor_signal','RF_motor_enable','RF_motor_dir','RF_servo_angle','RF_servo_cmd','RF_wheel_rpm','RF_motor_signal','LR_motor_enable','LR_motor_dir','LR_servo_angle','LR_servo_cmd','LR_wheel_rpm','LR_motor_signal','RR_motor_enable','RR_motor_dir','RR_servo_angle','RR_servo_cmd','RR_wheel_rpm','RR_motor_signal']
  _slot_types = ['std_msgs/Header','std_msgs/Float32','std_msgs/Float32','std_msgs/Bool','std_msgs/Bool','std_msgs/Int8','std_msgs/Int16','std_msgs/Float32','std_msgs/Int8','std_msgs/Bool','std_msgs/Bool','std_msgs/Int8','std_msgs/Int16','std_msgs/Float32','std_msgs/Int8','std_msgs/Bool','std_msgs/Bool','std_msgs/Int8','std_msgs/Int16','std_msgs/Float32','std_msgs/Int8','std_msgs/Bool','std_msgs/Bool','std_msgs/Int8','std_msgs/Int16','std_msgs/Float32','std_msgs/Int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,linSpeed,angSpeed,LF_motor_enable,LF_motor_dir,LF_servo_angle,LF_servo_cmd,LF_wheel_rpm,LF_motor_signal,RF_motor_enable,RF_motor_dir,RF_servo_angle,RF_servo_cmd,RF_wheel_rpm,RF_motor_signal,LR_motor_enable,LR_motor_dir,LR_servo_angle,LR_servo_cmd,LR_wheel_rpm,LR_motor_signal,RR_motor_enable,RR_motor_dir,RR_servo_angle,RR_servo_cmd,RR_wheel_rpm,RR_motor_signal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ArduinoFeedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.linSpeed is None:
        self.linSpeed = std_msgs.msg.Float32()
      if self.angSpeed is None:
        self.angSpeed = std_msgs.msg.Float32()
      if self.LF_motor_enable is None:
        self.LF_motor_enable = std_msgs.msg.Bool()
      if self.LF_motor_dir is None:
        self.LF_motor_dir = std_msgs.msg.Bool()
      if self.LF_servo_angle is None:
        self.LF_servo_angle = std_msgs.msg.Int8()
      if self.LF_servo_cmd is None:
        self.LF_servo_cmd = std_msgs.msg.Int16()
      if self.LF_wheel_rpm is None:
        self.LF_wheel_rpm = std_msgs.msg.Float32()
      if self.LF_motor_signal is None:
        self.LF_motor_signal = std_msgs.msg.Int8()
      if self.RF_motor_enable is None:
        self.RF_motor_enable = std_msgs.msg.Bool()
      if self.RF_motor_dir is None:
        self.RF_motor_dir = std_msgs.msg.Bool()
      if self.RF_servo_angle is None:
        self.RF_servo_angle = std_msgs.msg.Int8()
      if self.RF_servo_cmd is None:
        self.RF_servo_cmd = std_msgs.msg.Int16()
      if self.RF_wheel_rpm is None:
        self.RF_wheel_rpm = std_msgs.msg.Float32()
      if self.RF_motor_signal is None:
        self.RF_motor_signal = std_msgs.msg.Int8()
      if self.LR_motor_enable is None:
        self.LR_motor_enable = std_msgs.msg.Bool()
      if self.LR_motor_dir is None:
        self.LR_motor_dir = std_msgs.msg.Bool()
      if self.LR_servo_angle is None:
        self.LR_servo_angle = std_msgs.msg.Int8()
      if self.LR_servo_cmd is None:
        self.LR_servo_cmd = std_msgs.msg.Int16()
      if self.LR_wheel_rpm is None:
        self.LR_wheel_rpm = std_msgs.msg.Float32()
      if self.LR_motor_signal is None:
        self.LR_motor_signal = std_msgs.msg.Int8()
      if self.RR_motor_enable is None:
        self.RR_motor_enable = std_msgs.msg.Bool()
      if self.RR_motor_dir is None:
        self.RR_motor_dir = std_msgs.msg.Bool()
      if self.RR_servo_angle is None:
        self.RR_servo_angle = std_msgs.msg.Int8()
      if self.RR_servo_cmd is None:
        self.RR_servo_cmd = std_msgs.msg.Int16()
      if self.RR_wheel_rpm is None:
        self.RR_wheel_rpm = std_msgs.msg.Float32()
      if self.RR_motor_signal is None:
        self.RR_motor_signal = std_msgs.msg.Int8()
    else:
      self.header = std_msgs.msg.Header()
      self.linSpeed = std_msgs.msg.Float32()
      self.angSpeed = std_msgs.msg.Float32()
      self.LF_motor_enable = std_msgs.msg.Bool()
      self.LF_motor_dir = std_msgs.msg.Bool()
      self.LF_servo_angle = std_msgs.msg.Int8()
      self.LF_servo_cmd = std_msgs.msg.Int16()
      self.LF_wheel_rpm = std_msgs.msg.Float32()
      self.LF_motor_signal = std_msgs.msg.Int8()
      self.RF_motor_enable = std_msgs.msg.Bool()
      self.RF_motor_dir = std_msgs.msg.Bool()
      self.RF_servo_angle = std_msgs.msg.Int8()
      self.RF_servo_cmd = std_msgs.msg.Int16()
      self.RF_wheel_rpm = std_msgs.msg.Float32()
      self.RF_motor_signal = std_msgs.msg.Int8()
      self.LR_motor_enable = std_msgs.msg.Bool()
      self.LR_motor_dir = std_msgs.msg.Bool()
      self.LR_servo_angle = std_msgs.msg.Int8()
      self.LR_servo_cmd = std_msgs.msg.Int16()
      self.LR_wheel_rpm = std_msgs.msg.Float32()
      self.LR_motor_signal = std_msgs.msg.Int8()
      self.RR_motor_enable = std_msgs.msg.Bool()
      self.RR_motor_dir = std_msgs.msg.Bool()
      self.RR_servo_angle = std_msgs.msg.Int8()
      self.RR_servo_cmd = std_msgs.msg.Int16()
      self.RR_wheel_rpm = std_msgs.msg.Float32()
      self.RR_motor_signal = std_msgs.msg.Int8()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2f2Bbhfb2Bbhfb2Bbhfb2Bbhfb.pack(_x.linSpeed.data, _x.angSpeed.data, _x.LF_motor_enable.data, _x.LF_motor_dir.data, _x.LF_servo_angle.data, _x.LF_servo_cmd.data, _x.LF_wheel_rpm.data, _x.LF_motor_signal.data, _x.RF_motor_enable.data, _x.RF_motor_dir.data, _x.RF_servo_angle.data, _x.RF_servo_cmd.data, _x.RF_wheel_rpm.data, _x.RF_motor_signal.data, _x.LR_motor_enable.data, _x.LR_motor_dir.data, _x.LR_servo_angle.data, _x.LR_servo_cmd.data, _x.LR_wheel_rpm.data, _x.LR_motor_signal.data, _x.RR_motor_enable.data, _x.RR_motor_dir.data, _x.RR_servo_angle.data, _x.RR_servo_cmd.data, _x.RR_wheel_rpm.data, _x.RR_motor_signal.data))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.linSpeed is None:
        self.linSpeed = std_msgs.msg.Float32()
      if self.angSpeed is None:
        self.angSpeed = std_msgs.msg.Float32()
      if self.LF_motor_enable is None:
        self.LF_motor_enable = std_msgs.msg.Bool()
      if self.LF_motor_dir is None:
        self.LF_motor_dir = std_msgs.msg.Bool()
      if self.LF_servo_angle is None:
        self.LF_servo_angle = std_msgs.msg.Int8()
      if self.LF_servo_cmd is None:
        self.LF_servo_cmd = std_msgs.msg.Int16()
      if self.LF_wheel_rpm is None:
        self.LF_wheel_rpm = std_msgs.msg.Float32()
      if self.LF_motor_signal is None:
        self.LF_motor_signal = std_msgs.msg.Int8()
      if self.RF_motor_enable is None:
        self.RF_motor_enable = std_msgs.msg.Bool()
      if self.RF_motor_dir is None:
        self.RF_motor_dir = std_msgs.msg.Bool()
      if self.RF_servo_angle is None:
        self.RF_servo_angle = std_msgs.msg.Int8()
      if self.RF_servo_cmd is None:
        self.RF_servo_cmd = std_msgs.msg.Int16()
      if self.RF_wheel_rpm is None:
        self.RF_wheel_rpm = std_msgs.msg.Float32()
      if self.RF_motor_signal is None:
        self.RF_motor_signal = std_msgs.msg.Int8()
      if self.LR_motor_enable is None:
        self.LR_motor_enable = std_msgs.msg.Bool()
      if self.LR_motor_dir is None:
        self.LR_motor_dir = std_msgs.msg.Bool()
      if self.LR_servo_angle is None:
        self.LR_servo_angle = std_msgs.msg.Int8()
      if self.LR_servo_cmd is None:
        self.LR_servo_cmd = std_msgs.msg.Int16()
      if self.LR_wheel_rpm is None:
        self.LR_wheel_rpm = std_msgs.msg.Float32()
      if self.LR_motor_signal is None:
        self.LR_motor_signal = std_msgs.msg.Int8()
      if self.RR_motor_enable is None:
        self.RR_motor_enable = std_msgs.msg.Bool()
      if self.RR_motor_dir is None:
        self.RR_motor_dir = std_msgs.msg.Bool()
      if self.RR_servo_angle is None:
        self.RR_servo_angle = std_msgs.msg.Int8()
      if self.RR_servo_cmd is None:
        self.RR_servo_cmd = std_msgs.msg.Int16()
      if self.RR_wheel_rpm is None:
        self.RR_wheel_rpm = std_msgs.msg.Float32()
      if self.RR_motor_signal is None:
        self.RR_motor_signal = std_msgs.msg.Int8()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.linSpeed.data, _x.angSpeed.data, _x.LF_motor_enable.data, _x.LF_motor_dir.data, _x.LF_servo_angle.data, _x.LF_servo_cmd.data, _x.LF_wheel_rpm.data, _x.LF_motor_signal.data, _x.RF_motor_enable.data, _x.RF_motor_dir.data, _x.RF_servo_angle.data, _x.RF_servo_cmd.data, _x.RF_wheel_rpm.data, _x.RF_motor_signal.data, _x.LR_motor_enable.data, _x.LR_motor_dir.data, _x.LR_servo_angle.data, _x.LR_servo_cmd.data, _x.LR_wheel_rpm.data, _x.LR_motor_signal.data, _x.RR_motor_enable.data, _x.RR_motor_dir.data, _x.RR_servo_angle.data, _x.RR_servo_cmd.data, _x.RR_wheel_rpm.data, _x.RR_motor_signal.data,) = _struct_2f2Bbhfb2Bbhfb2Bbhfb2Bbhfb.unpack(str[start:end])
      self.LF_motor_enable.data = bool(self.LF_motor_enable.data)
      self.LF_motor_dir.data = bool(self.LF_motor_dir.data)
      self.RF_motor_enable.data = bool(self.RF_motor_enable.data)
      self.RF_motor_dir.data = bool(self.RF_motor_dir.data)
      self.LR_motor_enable.data = bool(self.LR_motor_enable.data)
      self.LR_motor_dir.data = bool(self.LR_motor_dir.data)
      self.RR_motor_enable.data = bool(self.RR_motor_enable.data)
      self.RR_motor_dir.data = bool(self.RR_motor_dir.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2f2Bbhfb2Bbhfb2Bbhfb2Bbhfb.pack(_x.linSpeed.data, _x.angSpeed.data, _x.LF_motor_enable.data, _x.LF_motor_dir.data, _x.LF_servo_angle.data, _x.LF_servo_cmd.data, _x.LF_wheel_rpm.data, _x.LF_motor_signal.data, _x.RF_motor_enable.data, _x.RF_motor_dir.data, _x.RF_servo_angle.data, _x.RF_servo_cmd.data, _x.RF_wheel_rpm.data, _x.RF_motor_signal.data, _x.LR_motor_enable.data, _x.LR_motor_dir.data, _x.LR_servo_angle.data, _x.LR_servo_cmd.data, _x.LR_wheel_rpm.data, _x.LR_motor_signal.data, _x.RR_motor_enable.data, _x.RR_motor_dir.data, _x.RR_servo_angle.data, _x.RR_servo_cmd.data, _x.RR_wheel_rpm.data, _x.RR_motor_signal.data))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.linSpeed is None:
        self.linSpeed = std_msgs.msg.Float32()
      if self.angSpeed is None:
        self.angSpeed = std_msgs.msg.Float32()
      if self.LF_motor_enable is None:
        self.LF_motor_enable = std_msgs.msg.Bool()
      if self.LF_motor_dir is None:
        self.LF_motor_dir = std_msgs.msg.Bool()
      if self.LF_servo_angle is None:
        self.LF_servo_angle = std_msgs.msg.Int8()
      if self.LF_servo_cmd is None:
        self.LF_servo_cmd = std_msgs.msg.Int16()
      if self.LF_wheel_rpm is None:
        self.LF_wheel_rpm = std_msgs.msg.Float32()
      if self.LF_motor_signal is None:
        self.LF_motor_signal = std_msgs.msg.Int8()
      if self.RF_motor_enable is None:
        self.RF_motor_enable = std_msgs.msg.Bool()
      if self.RF_motor_dir is None:
        self.RF_motor_dir = std_msgs.msg.Bool()
      if self.RF_servo_angle is None:
        self.RF_servo_angle = std_msgs.msg.Int8()
      if self.RF_servo_cmd is None:
        self.RF_servo_cmd = std_msgs.msg.Int16()
      if self.RF_wheel_rpm is None:
        self.RF_wheel_rpm = std_msgs.msg.Float32()
      if self.RF_motor_signal is None:
        self.RF_motor_signal = std_msgs.msg.Int8()
      if self.LR_motor_enable is None:
        self.LR_motor_enable = std_msgs.msg.Bool()
      if self.LR_motor_dir is None:
        self.LR_motor_dir = std_msgs.msg.Bool()
      if self.LR_servo_angle is None:
        self.LR_servo_angle = std_msgs.msg.Int8()
      if self.LR_servo_cmd is None:
        self.LR_servo_cmd = std_msgs.msg.Int16()
      if self.LR_wheel_rpm is None:
        self.LR_wheel_rpm = std_msgs.msg.Float32()
      if self.LR_motor_signal is None:
        self.LR_motor_signal = std_msgs.msg.Int8()
      if self.RR_motor_enable is None:
        self.RR_motor_enable = std_msgs.msg.Bool()
      if self.RR_motor_dir is None:
        self.RR_motor_dir = std_msgs.msg.Bool()
      if self.RR_servo_angle is None:
        self.RR_servo_angle = std_msgs.msg.Int8()
      if self.RR_servo_cmd is None:
        self.RR_servo_cmd = std_msgs.msg.Int16()
      if self.RR_wheel_rpm is None:
        self.RR_wheel_rpm = std_msgs.msg.Float32()
      if self.RR_motor_signal is None:
        self.RR_motor_signal = std_msgs.msg.Int8()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.linSpeed.data, _x.angSpeed.data, _x.LF_motor_enable.data, _x.LF_motor_dir.data, _x.LF_servo_angle.data, _x.LF_servo_cmd.data, _x.LF_wheel_rpm.data, _x.LF_motor_signal.data, _x.RF_motor_enable.data, _x.RF_motor_dir.data, _x.RF_servo_angle.data, _x.RF_servo_cmd.data, _x.RF_wheel_rpm.data, _x.RF_motor_signal.data, _x.LR_motor_enable.data, _x.LR_motor_dir.data, _x.LR_servo_angle.data, _x.LR_servo_cmd.data, _x.LR_wheel_rpm.data, _x.LR_motor_signal.data, _x.RR_motor_enable.data, _x.RR_motor_dir.data, _x.RR_servo_angle.data, _x.RR_servo_cmd.data, _x.RR_wheel_rpm.data, _x.RR_motor_signal.data,) = _struct_2f2Bbhfb2Bbhfb2Bbhfb2Bbhfb.unpack(str[start:end])
      self.LF_motor_enable.data = bool(self.LF_motor_enable.data)
      self.LF_motor_dir.data = bool(self.LF_motor_dir.data)
      self.RF_motor_enable.data = bool(self.RF_motor_enable.data)
      self.RF_motor_dir.data = bool(self.RF_motor_dir.data)
      self.LR_motor_enable.data = bool(self.LR_motor_enable.data)
      self.LR_motor_dir.data = bool(self.LR_motor_dir.data)
      self.RR_motor_enable.data = bool(self.RR_motor_enable.data)
      self.RR_motor_dir.data = bool(self.RR_motor_dir.data)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_2f2Bbhfb2Bbhfb2Bbhfb2Bbhfb = struct.Struct("<2f2Bbhfb2Bbhfb2Bbhfb2Bbhfb")
