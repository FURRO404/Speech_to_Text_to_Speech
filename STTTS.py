#===========FURRO404===========#
#STTTS
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time
#------------------#
r = sr.Recognizer()

def Language_Selector():
    global lang1
    global lang2
    lang_list = ["de-DE", "en-US"]
    
    print(" - - - Language Codes - - -")
    print(" - - - - - - - - - - - - - - - - - -")
    print(" - - German ~ de-DE - - ")
    print(" - - English ~ en-US - - ")                  #Language Selector Section
    lang1 = str(input("\nEnter language code: "))
    
    if lang1 not in lang_list:
        print("\n\nINVALID LANGUAGE CODE\n\n")
        Language_Selector()

    else:
        lang_conv = {
            "de-DE" : "de",
            "en-US" : "en"
            }
        lang2 = lang_conv[lang1]
#-----------------Actual Engine-----------------#
Language_Selector()
while True:
    ready = input("Press enter when ready: ")
    with sr.Microphone() as source:
        try:
            print("\n\nListening!")
            audio = r.listen(source)
            text = r.recognize_google(audio, language = lang1)   #Speech to Text
            print("You said:", text, "\n")

            if text == "change language":
                Language_Selector()     #Change Language
                continue

            sentence = gTTS(text, lang = lang2)
            sentence = gTTS(text, lang = lang2)
            sentence.save('My_file.mp3')        #Text to Speech
            playsound('My_file.mp3')
            os.remove('My_file.mp3')
            
        except:
            print("whoops lol, I didnt get that\n")
            time.sleep(1)
#===========FURRO404===========#
