# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


def supress_zero(num):
	while num.startswith('0'):
		num = num[1:]
	return num
	return line
				
def days(num):
	return{
		0 : u'Lundi',
		1 : u'Mardi',
		2 : u'Mercredi',
		3 : u'Jeudi',
		4 : u'Vendredi',
		5 : u'Samedi',
		6 : u'Dimanche'
	}[num]

def months(num):
	return{
		'1' : u'Janvier',
		'2' : u'Février',
		'3' : u'Mars',
		'4' : u'Avril',
		'5' : u'Mai',
		'6' : u'Juin',
		'7' : u'Juillet',
		'8' : u'Août',
		'9' : u'Septembre',
		'10' : u'Octobre',
		'11' : u'Novembre',
		'12' : u'Décembre'
	}[num]
	
def files(num):
	return{
		0 : u'Data\OneWordKeysHashtable.txt',
		1 : u'Data\ComposedKeysHashtable.txt',
		2 : u'Data\MacroPathsHashtable.txt'
	}[num]