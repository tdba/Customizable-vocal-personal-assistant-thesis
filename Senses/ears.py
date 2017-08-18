# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


import speech_recognition as sr
import Utilities
	
r = sr.Recognizer()

def listen():
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print(u'Say something!')
		audio = r.listen(source)

	try:
		s = (r.recognize_google(audio, language = "fr-FR")).lower()
		print s
		return s

	except sr.UnknownValueError:		
		print(u'Could not understand audio')
		return ''
	except sr.RequestError as e:
		print(u'Could not request results; {0}'.format(e))