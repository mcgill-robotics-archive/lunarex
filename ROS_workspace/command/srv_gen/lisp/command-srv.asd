
(cl:in-package :asdf)

(defsystem "command-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "QuadrantRequest" :depends-on ("_package_QuadrantRequest"))
    (:file "_package_QuadrantRequest" :depends-on ("_package"))
  ))