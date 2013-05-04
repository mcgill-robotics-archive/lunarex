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
  "9720d9672632fb40037b88dcefe05516")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'corner_detector-request)))
  "Returns md5sum for a message object of type 'corner_detector-request"
  "9720d9672632fb40037b88dcefe05516")
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
  ((left_bottom_corner
    :reader left_bottom_corner
    :initarg :left_bottom_corner
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (right_bottom_corner
    :reader right_bottom_corner
    :initarg :right_bottom_corner
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (left_top_corner
    :reader left_top_corner
    :initarg :left_top_corner
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (right_top_corner
    :reader right_top_corner
    :initarg :right_top_corner
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass corner_detector-response (<corner_detector-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <corner_detector-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'corner_detector-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name corner_detector-srv:<corner_detector-response> is deprecated: use corner_detector-srv:corner_detector-response instead.")))

(cl:ensure-generic-function 'left_bottom_corner-val :lambda-list '(m))
(cl:defmethod left_bottom_corner-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:left_bottom_corner-val is deprecated.  Use corner_detector-srv:left_bottom_corner instead.")
  (left_bottom_corner m))

(cl:ensure-generic-function 'right_bottom_corner-val :lambda-list '(m))
(cl:defmethod right_bottom_corner-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:right_bottom_corner-val is deprecated.  Use corner_detector-srv:right_bottom_corner instead.")
  (right_bottom_corner m))

(cl:ensure-generic-function 'left_top_corner-val :lambda-list '(m))
(cl:defmethod left_top_corner-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:left_top_corner-val is deprecated.  Use corner_detector-srv:left_top_corner instead.")
  (left_top_corner m))

(cl:ensure-generic-function 'right_top_corner-val :lambda-list '(m))
(cl:defmethod right_top_corner-val ((m <corner_detector-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-srv:right_top_corner-val is deprecated.  Use corner_detector-srv:right_top_corner instead.")
  (right_top_corner m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <corner_detector-response>) ostream)
  "Serializes a message object of type '<corner_detector-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'left_bottom_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'left_bottom_corner))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'right_bottom_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'right_bottom_corner))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'left_top_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'left_top_corner))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'right_top_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'right_top_corner))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <corner_detector-response>) istream)
  "Deserializes a message object of type '<corner_detector-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'left_bottom_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'left_bottom_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'right_bottom_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'right_bottom_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'left_top_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'left_top_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'right_top_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'right_top_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
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
  "9720d9672632fb40037b88dcefe05516")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'corner_detector-response)))
  "Returns md5sum for a message object of type 'corner_detector-response"
  "9720d9672632fb40037b88dcefe05516")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<corner_detector-response>)))
  "Returns full string definition for message of type '<corner_detector-response>"
  (cl:format cl:nil "~%uint32[] left_bottom_corner~%uint32[] right_bottom_corner~%uint32[] left_top_corner~%uint32[] right_top_corner~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'corner_detector-response)))
  "Returns full string definition for message of type 'corner_detector-response"
  (cl:format cl:nil "~%uint32[] left_bottom_corner~%uint32[] right_bottom_corner~%uint32[] left_top_corner~%uint32[] right_top_corner~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <corner_detector-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'left_bottom_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'right_bottom_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'left_top_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'right_top_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <corner_detector-response>))
  "Converts a ROS message object to a list"
  (cl:list 'corner_detector-response
    (cl:cons ':left_bottom_corner (left_bottom_corner msg))
    (cl:cons ':right_bottom_corner (right_bottom_corner msg))
    (cl:cons ':left_top_corner (left_top_corner msg))
    (cl:cons ':right_top_corner (right_top_corner msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'corner_detector)))
  'corner_detector-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'corner_detector)))
  'corner_detector-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'corner_detector)))
  "Returns string type for a service object of type '<corner_detector>"
  "corner_detector/corner_detector")