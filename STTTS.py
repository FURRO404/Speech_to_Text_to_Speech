#=============FURRO404=============#
#STTTS.py
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
r = sr.Recognizer()
#--------------------------------------------------#
while True:
    start = input("Press enter to start: ")
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print("You said:", text, "\n")
            sentence = gTTS(text)
            sentence.save('My_file.mp3')
            playsound('My_file.mp3')
            os.remove('My_file.mp3')
        except:
            print("whoops lol, I didnt get that")

#=============FURRO404=============#
