; Auto-generated. Do not edit!


(cl:in-package arduino_msgs-msg)


;//! \htmlinclude LiteArduinoFeedback.msg.html

(cl:defclass <LiteArduinoFeedback> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (LF_motor_enable
    :reader LF_motor_enable
    :initarg :LF_motor_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LF_motor_dir
    :reader LF_motor_dir
    :initarg :LF_motor_dir
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LF_wheel_rpm
    :reader LF_wheel_rpm
    :initarg :LF_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LF_motor_cmd
    :reader LF_motor_cmd
    :initarg :LF_motor_cmd
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (LF_servo_angle
    :reader LF_servo_angle
    :initarg :LF_servo_angle
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LF_servo_cmd
    :reader LF_servo_cmd
    :initarg :LF_servo_cmd
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8)))
)

(cl:defclass LiteArduinoFeedback (<LiteArduinoFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LiteArduinoFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LiteArduinoFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name arduino_msgs-msg:<LiteArduinoFeedback> is deprecated: use arduino_msgs-msg:LiteArduinoFeedback instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:header-val is deprecated.  Use arduino_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'LF_motor_enable-val :lambda-list '(m))
(cl:defmethod LF_motor_enable-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_enable-val is deprecated.  Use arduino_msgs-msg:LF_motor_enable instead.")
  (LF_motor_enable m))

(cl:ensure-generic-function 'LF_motor_dir-val :lambda-list '(m))
(cl:defmethod LF_motor_dir-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_dir-val is deprecated.  Use arduino_msgs-msg:LF_motor_dir instead.")
  (LF_motor_dir m))

(cl:ensure-generic-function 'LF_wheel_rpm-val :lambda-list '(m))
(cl:defmethod LF_wheel_rpm-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:LF_wheel_rpm instead.")
  (LF_wheel_rpm m))

(cl:ensure-generic-function 'LF_motor_cmd-val :lambda-list '(m))
(cl:defmethod LF_motor_cmd-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_cmd-val is deprecated.  Use arduino_msgs-msg:LF_motor_cmd instead.")
  (LF_motor_cmd m))

(cl:ensure-generic-function 'LF_servo_angle-val :lambda-list '(m))
(cl:defmethod LF_servo_angle-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_servo_angle-val is deprecated.  Use arduino_msgs-msg:LF_servo_angle instead.")
  (LF_servo_angle m))

(cl:ensure-generic-function 'LF_servo_cmd-val :lambda-list '(m))
(cl:defmethod LF_servo_cmd-val ((m <LiteArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_servo_cmd-val is deprecated.  Use arduino_msgs-msg:LF_servo_cmd instead.")
  (LF_servo_cmd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LiteArduinoFeedback>) ostream)
  "Serializes a message object of type '<LiteArduinoFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_dir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_servo_cmd) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LiteArduinoFeedback>) istream)
  "Deserializes a message object of type '<LiteArduinoFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_dir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_servo_cmd) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LiteArduinoFeedback>)))
  "Returns string type for a message object of type '<LiteArduinoFeedback>"
  "arduino_msgs/LiteArduinoFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LiteArduinoFeedback)))
  "Returns string type for a message object of type 'LiteArduinoFeedback"
  "arduino_msgs/LiteArduinoFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LiteArduinoFeedback>)))
  "Returns md5sum for a message object of type '<LiteArduinoFeedback>"
  "0ddc16df7b8b5e66b3f5a490e721c6f0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LiteArduinoFeedback)))
  "Returns md5sum for a message object of type 'LiteArduinoFeedback"
  "0ddc16df7b8b5e66b3f5a490e721c6f0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LiteArduinoFeedback>)))
  "Returns full string definition for message of type '<LiteArduinoFeedback>"
  (cl:format cl:nil "Header header~%~%std_msgs/Bool LF_motor_enable~%std_msgs/Bool LF_motor_dir~%std_msgs/Float32 LF_wheel_rpm~%std_msgs/Int8 LF_motor_cmd~%~%std_msgs/Float32 LF_servo_angle~%std_msgs/Int8 LF_servo_cmd~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%================================================================================~%MSG: std_msgs/Int8~%int8 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LiteArduinoFeedback)))
  "Returns full string definition for message of type 'LiteArduinoFeedback"
  (cl:format cl:nil "Header header~%~%std_msgs/Bool LF_motor_enable~%std_msgs/Bool LF_motor_dir~%std_msgs/Float32 LF_wheel_rpm~%std_msgs/Int8 LF_motor_cmd~%~%std_msgs/Float32 LF_servo_angle~%std_msgs/Int8 LF_servo_cmd~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%================================================================================~%MSG: std_msgs/Int8~%int8 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LiteArduinoFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_dir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_servo_cmd))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LiteArduinoFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'LiteArduinoFeedback
    (cl:cons ':header (header msg))
    (cl:cons ':LF_motor_enable (LF_motor_enable msg))
    (cl:cons ':LF_motor_dir (LF_motor_dir msg))
    (cl:cons ':LF_wheel_rpm (LF_wheel_rpm msg))
    (cl:cons ':LF_motor_cmd (LF_motor_cmd msg))
    (cl:cons ':LF_servo_angle (LF_servo_angle msg))
    (cl:cons ':LF_servo_cmd (LF_servo_cmd msg))
))
