from googletrans import Translator

translator = Translator()

def Translate_SI_into_EN(input) :
    translated = translator.translate(input, src='si', dest='en') 
    print(translated.text)
    return translated.text