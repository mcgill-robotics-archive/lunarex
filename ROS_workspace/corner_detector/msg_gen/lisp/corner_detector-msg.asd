
(cl:in-package :asdf)

(defsystem "corner_detector-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Corners" :depends-on ("_package_Corners"))
    (:file "_package_Corners" :depends-on ("_package"))
  ))