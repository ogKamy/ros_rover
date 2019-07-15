#! /usr/bin/env python

import navio.adc
import navio.util

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist


class AdcReader(object):
    def __init__(self):
        self.pub = rospy.Publisher('/health/batteries', Float32MultiArray, queue_size=1)
        self.adc = navio.adc.ADC()
        self.adc_voltages = Float32MultiArray()

    def get_voltage(self, direction):
        for i in range (0, self.adc.channel_count):
            self.adc_voltages[i] = self.adc.read(i)
            
        self.pub.publish(adc_voltages)


if __name__ == "__main__":
    rospy.init_node('adc_reader')
    adc_reader = AdcReader()

    rate = rospy.Rate(0.1)

    while not rospy.is_shutdown():
        adc_reader.get_voltage()
        rate.sleep()