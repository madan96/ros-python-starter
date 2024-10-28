#!/usr/bin/env python3
import unittest

import rospy
import rostest
from std_msgs.msg import Bool


class TestROSNode(unittest.TestCase):

    def setUp(self):
        rospy.init_node("test_ros", anonymous=True)
        self.received_message = None

    def test_subscriber_receives_messages(self):
        self.received_message = rospy.wait_for_message("dog_status", Bool, timeout=10)

        print("Received message from dog_status topic")
        self.assertEqual(self.received_message.data, True)


if __name__ == "__main__":
    rostest.rosrun("python_starter", "test_ros_node", TestROSNode)
