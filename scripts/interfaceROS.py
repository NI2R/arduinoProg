#!/usr/bin/env python


import sys
import os
import rospy

import comArduino

from std_msgs.msg import String as ROS_String
from geometry_msgs.msg import Pose as ROS_Pose

class Robot_properties:
	def __init__(self):

		self.publish_topic = 'arduinoState' #nom du topic que je publie

		self.pub = rospy.Publisher(self.publish_topic, ROS_String, queue_size=1)

	#def subscrib(self, ros_data):

	def publish(self, message): #x sera la position et y la couleur
		Msg = ROS_String
		Msg = message  
		self.pub.publish(Msg)

	def publishImage(self, image):
		self.pubImg.publish(image)



def main():
	rospy.init_node('Traite_Image', anonymous=True)
	Objtester = comArduino.Tester() #objet de type objet
	rospy.sleep(5)
	while not rospy.is_shutdown():
		Objtester.updater()
		rospy.sleep(0.03)


if __name__ ==  '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
