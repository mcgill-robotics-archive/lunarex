; Auto-generated. Do not edit!


(cl:in-package kinect_node-srv)


;//! \htmlinclude kinectSafeDistance-request.msg.html

(cl:defclass <kinectSafeDistance-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type cl:integer
    :initform 0))
)

(cl:defclass kinectSafeDistance-request (<kinectSafeDistance-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <kinectSafeDistance-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'kinectSafeDistance-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinect_node-srv:<kinectSafeDistance-request> is deprecated: use kinect_node-srv:kinectSafeDistance-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <kinectSafeDistance-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinect_node-srv:request-val is deprecated.  Use kinect_node-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <kinectSafeDistance-request>) ostream)
  "Serializes a message object of type '<kinectSafeDistance-request>"
  (cl:let* ((signed (cl:slot-value msg 'request)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <kinectSafeDistance-request>) istream)
  "Deserializes a message object of type '<kinectSafeDistance-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'request) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<kinectSafeDistance-request>)))
  "Returns string type for a service object of type '<kinectSafeDistance-request>"
  "kinect_node/kinectSafeDistanceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'kinectSafeDistance-request)))
  "Returns string type for a service object of type 'kinectSafeDistance-request"
  "kinect_node/kinectSafeDistanceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<kinectSafeDistance-request>)))
  "Returns md5sum for a message object of type '<kinectSafeDistance-request>"
  "08ce175063802de56af0355992d6d2f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'kinectSafeDistance-request)))
  "Returns md5sum for a message object of type 'kinectSafeDistance-request"
  "08ce175063802de56af0355992d6d2f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<kinectSafeDistance-request>)))
  "Returns full string definition for message of type '<kinectSafeDistance-request>"
  (cl:format cl:nil "int32 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'kinectSafeDistance-request)))
  "Returns full string definition for message of type 'kinectSafeDistance-request"
  (cl:format cl:nil "int32 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <kinectSafeDistance-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <kinectSafeDistance-request>))
  "Converts a ROS message object to a list"
  (cl:list 'kinectSafeDistance-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude kinectSafeDistance-response.msg.html

(cl:defclass <kinectSafeDistance-response> (roslisp-msg-protocol:ros-message)
  ((distance
    :reader distance
    :initarg :distance
    :type cl:integer
    :initform 0))
)

(cl:defclass kinectSafeDistance-response (<kinectSafeDistance-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <kinectSafeDistance-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'kinectSafeDistance-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kinect_node-srv:<kinectSafeDistance-response> is deprecated: use kinect_node-srv:kinectSafeDistance-response instead.")))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <kinectSafeDistance-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kinect_node-srv:distance-val is deprecated.  Use kinect_node-srv:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <kinectSafeDistance-response>) ostream)
  "Serializes a message object of type '<kinectSafeDistance-response>"
  (cl:let* ((signed (cl:slot-value msg 'distance)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <kinectSafeDistance-response>) istream)
  "Deserializes a message object of type '<kinectSafeDistance-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'distance) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<kinectSafeDistance-response>)))
  "Returns string type for a service object of type '<kinectSafeDistance-response>"
  "kinect_node/kinectSafeDistanceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'kinectSafeDistance-response)))
  "Returns string type for a service object of type 'kinectSafeDistance-response"
  "kinect_node/kinectSafeDistanceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<kinectSafeDistance-response>)))
  "Returns md5sum for a message object of type '<kinectSafeDistance-response>"
  "08ce175063802de56af0355992d6d2f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'kinectSafeDistance-response)))
  "Returns md5sum for a message object of type 'kinectSafeDistance-response"
  "08ce175063802de56af0355992d6d2f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<kinectSafeDistance-response>)))
  "Returns full string definition for message of type '<kinectSafeDistance-response>"
  (cl:format cl:nil "int32 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'kinectSafeDistance-response)))
  "Returns full string definition for message of type 'kinectSafeDistance-response"
  (cl:format cl:nil "int32 distance~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <kinectSafeDistance-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <kinectSafeDistance-response>))
  "Converts a ROS message object to a list"
  (cl:list 'kinectSafeDistance-response
    (cl:cons ':distance (distance msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'kinectSafeDistance)))
  'kinectSafeDistance-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'kinectSafeDistance)))
  'kinectSafeDistance-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'kinectSafeDistance)))
  "Returns string type for a service object of type '<kinectSafeDistance>"
  "kinect_node/kinectSafeDistance")