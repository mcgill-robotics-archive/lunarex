
(cl:in-package :asdf)

(defsystem "kinect_node-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "KinectData" :depends-on ("_package_KinectData"))
    (:file "_package_KinectData" :depends-on ("_package"))
  ))