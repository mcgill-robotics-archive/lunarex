; Auto-generated. Do not edit!


(cl:in-package corner_detector-msg)


;//! \htmlinclude Corners.msg.html

(cl:defclass <Corners> (roslisp-msg-protocol:ros-message)
  ((LR_corner
    :reader LR_corner
    :initarg :LR_corner
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (RR_corner
    :reader RR_corner
    :initarg :RR_corner
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (LF_corner
    :reader LF_corner
    :initarg :LF_corner
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (RF_corner
    :reader RF_corner
    :initarg :RF_corner
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (resolution
    :reader resolution
    :initarg :resolution
    :type cl:float
    :initform 0.0)
   (width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0)
   (left
    :reader left
    :initarg :left
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Corners (<Corners>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Corners>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Corners)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name corner_detector-msg:<Corners> is deprecated: use corner_detector-msg:Corners instead.")))

(cl:ensure-generic-function 'LR_corner-val :lambda-list '(m))
(cl:defmethod LR_corner-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:LR_corner-val is deprecated.  Use corner_detector-msg:LR_corner instead.")
  (LR_corner m))

(cl:ensure-generic-function 'RR_corner-val :lambda-list '(m))
(cl:defmethod RR_corner-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:RR_corner-val is deprecated.  Use corner_detector-msg:RR_corner instead.")
  (RR_corner m))

(cl:ensure-generic-function 'LF_corner-val :lambda-list '(m))
(cl:defmethod LF_corner-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:LF_corner-val is deprecated.  Use corner_detector-msg:LF_corner instead.")
  (LF_corner m))

(cl:ensure-generic-function 'RF_corner-val :lambda-list '(m))
(cl:defmethod RF_corner-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:RF_corner-val is deprecated.  Use corner_detector-msg:RF_corner instead.")
  (RF_corner m))

(cl:ensure-generic-function 'resolution-val :lambda-list '(m))
(cl:defmethod resolution-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:resolution-val is deprecated.  Use corner_detector-msg:resolution instead.")
  (resolution m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:width-val is deprecated.  Use corner_detector-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:height-val is deprecated.  Use corner_detector-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'left-val :lambda-list '(m))
(cl:defmethod left-val ((m <Corners>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader corner_detector-msg:left-val is deprecated.  Use corner_detector-msg:left instead.")
  (left m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Corners>) ostream)
  "Serializes a message object of type '<Corners>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'LR_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'LR_corner))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'RR_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'RR_corner))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'LF_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'LF_corner))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'RF_corner))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'RF_corner))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'resolution))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'left) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Corners>) istream)
  "Deserializes a message object of type '<Corners>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'LR_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'LR_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'RR_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'RR_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'LF_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'LF_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'RF_corner) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'RF_corner)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'resolution) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'left) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Corners>)))
  "Returns string type for a message object of type '<Corners>"
  "corner_detector/Corners")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Corners)))
  "Returns string type for a message object of type 'Corners"
  "corner_detector/Corners")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Corners>)))
  "Returns md5sum for a message object of type '<Corners>"
  "a4f1fa3bb3f9c8b6d82f1472cf657570")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Corners)))
  "Returns md5sum for a message object of type 'Corners"
  "a4f1fa3bb3f9c8b6d82f1472cf657570")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Corners>)))
  "Returns full string definition for message of type '<Corners>"
  (cl:format cl:nil "uint8[] LR_corner~%uint8[] RR_corner~%uint8[] LF_corner~%uint8[] RF_corner~%float32 resolution~%uint32 width~%uint32 height~%bool left~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Corners)))
  "Returns full string definition for message of type 'Corners"
  (cl:format cl:nil "uint8[] LR_corner~%uint8[] RR_corner~%uint8[] LF_corner~%uint8[] RF_corner~%float32 resolution~%uint32 width~%uint32 height~%bool left~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Corners>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'LR_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'RR_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'LF_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'RF_corner) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Corners>))
  "Converts a ROS message object to a list"
  (cl:list 'Corners
    (cl:cons ':LR_corner (LR_corner msg))
    (cl:cons ':RR_corner (RR_corner msg))
    (cl:cons ':LF_corner (LF_corner msg))
    (cl:cons ':RF_corner (RF_corner msg))
    (cl:cons ':resolution (resolution msg))
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
    (cl:cons ':left (left msg))
))
