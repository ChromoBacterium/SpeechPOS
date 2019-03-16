import spacy
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
        print("Say something")
        audio = r.listen(source)
        text = r.recognize_google(audio) 
        try:
                print(text)        
        except:
                pass

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

for entity in doc.ents:
        print(entity.text, entity.label_)