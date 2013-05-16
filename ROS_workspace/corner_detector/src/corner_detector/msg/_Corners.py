"""autogenerated by genpy from corner_detector/Corners.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Corners(genpy.Message):
  _md5sum = "939ad33e83c6aaa3351a308edd81ceb9"
  _type = "corner_detector/Corners"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32[] LR_corner
uint32[] RR_corner
uint32[] LF_corner
uint32[] RF_corner
float32 resolution
uint32 width
uint32 height
bool left
"""
  __slots__ = ['LR_corner','RR_corner','LF_corner','RF_corner','resolution','width','height','left']
  _slot_types = ['uint32[]','uint32[]','uint32[]','uint32[]','float32','uint32','uint32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       LR_corner,RR_corner,LF_corner,RF_corner,resolution,width,height,left

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Corners, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.LR_corner is None:
        self.LR_corner = []
      if self.RR_corner is None:
        self.RR_corner = []
      if self.LF_corner is None:
        self.LF_corner = []
      if self.RF_corner is None:
        self.RF_corner = []
      if self.resolution is None:
        self.resolution = 0.
      if self.width is None:
        self.width = 0
      if self.height is None:
        self.height = 0
      if self.left is None:
        self.left = False
    else:
      self.LR_corner = []
      self.RR_corner = []
      self.LF_corner = []
      self.RF_corner = []
      self.resolution = 0.
      self.width = 0
      self.height = 0
      self.left = False

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
      length = len(self.LR_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.LR_corner))
      length = len(self.RR_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.RR_corner))
      length = len(self.LF_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.LF_corner))
      length = len(self.RF_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.RF_corner))
      _x = self
      buff.write(_struct_f2IB.pack(_x.resolution, _x.width, _x.height, _x.left))
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
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.LR_corner = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.RR_corner = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.LF_corner = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.RF_corner = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 13
      (_x.resolution, _x.width, _x.height, _x.left,) = _struct_f2IB.unpack(str[start:end])
      self.left = bool(self.left)
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
      length = len(self.LR_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.LR_corner.tostring())
      length = len(self.RR_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.RR_corner.tostring())
      length = len(self.LF_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.LF_corner.tostring())
      length = len(self.RF_corner)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.RF_corner.tostring())
      _x = self
      buff.write(_struct_f2IB.pack(_x.resolution, _x.width, _x.height, _x.left))
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
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.LR_corner = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.RR_corner = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.LF_corner = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.RF_corner = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      _x = self
      start = end
      end += 13
      (_x.resolution, _x.width, _x.height, _x.left,) = _struct_f2IB.unpack(str[start:end])
      self.left = bool(self.left)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f2IB = struct.Struct("<f2IB")