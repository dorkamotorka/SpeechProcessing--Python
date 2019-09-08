import speech_recognition as SR
import time

Rec = SR.Recognizer()
Mic = SR.Microphone()

try :
    with Mic as source :
        Rec.adjust_for_ambient_noise(source, duration=0.5)
        audio = Rec.listen(source)
    print(Rec.recognize_google(audio))
except KeyboardInterrupt :
    pass