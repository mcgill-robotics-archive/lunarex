import rosbag
bag = rosbag.Bag('basic_localization_stage.bag')
for topic, msg, t in bag.read_messages(topics=['/tf']):
    print msg
bag.close()

