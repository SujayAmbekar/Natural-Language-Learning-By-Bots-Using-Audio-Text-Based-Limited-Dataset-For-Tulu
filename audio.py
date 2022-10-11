import speech_recognition as sr

def transcribeEnglish():
	recognizer = sr.Recognizer()
	with sr.Microphone() as inputs:
		print("Please speak now")
		listening = recognizer.listen(inputs)
		print("Analysing...")
		try:
			ent = recognizer.recognize_google(listening, language = "en")
			print("Did you say {a}?".format(a=ent))
			return ent
		except:
			print("Could not understand you.")


def transcribeTulu():
	recognizer = sr.Recognizer()
	with sr.Microphone() as inputs:
		print("Please speak now")
		listening = recognizer.listen(inputs)
		print("Analysing...")
		try:
			ent = recognizer.recognize_google(listening, language = "kn-IN")
			print("Did you say {a}?".format(a=ent))
			return ent
		except:
			print("Could not understand you.")

def recognizeTuluVoice():
    flag = 1
    while(flag):
        text= transcribeTulu()
        flag=int(input("Enter 0 if the text is correct."))
    return text

def recognizeEnglishVoice():
    flag = 1
    while(flag):
        text= transcribeEnglish()
        flag=input("Enter 0 if the text is correct.")
    return text
