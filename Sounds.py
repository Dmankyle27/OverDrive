import vlc
import time

def Engage_Sound():
	sound_file = vlc.MediaPlayer("/home/logan/Desktop/OpenDrive/Electronic_Chime-KevanGC-495939803.mp3")
	sound_file.play()
	time.sleep(2)
	sound_file = vlc.MediaPlayer("/home/logan/Desktop/OpenDrive/engage.mp3")
	sound_file.play()


def DisEngage_Sound():
	sound_file = vlc.MediaPlayer("/home/logan/Desktop/OpenDrive/Electronic_Chime-KevanGC-495939803.mp3")
	sound_file.play()
	time.sleep(2)
	sound_file = vlc.MediaPlayer("/home/logan/Desktop/OpenDrive/disengage.mp3")
	sound_file.play()


def Distracted_Sound():
	sound_file = vlc.MediaPlayer("/home/logan/Desktop/OpenDrive/Distracted.mp3")
	sound_file.play()
	time.sleep(1)
