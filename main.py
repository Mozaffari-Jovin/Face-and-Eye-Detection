import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import cv2
import numpy as np
import time

class MyMediaPlayer():
	def __init__(self):
		self.detector_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		# face detector is an object constructed from the class CascadeClassifier using the aforesaid model
		self.detector_eye = cv2.CascadeClassifier('haarcascade_eye.xml')
		self.cap = cv2.VideoCapture(0)  # 0 coresponds to the laptop webcam and 1 to the one from USB

	def play_mp3or4(self, target_dir):
		music = vlc.MediaPlayer(target_dir)
		music.play()
		time.sleep(15) # wait 15 sec

	def print_book(self):
		print("How to Write a Scientific Paper for ISI Journals") 

	def stream_webcam(self):
		while True:
			ret, frame = self.cap.read()
			if ret:
				frame = cv2.flip(frame, 1) # move column by 180 deg to flip screen
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # cvt convert color to gray
				results_face = self.detector_face.detectMultiScale(gray) # head's coordinate
				# detectMultiScale is a detector's method
				# print(results_face) # [x, y, w, h]
				# quit()
				for (x, y, w, h) in results_face:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # draw a rectangle around the head
					gray_eye = gray[y:y+h, x:x+w]
					frame_eye = frame[y:y+h, x:x+w]
					results_eye = self.detector_eye.detectMultiScale(gray_eye)
					for (ex, ey, ew, eh) in results_eye:
						cv2.rectangle(frame_eye, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
				cv2.imshow("Webcam", frame) # show frame
				q = cv2.waitKey(1) # wait for 1 second to return a frame
				if q == ord("q"): # press q key on the webcam screen to quit 
					break
		self.cap.release() # close cap
		cv2.destroyAllWindows() # this function allows users to destroy or close all windows at any time after exiting the script.


customer_input = input("Select from the menu (music, video, book, webcam) to be surprised: ")
mp = MyMediaPlayer()
if customer_input == "music":
	mp.play_mp3or4("music.mp3")
elif customer_input == "video":
	mp.play_mp3or4("music.mp4")
elif customer_input == "book":
	mp.print_book()	
elif customer_input == "webcam":
	mp.stream_webcam()
