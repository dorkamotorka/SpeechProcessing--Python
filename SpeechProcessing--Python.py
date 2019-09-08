import speech_recognition as SR
import time
import sys
from Translator import Translate_SI_into_EN

#def SpeechRec() :
Rec = SR.Recognizer()
Mic = SR.Microphone()

while True :
    try :
        with Mic as source :
            Rec.adjust_for_ambient_noise(source, duration=0.5)
            audio = Rec.listen(source)
            print(Rec.recognize_google(audio))
            #return Rec.recognize_google(audio)

    except :
        print("Error")

    
    
