import cv2
import numpy as np
import obd
import time
from tkinter import *
import FaceRec as fr
import Sounds as sd

class OpenDrive(Frame):
	global Distracted
	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master

		self.init_window()

	def init_window(self):
		self.master.title("OpenDrive")

		self.pack(fill=BOTH, expand=1)

		engageButton = Button(self, text="Engage", command=self.engage)
		engageButton.place(x=0, y=0)

	def Distracted(self):
		time.sleep(2)
		text = Label(self, text="PLEASE PAY ATTENTION!")
		text.pack()
		time.sleep(4)
		sd.Distracted_Sound()

	def engage(self):
		sd.Engage_Sound()
		fr.facedetect()

	def disengage(self):
		sd.DisEngage_Sound()

root = Tk()

root.geometry("400x300")

app = OpenDrive(root)

root.mainloop()
