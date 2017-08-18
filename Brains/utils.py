# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


from Senses.mouth import speak
from Utilities.tools import *
import net

import os
from time import localtime, strftime
from datetime import date

def h(msg):
	time = strftime("%X", localtime()).split(":")
	speak([" Il est " + supress_zero(time[0]) + " heures et " + supress_zero(time[1]) + " minutes.", " Il est " + supress_zero(time[0]) + " heures " + supress_zero(time[1]), " " + supress_zero(time[0]) + " heures " + supress_zero(time[1])])

def d(msg):
	dat = date.today().strftime("%Y-%m-%d").split('-')
	speak([" Nous sommes le " + days(date.today().weekday()) + supress_zero(dat[2]) + months(supress_zero(dat[1])), " Nous sommes le " + supress_zero(dat[2]) + months(supress_zero(dat[1]))])

def sound(message):
	if (u'coupe') in message:
		os.system('nircmd.exe mutesysvolume 1')
	elif (u'remets' in message):
		os.system('nircmd.exe mutesysvolume 0')
	elif (u'baisse') in message or (u'diminue') in message:
		if (u'un peu') in message:
			os.system(u'nircmd.exe changesysvolume -6553')
		else:
			os.system(u'nircmd.exe changesysvolume -13107')
	elif (u'augmente') in message or (u'monte') in message:
		os.system(u'nircmd.exe mutesysvolume 0')
		if (u'un peu') in message:
			os.system(u'nircmd.exe changesysvolume 6553')
		else:
			os.system(u'nircmd.exe changesysvolume 13107')

def bright(message):
	if (u'baisse') in message or (u'diminue') in message:
		if (u'un peu') in message:
			os.system(u'nircmd.exe changebrightness -10')
		else:
			os.system(u'nircmd.exe changebrightness -20')
	elif (u'augmente') in message or (u'monte') in message:
		if (u'un peu') in message:
			os.system(u'nircmd.exe changebrightness 10')
		else:
			os.system(u'nircmd.exe changebrightness 20')

def search(message):
	if (u'sur') in message:
		tmp = message.split(u'sur')[1]
	elif (u'à propos du') in message:
		tmp = message.split(u'à propos du')[1]
	elif (u'à propos de') in message:
		tmp = message.split(u'à propos de')[1]
	elif (u'à propos des') in message:
		tmp = message.split(u'à propos des')[1]
	elif (u'à propos d\'') in message:
		tmp = message.split(u'à propos d\'')[1]
	else:
		tmp = message
	#TypeOfSearch:
	net.net_search(tmp)
