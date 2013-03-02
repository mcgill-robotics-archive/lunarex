; Auto-generated. Do not edit!


(cl:in-package tf_service_test-srv)


;//! \htmlinclude TestSrv-request.msg.html

(cl:defclass <TestSrv-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type cl:integer
    :initform 0))
)

(cl:defclass TestSrv-request (<TestSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TestSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TestSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tf_service_test-srv:<TestSrv-request> is deprecated: use tf_service_test-srv:TestSrv-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <TestSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tf_service_test-srv:request-val is deprecated.  Use tf_service_test-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TestSrv-request>) ostream)
  "Serializes a message object of type '<TestSrv-request>"
  (cl:let* ((signed (cl:slot-value msg 'request)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TestSrv-request>) istream)
  "Deserializes a message object of type '<TestSrv-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'request) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TestSrv-request>)))
  "Returns string type for a service object of type '<TestSrv-request>"
  "tf_service_test/TestSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TestSrv-request)))
  "Returns string type for a service object of type 'TestSrv-request"
  "tf_service_test/TestSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TestSrv-request>)))
  "Returns md5sum for a message object of type '<TestSrv-request>"
  "57e40f56f94dc9c5c0bad06f1ba3cdc3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TestSrv-request)))
  "Returns md5sum for a message object of type 'TestSrv-request"
  "57e40f56f94dc9c5c0bad06f1ba3cdc3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TestSrv-request>)))
  "Returns full string definition for message of type '<TestSrv-request>"
  (cl:format cl:nil "int32 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TestSrv-request)))
  "Returns full string definition for message of type 'TestSrv-request"
  (cl:format cl:nil "int32 request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TestSrv-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TestSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TestSrv-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude TestSrv-response.msg.html

(cl:defclass <TestSrv-response> (roslisp-msg-protocol:ros-message)
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
   (kinect_map
    :reader kinect_map
    :initarg :kinect_map
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass TestSrv-response (<TestSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TestSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TestSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tf_service_test-srv:<TestSrv-response> is deprecated: use tf_service_test-srv:TestSrv-response instead.")))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <TestSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tf_service_test-srv:height-val is deprecated.  Use tf_service_test-srv:height instead.")
  (height m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <TestSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tf_service_test-srv:width-val is deprecated.  Use tf_service_test-srv:width instead.")
  (width m))

(cl:ensure-generic-function 'kinect_map-val :lambda-list '(m))
(cl:defmethod kinect_map-val ((m <TestSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tf_service_test-srv:kinect_map-val is deprecated.  Use tf_service_test-srv:kinect_map instead.")
  (kinect_map m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TestSrv-response>) ostream)
  "Serializes a message object of type '<TestSrv-response>"
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
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'kinect_map))))
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
   (cl:slot-value msg 'kinect_map))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TestSrv-response>) istream)
  "Deserializes a message object of type '<TestSrv-response>"
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
  (cl:setf (cl:slot-value msg 'kinect_map) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'kinect_map)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TestSrv-response>)))
  "Returns string type for a service object of type '<TestSrv-response>"
  "tf_service_test/TestSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TestSrv-response)))
  "Returns string type for a service object of type 'TestSrv-response"
  "tf_service_test/TestSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TestSrv-response>)))
  "Returns md5sum for a message object of type '<TestSrv-response>"
  "57e40f56f94dc9c5c0bad06f1ba3cdc3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TestSrv-response)))
  "Returns md5sum for a message object of type 'TestSrv-response"
  "57e40f56f94dc9c5c0bad06f1ba3cdc3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TestSrv-response>)))
  "Returns full string definition for message of type '<TestSrv-response>"
  (cl:format cl:nil "int32 height~%int32 width~%int32[] kinect_map~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TestSrv-response)))
  "Returns full string definition for message of type 'TestSrv-response"
  (cl:format cl:nil "int32 height~%int32 width~%int32[] kinect_map~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TestSrv-response>))
  (cl:+ 0
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'kinect_map) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TestSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TestSrv-response
    (cl:cons ':height (height msg))
    (cl:cons ':width (width msg))
    (cl:cons ':kinect_map (kinect_map msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TestSrv)))
  'TestSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TestSrv)))
  'TestSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TestSrv)))
  "Returns string type for a service object of type '<TestSrv>"
  "tf_service_test/TestSrv")