# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


import pyttsx
import random

engine = pyttsx.init()
engine.setProperty('rate', 130)

def speak(rand):
	engine.say(random.choice(rand))
	engine.runAndWait()