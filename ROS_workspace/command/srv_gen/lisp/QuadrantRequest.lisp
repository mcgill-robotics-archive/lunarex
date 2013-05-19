; Auto-generated. Do not edit!


(cl:in-package command-srv)


;//! \htmlinclude QuadrantRequest-request.msg.html

(cl:defclass <QuadrantRequest-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass QuadrantRequest-request (<QuadrantRequest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <QuadrantRequest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'QuadrantRequest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name command-srv:<QuadrantRequest-request> is deprecated: use command-srv:QuadrantRequest-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <QuadrantRequest-request>) ostream)
  "Serializes a message object of type '<QuadrantRequest-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <QuadrantRequest-request>) istream)
  "Deserializes a message object of type '<QuadrantRequest-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<QuadrantRequest-request>)))
  "Returns string type for a service object of type '<QuadrantRequest-request>"
  "command/QuadrantRequestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QuadrantRequest-request)))
  "Returns string type for a service object of type 'QuadrantRequest-request"
  "command/QuadrantRequestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<QuadrantRequest-request>)))
  "Returns md5sum for a message object of type '<QuadrantRequest-request>"
  "eca501e934cd757be612cae2f964dc45")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'QuadrantRequest-request)))
  "Returns md5sum for a message object of type 'QuadrantRequest-request"
  "eca501e934cd757be612cae2f964dc45")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<QuadrantRequest-request>)))
  "Returns full string definition for message of type '<QuadrantRequest-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'QuadrantRequest-request)))
  "Returns full string definition for message of type 'QuadrantRequest-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <QuadrantRequest-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <QuadrantRequest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'QuadrantRequest-request
))
;//! \htmlinclude QuadrantRequest-response.msg.html

(cl:defclass <QuadrantRequest-response> (roslisp-msg-protocol:ros-message)
  ((quadrant
    :reader quadrant
    :initarg :quadrant
    :type cl:fixnum
    :initform 0))
)

(cl:defclass QuadrantRequest-response (<QuadrantRequest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <QuadrantRequest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'QuadrantRequest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name command-srv:<QuadrantRequest-response> is deprecated: use command-srv:QuadrantRequest-response instead.")))

(cl:ensure-generic-function 'quadrant-val :lambda-list '(m))
(cl:defmethod quadrant-val ((m <QuadrantRequest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader command-srv:quadrant-val is deprecated.  Use command-srv:quadrant instead.")
  (quadrant m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <QuadrantRequest-response>) ostream)
  "Serializes a message object of type '<QuadrantRequest-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'quadrant)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <QuadrantRequest-response>) istream)
  "Deserializes a message object of type '<QuadrantRequest-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'quadrant)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<QuadrantRequest-response>)))
  "Returns string type for a service object of type '<QuadrantRequest-response>"
  "command/QuadrantRequestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QuadrantRequest-response)))
  "Returns string type for a service object of type 'QuadrantRequest-response"
  "command/QuadrantRequestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<QuadrantRequest-response>)))
  "Returns md5sum for a message object of type '<QuadrantRequest-response>"
  "eca501e934cd757be612cae2f964dc45")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'QuadrantRequest-response)))
  "Returns md5sum for a message object of type 'QuadrantRequest-response"
  "eca501e934cd757be612cae2f964dc45")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<QuadrantRequest-response>)))
  "Returns full string definition for message of type '<QuadrantRequest-response>"
  (cl:format cl:nil "uint8 quadrant~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'QuadrantRequest-response)))
  "Returns full string definition for message of type 'QuadrantRequest-response"
  (cl:format cl:nil "uint8 quadrant~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <QuadrantRequest-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <QuadrantRequest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'QuadrantRequest-response
    (cl:cons ':quadrant (quadrant msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'QuadrantRequest)))
  'QuadrantRequest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'QuadrantRequest)))
  'QuadrantRequest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QuadrantRequest)))
  "Returns string type for a service object of type '<QuadrantRequest>"
  "command/QuadrantRequest")