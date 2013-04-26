
(cl:in-package :asdf)

(defsystem "arduino_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "LiteArduinoFeedback" :depends-on ("_package_LiteArduinoFeedback"))
    (:file "_package_LiteArduinoFeedback" :depends-on ("_package"))
    (:file "ArduinoFeedback" :depends-on ("_package_ArduinoFeedback"))
    (:file "_package_ArduinoFeedback" :depends-on ("_package"))
  ))