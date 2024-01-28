#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

class lidar_test:
    def __init__(self) -> None:
        Subscriber=rospy.Subscriber("/scan",LaserScan,self.callback_scan)
        
    def callback_scan(self,msg):
        print (msg)
    
    
    
if __name__ == '__main__':
    rospy.init_node('control_node')
    mgtu_turtle = lidar_test()
    rospy.spin()        