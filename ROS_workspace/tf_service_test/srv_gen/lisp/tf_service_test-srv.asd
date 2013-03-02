
(cl:in-package :asdf)

(defsystem "tf_service_test-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TestSrv" :depends-on ("_package_TestSrv"))
    (:file "_package_TestSrv" :depends-on ("_package"))
  ))