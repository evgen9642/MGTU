#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

class lidar_test:
    def __init__(self) -> None:
        Subscriber=rospy.Subscriber("/scan",LaserScan,self.callback_scan)
        self.data = []

    def callback_scan(self,msg):
        self.data.append(msg)
        if len(self.data) == 10:
            print(self.data)
            rospy.signal_shutdown("10 data points received")
    
    
    
if __name__ == '__main__':
    rospy.init_node('control_node')
    mgtu_turtle = lidar_test()
    rospy.spin()        