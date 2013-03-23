; Auto-generated. Do not edit!


(cl:in-package corner_detector-srv)


;//! \htmlinclude corner_detector-request.msg.html

(cl:defclass <corner_detector-request> (roslisp-msg-protocol:ros-message)
  ((map_meta
    :reader map_meta
    :initarg :map_meta
    :type nav_msgs-msg:MapMetaData
    :initform (cl:make-instance 'nav_msgs-msg:MapMetaData))
   (map
    :reader map
    :initarg :map
    :type nav_msgs-msg:OccupancyGrid
    :initform (cl:make-instance 'nav_msgs-msg:OccupancyGrid)))
)

(cl:defclass corner_detector-request (<corner_detector-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <corner_detector-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'corner_detector-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name corner_detector-srv:<corner_detector-request> is deprecated: use corner_detector-srv:corner_detector-request instead.")))

(cl:ensure-generic-function 'map_meta-val :lambda-list '(m))
(cl:defmethod map_meta-val ((m <corner_detector-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:map_meta-val is deprecated.  Use corner_detector-srv:map_meta instead.")
  (map_meta m))

(cl:ensure-generic-function 'map-val :lambda-list '(m))
(cl:defmethod map-val ((m <corner_detector-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:map-val is deprecated.  Use corner_detector-srv:map instead.")
  (map m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <corner_detector-request>) ostream)
  "Serializes a message object of type '<corner_detector-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'map_meta) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'map) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <corner_detector-request>) istream)
  "Deserializes a message object of type '<corner_detector-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'map_meta) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'map) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<corner_detector-request>)))
  "Returns string type for a service object of type '<corner_detector-request>"
  "corner_detector/corner_detectorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'corner_detector-request)))
  "Returns string type for a service object of type 'corner_detector-request"
  "corner_detector/corner_detectorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<corner_detector-request>)))
  "Returns md5sum for a message object of type '<corner_detector-request>"
  "6ab07915844f78d653bb02cb6aaed405")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'corner_detector-request)))
  "Returns md5sum for a message object of type 'corner_detector-request"
  "6ab07915844f78d653bb02cb6aaed405")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<corner_detector-request>)))
  "Returns full string definition for message of type '<corner_detector-request>"
  (cl:format cl:nil "~%nav_msgs/MapMetaData map_meta~%nav_msgs/OccupancyGrid map~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'corner_detector-request)))
  "Returns full string definition for message of type 'corner_detector-request"
  (cl:format cl:nil "~%nav_msgs/MapMetaData map_meta~%nav_msgs/OccupancyGrid map~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <corner_detector-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'map_meta))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'map))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <corner_detector-request>))
  "Converts a ROS message object to a list"
  (cl:list 'corner_detector-request
    (cl:cons ':map_meta (map_meta msg))
    (cl:cons ':map (map msg))
))
;//! \htmlinclude corner_detector-response.msg.html

(cl:defclass <corner_detector-response> (roslisp-msg-protocol:ros-message)
  ((lower_left
    :reader lower_left
    :initarg :lower_left
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (lower_right
    :reader lower_right
    :initarg :lower_right
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (top_left
    :reader top_left
    :initarg :top_left
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (top_right
    :reader top_right
    :initarg :top_right
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass corner_detector-response (<corner_detector-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <corner_detector-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'corner_detector-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name corner_detector-srv:<corner_detector-response> is deprecated: use corner_detector-srv:corner_detector-response instead.")))

(cl:ensure-generic-function 'lower_left-val :lambda-list '(m))
(cl:defmethod lower_left-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:lower_left-val is deprecated.  Use corner_detector-srv:lower_left instead.")
  (lower_left m))

(cl:ensure-generic-function 'lower_right-val :lambda-list '(m))
(cl:defmethod lower_right-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:lower_right-val is deprecated.  Use corner_detector-srv:lower_right instead.")
  (lower_right m))

(cl:ensure-generic-function 'top_left-val :lambda-list '(m))
(cl:defmethod top_left-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:top_left-val is deprecated.  Use corner_detector-srv:top_left instead.")
  (top_left m))

(cl:ensure-generic-function 'top_right-val :lambda-list '(m))
(cl:defmethod top_right-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:top_right-val is deprecated.  Use corner_detector-srv:top_right instead.")
  (top_right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <corner_detector-response>) ostream)
  "Serializes a message object of type '<corner_detector-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'lower_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'lower_left))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'lower_right))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'lower_right))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'top_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'top_left))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'top_right))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'top_right))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <corner_detector-response>) istream)
  "Deserializes a message object of type '<corner_detector-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'lower_left) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'lower_left)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'lower_right) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'lower_right)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'top_left) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'top_left)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'top_right) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'top_right)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<corner_detector-response>)))
  "Returns string type for a service object of type '<corner_detector-response>"
  "corner_detector/corner_detectorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'corner_detector-response)))
  "Returns string type for a service object of type 'corner_detector-response"
  "corner_detector/corner_detectorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<corner_detector-response>)))
  "Returns md5sum for a message object of type '<corner_detector-response>"
  "6ab07915844f78d653bb02cb6aaed405")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'corner_detector-response)))
  "Returns md5sum for a message object of type 'corner_detector-response"
  "6ab07915844f78d653bb02cb6aaed405")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<corner_detector-response>)))
  "Returns full string definition for message of type '<corner_detector-response>"
  (cl:format cl:nil "~%float32[] lower_left~%float32[] lower_right~%float32[] top_left~%float32[] top_right~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'corner_detector-response)))
  "Returns full string definition for message of type 'corner_detector-response"
  (cl:format cl:nil "~%float32[] lower_left~%float32[] lower_right~%float32[] top_left~%float32[] top_right~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <corner_detector-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'lower_left) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'lower_right) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'top_left) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'top_right) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <corner_detector-response>))
  "Converts a ROS message object to a list"
  (cl:list 'corner_detector-response
    (cl:cons ':lower_left (lower_left msg))
    (cl:cons ':lower_right (lower_right msg))
    (cl:cons ':top_left (top_left msg))
    (cl:cons ':top_right (top_right msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'corner_detector)))
  'corner_detector-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'corner_detector)))
  'corner_detector-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'corner_detector)))
  "Returns string type for a service object of type '<corner_detector>"
  "corner_detector/corner_detector")