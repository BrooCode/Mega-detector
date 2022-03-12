
# from imutils import build_montages
# from datetime import datetime
import numpy as np
import imagezmq
# import argparse
import imutils
import cv2
import run_tf_detector as detect
import winsound


imageHub = imagezmq.ImageHub()

def send_notification():
	#send notification to server
	frequency = 2500
	duration = 1000
	winsound.Beep(frequency,duration)


while True:
	(rpiName, frame) = imageHub.recv_image()
	imageHub.send_reply(b'OK')

	frame = imutils.resize(frame, width=1200)
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)


	cv2.putText(frame, rpiName, (10, 25),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

	res,flag = detect.load_and_run_detector(frame)

	cv2.imshow("animal_detection",res)
	# cv2.imshow("animal_detection",detect.load_and_run_detector(frame))

	if flag == 1:
		frequency = 2500
		duration = 500
		winsound.Beep(frequency,duration)

	key = cv2.waitKey(1) & 0xFF



	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()