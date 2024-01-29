#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

class lidar_test:
    def __init__(self) -> None:
        Subscriber=rospy.Subscriber("/scan",LaserScan,self.callback_scan)
        self.data = []

    def callback_scan(self,msg):
        self.data.append(msg)
        self.data.sort(key=lambda x: x.range, reverse=True) #Сортировка данных по диапазону в порядке убывания
        if len(self.data) >10:
            self.data = self.data[:10] #Оставляем 10 верхних точек максимального диапазона
            self.data.sort(key=lambda x: x.range, reverse=True) #Сортировка данных по диапазону в порядке убывания
            print(self.data)
            rospy.signal_shutdown("10 data points received")
    
    
    
if __name__ == '__main__':
    rospy.init_node('control_node')
    mgtu_turtle = lidar_test()
    rospy.spin()   