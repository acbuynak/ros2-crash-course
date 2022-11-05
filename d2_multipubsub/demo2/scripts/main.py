#!/usr/bin/env python3
#
# Software License Agreement (Apache 2.0 License)
# Copyright (c) 2022, The Ohio State University
# The Artificially Intelligent Manufacturing Systems Lab (AIMS)
#
# Author: acbuynak
#
# Node: demo2


#############
## Imports ##
#############

# ROS
import rclpy
from rclpy.node import Node

# ROS Messages
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import Pose

from cv_bridge import CvBridge, CvBridgeError


######################
## Class Controller ##
######################

class MyControl(Node):
    '''
        1 - Initialize ROS node and set publishing rate.
        2 - Setup publisher & subscriber connections.
        3 - Process data recieved.
        4 - Publish to custom ROS message. 
    '''

    def __init__(self) -> None:

        # Setup Node
        super().__init__('demo2_node')


	# Add code here!


##########
## Main ##
##########

def main(args=None):

    rclpy.init(args=args)

    # Init Node & Spin
    mc = MyControl()
    rclpy.spin(mc)

    # Cleanup
    mc.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()