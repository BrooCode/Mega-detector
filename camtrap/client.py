# USAGE
# python client.py --server-ip SERVER_IP

# import the necessary packages
from cv2 import CLAHE
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import cv2


def enchance_img(frame):
		temp_img = frame 
		wb = cv2.xphoto.createGrayworldWB()
		wb.setSaturationThreshold(0.99)
		img_wb = wb.balanceWhite(temp_img)
		img_lab = cv2.cvtColor(img_wb,cv2.COLOR_BGR2LAB)
		l,a,b = cv2.split(img_lab)
		# print(type(l))
		# g_l = cv2.cvtColor(l,cv2.COLOR_BGR2GRAY)
		clahe = cv2.createCLAHE(clipLimit=6,tileGridSize=(8,8))
		img_l = clahe.apply(l)
		img_clahe = cv2.merge((img_l,a,b))
		return cv2.cvtColor(img_clahe,cv2.COLOR_Lab2BGR)

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format('127.0.0.1'))



rpiName = socket.gethostname()
print("camera starting")

vs = VideoStream(src=0).start()
# vs = VideoStream(src='rtsp://admin:cam123@192.168.1.60:554/unicaststream/1').start()
time.sleep(2.0)


while True:
    	
	frame = vs.read()
	sender.send_image(rpiName, (frame))


