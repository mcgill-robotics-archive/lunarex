; Auto-generated. Do not edit!


(cl:in-package arduino_msgs-msg)


;//! \htmlinclude ArduinoFeedback.msg.html

(cl:defclass <ArduinoFeedback> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (linSpeed
    :reader linSpeed
    :initarg :linSpeed
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (angSpeed
    :reader angSpeed
    :initarg :angSpeed
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
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
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (LF_servo_angle
    :reader LF_servo_angle
    :initarg :LF_servo_angle
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LF_servo_cmd
    :reader LF_servo_cmd
    :initarg :LF_servo_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (RF_motor_enable
    :reader RF_motor_enable
    :initarg :RF_motor_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RF_motor_dir
    :reader RF_motor_dir
    :initarg :RF_motor_dir
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RF_wheel_rpm
    :reader RF_wheel_rpm
    :initarg :RF_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (RF_motor_cmd
    :reader RF_motor_cmd
    :initarg :RF_motor_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (RF_servo_angle
    :reader RF_servo_angle
    :initarg :RF_servo_angle
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (RF_servo_cmd
    :reader RF_servo_cmd
    :initarg :RF_servo_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (LR_motor_enable
    :reader LR_motor_enable
    :initarg :LR_motor_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LR_motor_dir
    :reader LR_motor_dir
    :initarg :LR_motor_dir
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LR_wheel_rpm
    :reader LR_wheel_rpm
    :initarg :LR_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LR_motor_cmd
    :reader LR_motor_cmd
    :initarg :LR_motor_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (LR_servo_angle
    :reader LR_servo_angle
    :initarg :LR_servo_angle
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LR_servo_cmd
    :reader LR_servo_cmd
    :initarg :LR_servo_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (RR_motor_enable
    :reader RR_motor_enable
    :initarg :RR_motor_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RR_motor_dir
    :reader RR_motor_dir
    :initarg :RR_motor_dir
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RR_wheel_rpm
    :reader RR_wheel_rpm
    :initarg :RR_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (RR_motor_cmd
    :reader RR_motor_cmd
    :initarg :RR_motor_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (RR_servo_angle
    :reader RR_servo_angle
    :initarg :RR_servo_angle
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (RR_servo_cmd
    :reader RR_servo_cmd
    :initarg :RR_servo_cmd
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16)))
)

(cl:defclass ArduinoFeedback (<ArduinoFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArduinoFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArduinoFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name arduino_msgs-msg:<ArduinoFeedback> is deprecated: use arduino_msgs-msg:ArduinoFeedback instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:header-val is deprecated.  Use arduino_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'linSpeed-val :lambda-list '(m))
(cl:defmethod linSpeed-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:linSpeed-val is deprecated.  Use arduino_msgs-msg:linSpeed instead.")
  (linSpeed m))

(cl:ensure-generic-function 'angSpeed-val :lambda-list '(m))
(cl:defmethod angSpeed-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:angSpeed-val is deprecated.  Use arduino_msgs-msg:angSpeed instead.")
  (angSpeed m))

(cl:ensure-generic-function 'LF_motor_enable-val :lambda-list '(m))
(cl:defmethod LF_motor_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_enable-val is deprecated.  Use arduino_msgs-msg:LF_motor_enable instead.")
  (LF_motor_enable m))

(cl:ensure-generic-function 'LF_motor_dir-val :lambda-list '(m))
(cl:defmethod LF_motor_dir-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_dir-val is deprecated.  Use arduino_msgs-msg:LF_motor_dir instead.")
  (LF_motor_dir m))

(cl:ensure-generic-function 'LF_wheel_rpm-val :lambda-list '(m))
(cl:defmethod LF_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:LF_wheel_rpm instead.")
  (LF_wheel_rpm m))

(cl:ensure-generic-function 'LF_motor_cmd-val :lambda-list '(m))
(cl:defmethod LF_motor_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_cmd-val is deprecated.  Use arduino_msgs-msg:LF_motor_cmd instead.")
  (LF_motor_cmd m))

(cl:ensure-generic-function 'LF_servo_angle-val :lambda-list '(m))
(cl:defmethod LF_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_servo_angle-val is deprecated.  Use arduino_msgs-msg:LF_servo_angle instead.")
  (LF_servo_angle m))

(cl:ensure-generic-function 'LF_servo_cmd-val :lambda-list '(m))
(cl:defmethod LF_servo_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_servo_cmd-val is deprecated.  Use arduino_msgs-msg:LF_servo_cmd instead.")
  (LF_servo_cmd m))

(cl:ensure-generic-function 'RF_motor_enable-val :lambda-list '(m))
(cl:defmethod RF_motor_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_motor_enable-val is deprecated.  Use arduino_msgs-msg:RF_motor_enable instead.")
  (RF_motor_enable m))

(cl:ensure-generic-function 'RF_motor_dir-val :lambda-list '(m))
(cl:defmethod RF_motor_dir-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_motor_dir-val is deprecated.  Use arduino_msgs-msg:RF_motor_dir instead.")
  (RF_motor_dir m))

(cl:ensure-generic-function 'RF_wheel_rpm-val :lambda-list '(m))
(cl:defmethod RF_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:RF_wheel_rpm instead.")
  (RF_wheel_rpm m))

(cl:ensure-generic-function 'RF_motor_cmd-val :lambda-list '(m))
(cl:defmethod RF_motor_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_motor_cmd-val is deprecated.  Use arduino_msgs-msg:RF_motor_cmd instead.")
  (RF_motor_cmd m))

(cl:ensure-generic-function 'RF_servo_angle-val :lambda-list '(m))
(cl:defmethod RF_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_servo_angle-val is deprecated.  Use arduino_msgs-msg:RF_servo_angle instead.")
  (RF_servo_angle m))

(cl:ensure-generic-function 'RF_servo_cmd-val :lambda-list '(m))
(cl:defmethod RF_servo_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_servo_cmd-val is deprecated.  Use arduino_msgs-msg:RF_servo_cmd instead.")
  (RF_servo_cmd m))

(cl:ensure-generic-function 'LR_motor_enable-val :lambda-list '(m))
(cl:defmethod LR_motor_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_motor_enable-val is deprecated.  Use arduino_msgs-msg:LR_motor_enable instead.")
  (LR_motor_enable m))

(cl:ensure-generic-function 'LR_motor_dir-val :lambda-list '(m))
(cl:defmethod LR_motor_dir-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_motor_dir-val is deprecated.  Use arduino_msgs-msg:LR_motor_dir instead.")
  (LR_motor_dir m))

(cl:ensure-generic-function 'LR_wheel_rpm-val :lambda-list '(m))
(cl:defmethod LR_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:LR_wheel_rpm instead.")
  (LR_wheel_rpm m))

(cl:ensure-generic-function 'LR_motor_cmd-val :lambda-list '(m))
(cl:defmethod LR_motor_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_motor_cmd-val is deprecated.  Use arduino_msgs-msg:LR_motor_cmd instead.")
  (LR_motor_cmd m))

(cl:ensure-generic-function 'LR_servo_angle-val :lambda-list '(m))
(cl:defmethod LR_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_servo_angle-val is deprecated.  Use arduino_msgs-msg:LR_servo_angle instead.")
  (LR_servo_angle m))

(cl:ensure-generic-function 'LR_servo_cmd-val :lambda-list '(m))
(cl:defmethod LR_servo_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_servo_cmd-val is deprecated.  Use arduino_msgs-msg:LR_servo_cmd instead.")
  (LR_servo_cmd m))

(cl:ensure-generic-function 'RR_motor_enable-val :lambda-list '(m))
(cl:defmethod RR_motor_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_motor_enable-val is deprecated.  Use arduino_msgs-msg:RR_motor_enable instead.")
  (RR_motor_enable m))

(cl:ensure-generic-function 'RR_motor_dir-val :lambda-list '(m))
(cl:defmethod RR_motor_dir-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_motor_dir-val is deprecated.  Use arduino_msgs-msg:RR_motor_dir instead.")
  (RR_motor_dir m))

(cl:ensure-generic-function 'RR_wheel_rpm-val :lambda-list '(m))
(cl:defmethod RR_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:RR_wheel_rpm instead.")
  (RR_wheel_rpm m))

(cl:ensure-generic-function 'RR_motor_cmd-val :lambda-list '(m))
(cl:defmethod RR_motor_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_motor_cmd-val is deprecated.  Use arduino_msgs-msg:RR_motor_cmd instead.")
  (RR_motor_cmd m))

(cl:ensure-generic-function 'RR_servo_angle-val :lambda-list '(m))
(cl:defmethod RR_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_servo_angle-val is deprecated.  Use arduino_msgs-msg:RR_servo_angle instead.")
  (RR_servo_angle m))

(cl:ensure-generic-function 'RR_servo_cmd-val :lambda-list '(m))
(cl:defmethod RR_servo_cmd-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_servo_cmd-val is deprecated.  Use arduino_msgs-msg:RR_servo_cmd instead.")
  (RR_servo_cmd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArduinoFeedback>) ostream)
  "Serializes a message object of type '<ArduinoFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'linSpeed) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'angSpeed) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_dir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_servo_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_motor_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_motor_dir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_motor_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_servo_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_motor_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_motor_dir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_motor_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_servo_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_motor_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_motor_dir) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_motor_cmd) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_servo_cmd) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArduinoFeedback>) istream)
  "Deserializes a message object of type '<ArduinoFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'linSpeed) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'angSpeed) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_dir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_servo_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_motor_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_motor_dir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_motor_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_servo_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_motor_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_motor_dir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_motor_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_servo_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_motor_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_motor_dir) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_motor_cmd) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_servo_cmd) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArduinoFeedback>)))
  "Returns string type for a message object of type '<ArduinoFeedback>"
  "arduino_msgs/ArduinoFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArduinoFeedback)))
  "Returns string type for a message object of type 'ArduinoFeedback"
  "arduino_msgs/ArduinoFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArduinoFeedback>)))
  "Returns md5sum for a message object of type '<ArduinoFeedback>"
  "bb6a00989cbfd262c4446155bd168ba0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArduinoFeedback)))
  "Returns md5sum for a message object of type 'ArduinoFeedback"
  "bb6a00989cbfd262c4446155bd168ba0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArduinoFeedback>)))
  "Returns full string definition for message of type '<ArduinoFeedback>"
  (cl:format cl:nil "Header header~%~%std_msgs/Float32 linSpeed~%std_msgs/Float32 angSpeed~%~%std_msgs/Bool LF_motor_enable~%std_msgs/Bool LF_motor_dir~%std_msgs/Float32 LF_wheel_rpm~%std_msgs/Int16 LF_motor_cmd~%~%std_msgs/Float32 LF_servo_angle~%std_msgs/Int16 LF_servo_cmd~%~%~%std_msgs/Bool RF_motor_enable~%std_msgs/Bool RF_motor_dir~%std_msgs/Float32 RF_wheel_rpm~%std_msgs/Int16 RF_motor_cmd~%~%std_msgs/Float32 RF_servo_angle~%std_msgs/Int16 RF_servo_cmd~%~%std_msgs/Bool LR_motor_enable~%std_msgs/Bool LR_motor_dir~%std_msgs/Float32 LR_wheel_rpm~%std_msgs/Int16 LR_motor_cmd~%~%std_msgs/Float32 LR_servo_angle~%std_msgs/Int16 LR_servo_cmd~%~%std_msgs/Bool RR_motor_enable~%std_msgs/Bool RR_motor_dir~%std_msgs/Float32 RR_wheel_rpm~%std_msgs/Int16 RR_motor_cmd~%~%std_msgs/Float32 RR_servo_angle~%std_msgs/Int16 RR_servo_cmd~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/Int16~%int16 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArduinoFeedback)))
  "Returns full string definition for message of type 'ArduinoFeedback"
  (cl:format cl:nil "Header header~%~%std_msgs/Float32 linSpeed~%std_msgs/Float32 angSpeed~%~%std_msgs/Bool LF_motor_enable~%std_msgs/Bool LF_motor_dir~%std_msgs/Float32 LF_wheel_rpm~%std_msgs/Int16 LF_motor_cmd~%~%std_msgs/Float32 LF_servo_angle~%std_msgs/Int16 LF_servo_cmd~%~%~%std_msgs/Bool RF_motor_enable~%std_msgs/Bool RF_motor_dir~%std_msgs/Float32 RF_wheel_rpm~%std_msgs/Int16 RF_motor_cmd~%~%std_msgs/Float32 RF_servo_angle~%std_msgs/Int16 RF_servo_cmd~%~%std_msgs/Bool LR_motor_enable~%std_msgs/Bool LR_motor_dir~%std_msgs/Float32 LR_wheel_rpm~%std_msgs/Int16 LR_motor_cmd~%~%std_msgs/Float32 LR_servo_angle~%std_msgs/Int16 LR_servo_cmd~%~%std_msgs/Bool RR_motor_enable~%std_msgs/Bool RR_motor_dir~%std_msgs/Float32 RR_wheel_rpm~%std_msgs/Int16 RR_motor_cmd~%~%std_msgs/Float32 RR_servo_angle~%std_msgs/Int16 RR_servo_cmd~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/Int16~%int16 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArduinoFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'linSpeed))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'angSpeed))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_dir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_servo_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_motor_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_motor_dir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_motor_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_servo_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_motor_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_motor_dir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_motor_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_servo_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_motor_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_motor_dir))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_motor_cmd))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_servo_cmd))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArduinoFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'ArduinoFeedback
    (cl:cons ':header (header msg))
    (cl:cons ':linSpeed (linSpeed msg))
    (cl:cons ':angSpeed (angSpeed msg))
    (cl:cons ':LF_motor_enable (LF_motor_enable msg))
    (cl:cons ':LF_motor_dir (LF_motor_dir msg))
    (cl:cons ':LF_wheel_rpm (LF_wheel_rpm msg))
    (cl:cons ':LF_motor_cmd (LF_motor_cmd msg))
    (cl:cons ':LF_servo_angle (LF_servo_angle msg))
    (cl:cons ':LF_servo_cmd (LF_servo_cmd msg))
    (cl:cons ':RF_motor_enable (RF_motor_enable msg))
    (cl:cons ':RF_motor_dir (RF_motor_dir msg))
    (cl:cons ':RF_wheel_rpm (RF_wheel_rpm msg))
    (cl:cons ':RF_motor_cmd (RF_motor_cmd msg))
    (cl:cons ':RF_servo_angle (RF_servo_angle msg))
    (cl:cons ':RF_servo_cmd (RF_servo_cmd msg))
    (cl:cons ':LR_motor_enable (LR_motor_enable msg))
    (cl:cons ':LR_motor_dir (LR_motor_dir msg))
    (cl:cons ':LR_wheel_rpm (LR_wheel_rpm msg))
    (cl:cons ':LR_motor_cmd (LR_motor_cmd msg))
    (cl:cons ':LR_servo_angle (LR_servo_angle msg))
    (cl:cons ':LR_servo_cmd (LR_servo_cmd msg))
    (cl:cons ':RR_motor_enable (RR_motor_enable msg))
    (cl:cons ':RR_motor_dir (RR_motor_dir msg))
    (cl:cons ':RR_wheel_rpm (RR_wheel_rpm msg))
    (cl:cons ':RR_motor_cmd (RR_motor_cmd msg))
    (cl:cons ':RR_servo_angle (RR_servo_angle msg))
    (cl:cons ':RR_servo_cmd (RR_servo_cmd msg))
))
