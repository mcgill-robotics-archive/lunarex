import rosbag
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Int32, String, Int8

gridData = []

bag = rosbag.Bag('localization_feb10.bag')
m=''
for msg in bag.read_messages('/map'):
    gridData= msg[1]


bag.close()

print(gridData)

#if(len(sys.argv) < 2):
#    print(usage)
#    sys.exit()

#inputFile = open(sys.argv[1], 'r') 
#inputString = inputFile.read()
#scans = inputString.splitlines()

#params = scans[0].split(",")


