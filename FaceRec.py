import cv2
import numpy as np
import main as mn

class Faces:

	def facedetect(self):
		faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
		cam = cv2.VideoCapture(0);

		while(True):
			ret,img=cam.read();
			gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			faces=faceDetect.detectMultiScale(gray,1.3,5);
			status = "Distracted"
			for(x,y,w,h) in faces:
				cv2.rectangle(img,(x,y) , (x+w,y+h), (255,0,0),2)
				status = "Not Distracted"
			if status == "Not Distracted":
				pass
			else:
				mn.Distracted()
			cv2.imshow("Distraction Monitoring System", img);
			if(cv2.waitKey(1)==ord('q')):
				break;

		cam.release()
		cv2.destroyAllWindows()
