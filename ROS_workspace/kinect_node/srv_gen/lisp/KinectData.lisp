; Auto-generated. Do not edit!


(cl:in-package kinect_node-srv)


;//! \htmlinclude KinectData-request.msg.html

(cl:defclass <KinectData-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type cl:integer
    :initform 0))
)

(cl:defclass KinectData-request (<KinectData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <KinectData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'KinectData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinect_node-srv:<KinectData-request> is deprecated: use kinect_node-srv:KinectData-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <KinectData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinect_node-srv:request-val is deprecated.  Use kinect_node-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <KinectData-request>) ostream)
  "Serializes a message object of type '<KinectData-request>"
  (cl:let* ((signed (cl:slot-value msg 'request)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <KinectData-request>) istream)
  "Deserializes a message object of type '<KinectData-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'request) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<KinectData-request>)))
  "Returns string type for a service object of type '<KinectData-request>"
  "kinect_node/KinectDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'KinectData-request)))
  "Returns string type for a service object of type 'KinectData-request"
  "kinect_node/KinectDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<KinectData-request>)))
  "Returns md5sum for a message object of type '<KinectData-request>"
  "5eacc836fed57135e6fd765882abe88f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'KinectData-request)))
  "Returns md5sum for a message object of type 'KinectData-request"
  "5eacc836fed57135e6fd765882abe88f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<KinectData-request>)))
  "Returns full string definition for message of type '<KinectData-request>"
  (cl:format cl:nil "int32 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'KinectData-request)))
  "Returns full string definition for message of type 'KinectData-request"
  (cl:format cl:nil "int32 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <KinectData-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <KinectData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'KinectData-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude KinectData-response.msg.html

(cl:defclass <KinectData-response> (roslisp-msg-protocol:ros-message)
  ((height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0)
   (width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0)
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass KinectData-response (<KinectData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <KinectData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'KinectData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinect_node-srv:<KinectData-response> is deprecated: use kinect_node-srv:KinectData-response instead.")))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <KinectData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinect_node-srv:height-val is deprecated.  Use kinect_node-srv:height instead.")
  (height m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <KinectData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinect_node-srv:width-val is deprecated.  Use kinect_node-srv:width instead.")
  (width m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <KinectData-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinect_node-srv:data-val is deprecated.  Use kinect_node-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <KinectData-response>) ostream)
  "Serializes a message object of type '<KinectData-response>"
  (cl:let* ((signed (cl:slot-value msg 'height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <KinectData-response>) istream)
  "Deserializes a message object of type '<KinectData-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<KinectData-response>)))
  "Returns string type for a service object of type '<KinectData-response>"
  "kinect_node/KinectDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'KinectData-response)))
  "Returns string type for a service object of type 'KinectData-response"
  "kinect_node/KinectDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<KinectData-response>)))
  "Returns md5sum for a message object of type '<KinectData-response>"
  "5eacc836fed57135e6fd765882abe88f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'KinectData-response)))
  "Returns md5sum for a message object of type 'KinectData-response"
  "5eacc836fed57135e6fd765882abe88f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<KinectData-response>)))
  "Returns full string definition for message of type '<KinectData-response>"
  (cl:format cl:nil "int32 height~%int32 width~%int32[] data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'KinectData-response)))
  "Returns full string definition for message of type 'KinectData-response"
  (cl:format cl:nil "int32 height~%int32 width~%int32[] data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <KinectData-response>))
  (cl:+ 0
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <KinectData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'KinectData-response
    (cl:cons ':height (height msg))
    (cl:cons ':width (width msg))
    (cl:cons ':data (data msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'KinectData)))
  'KinectData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'KinectData)))
  'KinectData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'KinectData)))
  "Returns string type for a service object of type '<KinectData>"
  "kinect_node/KinectData")