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
   (LF_enable
    :reader LF_enable
    :initarg :LF_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LF_direction
    :reader LF_direction
    :initarg :LF_direction
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LF_servo_angle
    :reader LF_servo_angle
    :initarg :LF_servo_angle
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (LF_servo_pwm
    :reader LF_servo_pwm
    :initarg :LF_servo_pwm
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (LF_wheel_rpm
    :reader LF_wheel_rpm
    :initarg :LF_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LF_motor_signal
    :reader LF_motor_signal
    :initarg :LF_motor_signal
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (RF_enable
    :reader RF_enable
    :initarg :RF_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RF_direction
    :reader RF_direction
    :initarg :RF_direction
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RF_servo_angle
    :reader RF_servo_angle
    :initarg :RF_servo_angle
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (RF_servo_pwm
    :reader RF_servo_pwm
    :initarg :RF_servo_pwm
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (RF_wheel_rpm
    :reader RF_wheel_rpm
    :initarg :RF_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (RF_motor_signal
    :reader RF_motor_signal
    :initarg :RF_motor_signal
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (LR_enable
    :reader LR_enable
    :initarg :LR_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LR_direction
    :reader LR_direction
    :initarg :LR_direction
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (LR_servo_angle
    :reader LR_servo_angle
    :initarg :LR_servo_angle
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (LR_servo_pwm
    :reader LR_servo_pwm
    :initarg :LR_servo_pwm
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (LR_wheel_rpm
    :reader LR_wheel_rpm
    :initarg :LR_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (LR_motor_signal
    :reader LR_motor_signal
    :initarg :LR_motor_signal
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (RR_enable
    :reader RR_enable
    :initarg :RR_enable
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RR_direction
    :reader RR_direction
    :initarg :RR_direction
    :type std_msgs-msg:Bool
    :initform (cl:make-instance 'std_msgs-msg:Bool))
   (RR_servo_angle
    :reader RR_servo_angle
    :initarg :RR_servo_angle
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (RR_servo_pwm
    :reader RR_servo_pwm
    :initarg :RR_servo_pwm
    :type std_msgs-msg:Int16
    :initform (cl:make-instance 'std_msgs-msg:Int16))
   (RR_wheel_rpm
    :reader RR_wheel_rpm
    :initarg :RR_wheel_rpm
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (RR_motor_signal
    :reader RR_motor_signal
    :initarg :RR_motor_signal
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8)))
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

(cl:ensure-generic-function 'LF_enable-val :lambda-list '(m))
(cl:defmethod LF_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_enable-val is deprecated.  Use arduino_msgs-msg:LF_enable instead.")
  (LF_enable m))

(cl:ensure-generic-function 'LF_direction-val :lambda-list '(m))
(cl:defmethod LF_direction-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_direction-val is deprecated.  Use arduino_msgs-msg:LF_direction instead.")
  (LF_direction m))

(cl:ensure-generic-function 'LF_servo_angle-val :lambda-list '(m))
(cl:defmethod LF_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_servo_angle-val is deprecated.  Use arduino_msgs-msg:LF_servo_angle instead.")
  (LF_servo_angle m))

(cl:ensure-generic-function 'LF_servo_pwm-val :lambda-list '(m))
(cl:defmethod LF_servo_pwm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_servo_pwm-val is deprecated.  Use arduino_msgs-msg:LF_servo_pwm instead.")
  (LF_servo_pwm m))

(cl:ensure-generic-function 'LF_wheel_rpm-val :lambda-list '(m))
(cl:defmethod LF_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:LF_wheel_rpm instead.")
  (LF_wheel_rpm m))

(cl:ensure-generic-function 'LF_motor_signal-val :lambda-list '(m))
(cl:defmethod LF_motor_signal-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LF_motor_signal-val is deprecated.  Use arduino_msgs-msg:LF_motor_signal instead.")
  (LF_motor_signal m))

(cl:ensure-generic-function 'RF_enable-val :lambda-list '(m))
(cl:defmethod RF_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_enable-val is deprecated.  Use arduino_msgs-msg:RF_enable instead.")
  (RF_enable m))

(cl:ensure-generic-function 'RF_direction-val :lambda-list '(m))
(cl:defmethod RF_direction-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_direction-val is deprecated.  Use arduino_msgs-msg:RF_direction instead.")
  (RF_direction m))

(cl:ensure-generic-function 'RF_servo_angle-val :lambda-list '(m))
(cl:defmethod RF_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_servo_angle-val is deprecated.  Use arduino_msgs-msg:RF_servo_angle instead.")
  (RF_servo_angle m))

(cl:ensure-generic-function 'RF_servo_pwm-val :lambda-list '(m))
(cl:defmethod RF_servo_pwm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_servo_pwm-val is deprecated.  Use arduino_msgs-msg:RF_servo_pwm instead.")
  (RF_servo_pwm m))

(cl:ensure-generic-function 'RF_wheel_rpm-val :lambda-list '(m))
(cl:defmethod RF_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:RF_wheel_rpm instead.")
  (RF_wheel_rpm m))

(cl:ensure-generic-function 'RF_motor_signal-val :lambda-list '(m))
(cl:defmethod RF_motor_signal-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RF_motor_signal-val is deprecated.  Use arduino_msgs-msg:RF_motor_signal instead.")
  (RF_motor_signal m))

(cl:ensure-generic-function 'LR_enable-val :lambda-list '(m))
(cl:defmethod LR_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_enable-val is deprecated.  Use arduino_msgs-msg:LR_enable instead.")
  (LR_enable m))

(cl:ensure-generic-function 'LR_direction-val :lambda-list '(m))
(cl:defmethod LR_direction-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_direction-val is deprecated.  Use arduino_msgs-msg:LR_direction instead.")
  (LR_direction m))

(cl:ensure-generic-function 'LR_servo_angle-val :lambda-list '(m))
(cl:defmethod LR_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_servo_angle-val is deprecated.  Use arduino_msgs-msg:LR_servo_angle instead.")
  (LR_servo_angle m))

(cl:ensure-generic-function 'LR_servo_pwm-val :lambda-list '(m))
(cl:defmethod LR_servo_pwm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_servo_pwm-val is deprecated.  Use arduino_msgs-msg:LR_servo_pwm instead.")
  (LR_servo_pwm m))

(cl:ensure-generic-function 'LR_wheel_rpm-val :lambda-list '(m))
(cl:defmethod LR_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:LR_wheel_rpm instead.")
  (LR_wheel_rpm m))

(cl:ensure-generic-function 'LR_motor_signal-val :lambda-list '(m))
(cl:defmethod LR_motor_signal-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:LR_motor_signal-val is deprecated.  Use arduino_msgs-msg:LR_motor_signal instead.")
  (LR_motor_signal m))

(cl:ensure-generic-function 'RR_enable-val :lambda-list '(m))
(cl:defmethod RR_enable-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_enable-val is deprecated.  Use arduino_msgs-msg:RR_enable instead.")
  (RR_enable m))

(cl:ensure-generic-function 'RR_direction-val :lambda-list '(m))
(cl:defmethod RR_direction-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_direction-val is deprecated.  Use arduino_msgs-msg:RR_direction instead.")
  (RR_direction m))

(cl:ensure-generic-function 'RR_servo_angle-val :lambda-list '(m))
(cl:defmethod RR_servo_angle-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_servo_angle-val is deprecated.  Use arduino_msgs-msg:RR_servo_angle instead.")
  (RR_servo_angle m))

(cl:ensure-generic-function 'RR_servo_pwm-val :lambda-list '(m))
(cl:defmethod RR_servo_pwm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_servo_pwm-val is deprecated.  Use arduino_msgs-msg:RR_servo_pwm instead.")
  (RR_servo_pwm m))

(cl:ensure-generic-function 'RR_wheel_rpm-val :lambda-list '(m))
(cl:defmethod RR_wheel_rpm-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_wheel_rpm-val is deprecated.  Use arduino_msgs-msg:RR_wheel_rpm instead.")
  (RR_wheel_rpm m))

(cl:ensure-generic-function 'RR_motor_signal-val :lambda-list '(m))
(cl:defmethod RR_motor_signal-val ((m <ArduinoFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arduino_msgs-msg:RR_motor_signal-val is deprecated.  Use arduino_msgs-msg:RR_motor_signal instead.")
  (RR_motor_signal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArduinoFeedback>) ostream)
  "Serializes a message object of type '<ArduinoFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'linSpeed) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'angSpeed) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_direction) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_servo_pwm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LF_motor_signal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_direction) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_servo_pwm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RF_motor_signal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_direction) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_servo_pwm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LR_motor_signal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_enable) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_direction) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_servo_angle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_servo_pwm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_wheel_rpm) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'RR_motor_signal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArduinoFeedback>) istream)
  "Deserializes a message object of type '<ArduinoFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'linSpeed) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'angSpeed) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_direction) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_servo_pwm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LF_motor_signal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_direction) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_servo_pwm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RF_motor_signal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_direction) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_servo_pwm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LR_motor_signal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_enable) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_direction) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_servo_angle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_servo_pwm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_wheel_rpm) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'RR_motor_signal) istream)
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
  "9714a5e0162ffa0a697e028ea8e99e60")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArduinoFeedback)))
  "Returns md5sum for a message object of type 'ArduinoFeedback"
  "9714a5e0162ffa0a697e028ea8e99e60")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArduinoFeedback>)))
  "Returns full string definition for message of type '<ArduinoFeedback>"
  (cl:format cl:nil "Header header~%~%std_msgs/Float32 linSpeed~%std_msgs/Float32 angSpeed~%~%std_msgs/Bool LF_enable~%std_msgs/Bool LF_direction~%std_msgs/Int8 LF_servo_angle~%std_msgs/Int16 LF_servo_pwm~%std_msgs/Float32 LF_wheel_rpm~%std_msgs/Int8 LF_motor_signal~%~%std_msgs/Bool RF_enable~%std_msgs/Bool RF_direction~%std_msgs/Int8 RF_servo_angle~%std_msgs/Int16 RF_servo_pwm~%std_msgs/Float32 RF_wheel_rpm~%std_msgs/Int8 RF_motor_signal~%~%std_msgs/Bool LR_enable~%std_msgs/Bool LR_direction~%std_msgs/Int8 LR_servo_angle~%std_msgs/Int16 LR_servo_pwm~%std_msgs/Float32 LR_wheel_rpm~%std_msgs/Int8 LR_motor_signal~%~%std_msgs/Bool RR_enable~%std_msgs/Bool RR_direction~%std_msgs/Int8 RR_servo_angle~%std_msgs/Int16 RR_servo_pwm~%std_msgs/Float32 RR_wheel_rpm~%std_msgs/Int8 RR_motor_signal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/Int8~%int8 data~%~%================================================================================~%MSG: std_msgs/Int16~%int16 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArduinoFeedback)))
  "Returns full string definition for message of type 'ArduinoFeedback"
  (cl:format cl:nil "Header header~%~%std_msgs/Float32 linSpeed~%std_msgs/Float32 angSpeed~%~%std_msgs/Bool LF_enable~%std_msgs/Bool LF_direction~%std_msgs/Int8 LF_servo_angle~%std_msgs/Int16 LF_servo_pwm~%std_msgs/Float32 LF_wheel_rpm~%std_msgs/Int8 LF_motor_signal~%~%std_msgs/Bool RF_enable~%std_msgs/Bool RF_direction~%std_msgs/Int8 RF_servo_angle~%std_msgs/Int16 RF_servo_pwm~%std_msgs/Float32 RF_wheel_rpm~%std_msgs/Int8 RF_motor_signal~%~%std_msgs/Bool LR_enable~%std_msgs/Bool LR_direction~%std_msgs/Int8 LR_servo_angle~%std_msgs/Int16 LR_servo_pwm~%std_msgs/Float32 LR_wheel_rpm~%std_msgs/Int8 LR_motor_signal~%~%std_msgs/Bool RR_enable~%std_msgs/Bool RR_direction~%std_msgs/Int8 RR_servo_angle~%std_msgs/Int16 RR_servo_pwm~%std_msgs/Float32 RR_wheel_rpm~%std_msgs/Int8 RR_motor_signal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%================================================================================~%MSG: std_msgs/Bool~%bool data~%================================================================================~%MSG: std_msgs/Int8~%int8 data~%~%================================================================================~%MSG: std_msgs/Int16~%int16 data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArduinoFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'linSpeed))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'angSpeed))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_direction))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_servo_pwm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LF_motor_signal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_direction))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_servo_pwm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RF_motor_signal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_direction))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_servo_pwm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LR_motor_signal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_enable))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_direction))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_servo_angle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_servo_pwm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_wheel_rpm))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'RR_motor_signal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArduinoFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'ArduinoFeedback
    (cl:cons ':header (header msg))
    (cl:cons ':linSpeed (linSpeed msg))
    (cl:cons ':angSpeed (angSpeed msg))
    (cl:cons ':LF_enable (LF_enable msg))
    (cl:cons ':LF_direction (LF_direction msg))
    (cl:cons ':LF_servo_angle (LF_servo_angle msg))
    (cl:cons ':LF_servo_pwm (LF_servo_pwm msg))
    (cl:cons ':LF_wheel_rpm (LF_wheel_rpm msg))
    (cl:cons ':LF_motor_signal (LF_motor_signal msg))
    (cl:cons ':RF_enable (RF_enable msg))
    (cl:cons ':RF_direction (RF_direction msg))
    (cl:cons ':RF_servo_angle (RF_servo_angle msg))
    (cl:cons ':RF_servo_pwm (RF_servo_pwm msg))
    (cl:cons ':RF_wheel_rpm (RF_wheel_rpm msg))
    (cl:cons ':RF_motor_signal (RF_motor_signal msg))
    (cl:cons ':LR_enable (LR_enable msg))
    (cl:cons ':LR_direction (LR_direction msg))
    (cl:cons ':LR_servo_angle (LR_servo_angle msg))
    (cl:cons ':LR_servo_pwm (LR_servo_pwm msg))
    (cl:cons ':LR_wheel_rpm (LR_wheel_rpm msg))
    (cl:cons ':LR_motor_signal (LR_motor_signal msg))
    (cl:cons ':RR_enable (RR_enable msg))
    (cl:cons ':RR_direction (RR_direction msg))
    (cl:cons ':RR_servo_angle (RR_servo_angle msg))
    (cl:cons ':RR_servo_pwm (RR_servo_pwm msg))
    (cl:cons ':RR_wheel_rpm (RR_wheel_rpm msg))
    (cl:cons ':RR_motor_signal (RR_motor_signal msg))
))
