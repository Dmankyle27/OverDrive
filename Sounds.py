import vlc
import time

def Engage_Sound():
	sound_file = vlc.MediaPlayer("Directory to electroinc chime")
	sound_file.play()
	time.sleep(2)
	sound_file = vlc.MediaPlayer("Directory to engage.mp3")
	sound_file.play()


def DisEngage_Sound():
	sound_file = vlc.MediaPlayer("Directory to electroinc chime")
	sound_file.play()
	time.sleep(2)
	sound_file = vlc.MediaPlayer("directory to disengage.mp3")
	sound_file.play()


def Distracted_Sound():
	sound_file = vlc.MediaPlayer("Directory to Distracted.mp3")
	sound_file.play()
	time.sleep(1)
