from HerSpeech import Play
from YourSpeech import SpeechToAudioFile, AudioFileToText
from NewsApp import BBCTopTenHeadlines
import time as time
import pygame
from OpenWeatherApp import GetCurrentWeather
from ArduinoInterface import SendSignal
def PlayWakeUp():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("/home/rmslick/EMMA/MaggieMay.mp3")
    pygame.mixer.music.play()
    while True:
        wake = input("Hit space to wake up")
        if wake == " ":
            pygame.mixer.music.stop()
            break
#Function that runs as alarm

#Function to get the days weather
def Alarm(Alarm):
    Time = time.strftime("%H:%M")
    while Time != Alarm:
        Time = time.strftime("%H:%M")
        #print(Time)
    print("Wake up!")
    PlayWakeUp()

# Function to account for awkward returns from Stt
def Reformat(rtime):
    try :
        rtime = str(rtime)
        if len(rtime) == 1:
            rtime = "0" + rtime +":00"
        elif len(rtime) == 2:
            rtime = rtime + ":00"
        elif len(rtime) == 3 :
            new_rtime = "0"+rtime[0] + ":" + rtime[1] + rtime[2]
            rtime = new_rtime
        #6:30
        #1020?
        elif len(rtime) == 4:
            if rtime[1] == ":":
                rtime = "0" +rtime
            else:
                rtime = rtime[0:2]+":"+rtime[2:4]
        else:
            return 0
        print("Alarm set for "+ rtime)
        return rtime
    except:
        print("Whoops, error in the input")
        return 0

def RunLoop():
    SendSignal(49)
    ttime = 1
    Play("Good evening sir")
    while True:
        try:
            Play("What time would you like your wake up call?")
            SpeechToAudioFile(3,"Tryout.wav")
            ytime = AudioFileToText("Tryout.wav")
            ttime = Reformat(ytime)
            break
        except:
            Play("Sorry sir, didn't catch that.")
    #Pre Alarm
    Alarm(ttime)
    #Post alarm
    Play("Good mornind sir.")
    Play("Shall I get the coffee ready then sir?")
    SpeechToAudioFile(3,"Coffee.wav")
    coffee = AudioFileToText("Coffee.wav")
    if coffee == "yes":
        SendSignal(48)
    Play(GetCurrentWeather())
    Play("Now for the news.  Reporting for BBC News.")
    Play(BBCTopTenHeadlines())
    Play("That is all for todays news.")
    Play("Have a great day, sir.")
def main():
    RunLoop()

if __name__ == "__main__":
    main()
