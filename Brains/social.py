# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


from Senses.mouth import speak
from Senses.ears import listen
from Utilities import vars

def hello(msg):
	speak([u' Bienvenue monsieur', u' Bonjour monsieur'])
	#once

def ty(msg):
	speak([u' Derien', u' Pas de problèmes monsieur'])

def called(msg):
	speak([u' Oui monsieur?', u' Que puis-je pour vous?'])

def whatsup(msg):
	speak([u' Bien, merci'])

def rude(msg):
	speak([u' Surveillez votre langage je vous prie!'])

def shutdown(msg):
	speak([u' êtes vous sûr monsieur?'])
	msg = listen()
	if msg == u'oui' or msg == u'affirmatif':
		speak([u' Aurevoir monsieur', u' Paris s éteindra dans 3, 2, 1, 0'])
		vars.boucling = False

def pause(msg):
	tmp = listen()
	while tmp != (vars.name):
		tmp = listen()
		rand = [u' De nouveau en ligne', u' Que puis-je pour vous?']
		speak(rand)