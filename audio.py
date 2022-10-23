import speech_recognition as sr

def transcribeEnglish():
	recognizer = sr.Recognizer()
	with sr.Microphone() as inputs:
		listening = recognizer.listen(inputs)
		try:
			ent = recognizer.recognize_google(listening, language = "en")
			return ent
		except:
			return 0


def transcribeTulu():
	recognizer = sr.Recognizer()
	with sr.Microphone() as inputs:
		listening = recognizer.listen(inputs)
		try:
			ent = recognizer.recognize_google(listening, language = "kn-IN")
			return ent
		except:
			return 0

def recognizeTuluVoice():
	x = transcribeTulu()
	while not x:
		x = transcribeTulu()
	return x

def recognizeEnglishVoice():
	x = transcribeEnglish()
	while not x:
		x = transcribeEnglish()
	return x
