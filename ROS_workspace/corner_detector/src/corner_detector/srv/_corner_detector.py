"""autogenerated by genpy from corner_detector/corner_detectorRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import nav_msgs.msg
import genpy
import std_msgs.msg

class corner_detectorRequest(genpy.Message):
  _md5sum = "4a6812bd49a91eb54a1ed172b05d9359"
  _type = "corner_detector/corner_detectorRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
nav_msgs/MapMetaData map_meta
nav_msgs/OccupancyGrid map

================================================================================
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

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

"""
  __slots__ = ['map_meta','map']
  _slot_types = ['nav_msgs/MapMetaData','nav_msgs/OccupancyGrid']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       map_meta,map

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(corner_detectorRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.map_meta is None:
        self.map_meta = nav_msgs.msg.MapMetaData()
      if self.map is None:
        self.map = nav_msgs.msg.OccupancyGrid()
    else:
      self.map_meta = nav_msgs.msg.MapMetaData()
      self.map = nav_msgs.msg.OccupancyGrid()

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
      buff.write(_struct_2If2I7d3I.pack(_x.map_meta.map_load_time.secs, _x.map_meta.map_load_time.nsecs, _x.map_meta.resolution, _x.map_meta.width, _x.map_meta.height, _x.map_meta.origin.position.x, _x.map_meta.origin.position.y, _x.map_meta.origin.position.z, _x.map_meta.origin.orientation.x, _x.map_meta.origin.orientation.y, _x.map_meta.origin.orientation.z, _x.map_meta.origin.orientation.w, _x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs))
      _x = self.map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2If2I7d.pack(_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w))
      length = len(self.map.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.map.data))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.map_meta is None:
        self.map_meta = nav_msgs.msg.MapMetaData()
      if self.map is None:
        self.map = nav_msgs.msg.OccupancyGrid()
      end = 0
      _x = self
      start = end
      end += 88
      (_x.map_meta.map_load_time.secs, _x.map_meta.map_load_time.nsecs, _x.map_meta.resolution, _x.map_meta.width, _x.map_meta.height, _x.map_meta.origin.position.x, _x.map_meta.origin.position.y, _x.map_meta.origin.position.z, _x.map_meta.origin.orientation.x, _x.map_meta.origin.orientation.y, _x.map_meta.origin.orientation.z, _x.map_meta.origin.orientation.w, _x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs,) = _struct_2If2I7d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w,) = _struct_2If2I7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.map.data = struct.unpack(pattern, str[start:end])
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
      buff.write(_struct_2If2I7d3I.pack(_x.map_meta.map_load_time.secs, _x.map_meta.map_load_time.nsecs, _x.map_meta.resolution, _x.map_meta.width, _x.map_meta.height, _x.map_meta.origin.position.x, _x.map_meta.origin.position.y, _x.map_meta.origin.position.z, _x.map_meta.origin.orientation.x, _x.map_meta.origin.orientation.y, _x.map_meta.origin.orientation.z, _x.map_meta.origin.orientation.w, _x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs))
      _x = self.map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2If2I7d.pack(_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w))
      length = len(self.map.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.map.data.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.map_meta is None:
        self.map_meta = nav_msgs.msg.MapMetaData()
      if self.map is None:
        self.map = nav_msgs.msg.OccupancyGrid()
      end = 0
      _x = self
      start = end
      end += 88
      (_x.map_meta.map_load_time.secs, _x.map_meta.map_load_time.nsecs, _x.map_meta.resolution, _x.map_meta.width, _x.map_meta.height, _x.map_meta.origin.position.x, _x.map_meta.origin.position.y, _x.map_meta.origin.position.z, _x.map_meta.origin.orientation.x, _x.map_meta.origin.orientation.y, _x.map_meta.origin.orientation.z, _x.map_meta.origin.orientation.w, _x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs,) = _struct_2If2I7d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w,) = _struct_2If2I7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.map.data = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2If2I7d3I = struct.Struct("<2If2I7d3I")
_struct_2If2I7d = struct.Struct("<2If2I7d")
"""autogenerated by genpy from corner_detector/corner_detectorResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class corner_detectorResponse(genpy.Message):
  _md5sum = "b8f0d4aa6433aa8e2d7d6e5f1ee7dcb6"
  _type = "corner_detector/corner_detectorResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
float32[] lower_left
float32[] lower_right
float32[] top_left
float32[] top_right



"""
  __slots__ = ['lower_left','lower_right','top_left','top_right']
  _slot_types = ['float32[]','float32[]','float32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lower_left,lower_right,top_left,top_right

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(corner_detectorResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.lower_left is None:
        self.lower_left = []
      if self.lower_right is None:
        self.lower_right = []
      if self.top_left is None:
        self.top_left = []
      if self.top_right is None:
        self.top_right = []
    else:
      self.lower_left = []
      self.lower_right = []
      self.top_left = []
      self.top_right = []

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
      length = len(self.lower_left)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.lower_left))
      length = len(self.lower_right)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.lower_right))
      length = len(self.top_left)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.top_left))
      length = len(self.top_right)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.top_right))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.lower_left = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.lower_right = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.top_left = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.top_right = struct.unpack(pattern, str[start:end])
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
      length = len(self.lower_left)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.lower_left.tostring())
      length = len(self.lower_right)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.lower_right.tostring())
      length = len(self.top_left)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.top_left.tostring())
      length = len(self.top_right)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.top_right.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.lower_left = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.lower_right = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.top_left = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.top_right = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
class corner_detector(object):
  _type          = 'corner_detector/corner_detector'
  _md5sum = '6ab07915844f78d653bb02cb6aaed405'
  _request_class  = corner_detectorRequest
  _response_class = corner_detectorResponse