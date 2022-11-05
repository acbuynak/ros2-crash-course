#!/usr/bin/env python3

# Simulated Temperature Publisher
# Author: A.C. Buynak
#
# Software License Agreement (Apache 2.0 License)
#
# Copyright (c) 2022, A.C. Buynak
# All rights reserved.
#
# Desc:
# Create a publisher to fake temperature data

## Import

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Temperature
from std_msgs.msg import Header
from builtin_interfaces.msg import Time

from math import sin
from random import uniform


# Functions

def calc_temp(x):

    # Temp in Farenheit. Ranges from 0 to 1000F
    temp = 410 * sin(0.00025*x) + 10*sin(0.001*x) + 4*(0.02*x+0.5) + 470

    return temp


# Classes

class tempSimulator(Node):

    def __init__(self):
        super().__init__('oven_control')
        self.publisher_ = self.create_publisher(Temperature, 'oven_temp', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        msg_h = Header()
        msg_h.stamp = self.get_clock().now().to_msg()
        msg_h.frame_id = 'oven'

        msg = Temperature()
        msg.header = msg_h
        msg.temperature = calc_temp(self.i)
        msg.variance = 0.0 + uniform(0,5)*0.01

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing Temp: "%s"' % msg.temperature)
        self.i += 1





def main(args=None):

    # Setup
    rclpy.init(args=args)
    oven = tempSimulator()

    # Run
    rclpy.spin(oven)

    # Cleanup
    oven.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
