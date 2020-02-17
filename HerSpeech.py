from gtts import gTTS
import os
import pygame
dirpath = os.getcwd()
pygame.init()
pygame.mixer.init()
MUSIC_END = pygame.USEREVENT+1

# Helper function to hold execution until mp3 finished
def PlayUntil():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            return True
# Main function to speak a phrase
def Play(Phrase):
	language = 'en-uk'
	myobj = gTTS(text=Phrase, lang=language, slow=False)
	myobj.save("AlarmSetting.mp3")

	pygame.mixer.music.load(dirpath +"/AlarmSetting.mp3")
	pygame.mixer.music.play()

	pygame.mixer.music.set_endevent(MUSIC_END)


	while True:
		if PlayUntil():
			break
	#Clean up
	os.remove("AlarmSetting.mp3")
