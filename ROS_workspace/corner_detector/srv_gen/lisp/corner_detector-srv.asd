
(cl:in-package :asdf)

(defsystem "corner_detector-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :nav_msgs-msg
)
  :components ((:file "_package")
    (:file "corner_detector" :depends-on ("_package_corner_detector"))
    (:file "_package_corner_detector" :depends-on ("_package"))
  ))