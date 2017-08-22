# -*- coding: utf-8 -*-


import re
import os
import glob
import pickle
from time import sleep
import win32api
import win32con
from nltk.stem.snowball import FrenchStemmer

from Senses.mouth import speak
from Senses.ears import listen
from Utilities.tools import files

def macro_exe(ht, key):
	macro(ht[key]['path'], ht[key]['params'])

def dial_exe(ht, key):
	interac(ht[key])

def macro(file, param_titles):
	if len(param_titles) > 0:
		params = []
		for title in param_titles.keys():
			satis = False
			speak([u'Quelle valeur voulez vous donner au paramètre: ' + param_titles[title]])
			param = listen().encode('utf-8')
			while(not satis):
				speak([u' Est-ce que ' + param + u' est la valeur que vous souhaitiez'])
				message = listen().encode('utf-8')
			
				if message == u'oui' or message == u'affirmatif':
					satis = True
				else:
					speak([u'Réessayez pour: ' + param_titles[title]])
					param = listen().encode('utf-8')
			
			params.append(param)
		custom_macro(file, params)
	
	os.system(r'start Macros\customedMacro.mrf')
	sleep(2)
	win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
	sleep(2)
	win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
	win32api.keybd_event(win32con.VK_F10, 0, 0, 0)
	sleep(2)
	os.system(r'taskkill /f /im MouseRecorder.exe')

def interac(ans):
	speak([ans])
	
def creation(msg):
		if u'fonction' in msg or u'fonctionalité' in msg or u'macro' in msg :
			creation_macro()
		else:
			creation_interac()


def creation_macro():
	list = glob.glob("Macros\*.mrf")
	
	os.system(r'start C:\"Program Files (x86)\MouseRecorder\MouseRecorder.exe"')	
	sleep(2)
	win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
	win32api.keybd_event(win32con.VK_F9, 0, 0, 0)
	sleep(2)
	
	speak([u' Quand la macro est terminée, dites le mot "terminé"'])
	satis = False
	while(not satis):
			message = listen()
			
			if message == u'terminer':
				satis = True
				sleep(2)
				win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
				win32api.keybd_event(win32con.VK_F9, 0, 0, 0)
				sleep(2)
				speak([u' Sauvegardez le fichier dans le dossier prédéfini et quittez le programme."'])
				sleep(7)
				"""win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
				win32api.keybd_event(win32con.VK_CODE[0x53], 0, 0, 0)
				sleep(2)
				win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
				sleep(2)
				os.system(r'taskkill /f /im MouseRecorder.exe')"""
			else:
				param = listen()
				
	sec_list = glob.glob("Macros\*.mrf")
	path = u'' 
	for f in sec_list:
		if f not in list:
			path = f
	i = count(path)
	
	params ={}
	if i > 0:
		speak([u' Vous avez défini' + str(i) + u'paramètres, nous allons à présent vous demander un nom pour chacun'])
		for c in range(1, i+1):
			speak([u'Quelle valeur voulez vous donner au paramètre: ' + str(c)])
			param = listen()
			satis = False
		
			while(not satis):
				speak([u' Est-ce que ' + param + u' est la valeur que vous souhaitiez'])
				message = listen()
			
				if message == u'oui' or message == u'affirmatif':
					satis = True
				else:
					speak([u'Réessayez pour: ' + str(c)])
					param = listen()
			
			params[c] = param
	
	speak([u' Quel mot ou phrase doit provoquer cette réponse?'])
	ans = listen()
	satis = False
	
	while(not satis):
		speak([u' Est-ce que ' + ans + u' est la valeur que vous souhaitiez'])
		message = listen()
		
		if message == u'oui' or message == u'affirmatif':
			satis = True
		else:
			speak([u'Réessayez'])
			ans = listen()
			
	#add function to either 1w or gow
	words = re.findall(r"[\w]+", ans, re.UNICODE)
	key = ""
	if len(words) > 1:
		with open(files(1), mode = 'r') as f:
			composed_trigger_ht = pickle.load(f)
			f.close()
			
		key = ans
		update_ht(1, composed_trigger_ht, key, macro_exe)
		
	else:
		with open(files(0), mode = 'r') as f:
			trigger_ht = pickle.load(f)
			f.close()
		
		stemmer = FrenchStemmer()	
		key = stemmer.stem(words[0])
		update_ht(0, trigger_ht, key, macro_exe)
	
	#add to macro storage structure
	with open(files(2), mode = 'r') as f:
		macro_paths_ht = pickle.load(f)
		f.close()
		
	update_ht(2, macro_paths_ht, key,{'path': path, 'params': params})
	
def creation_interac():
	speak([u'Quelle réponse voulez vous donner à l ipa'])
	param = listen()
	satis = False
	while(not satis):
		speak([u' Est-ce que ' + param + u' est la valeur que vous souhaitiez'])
		message = listen()
		
		if message == u'oui' or message == u'affirmatif':
			satis = True
		else:
			speak([u'Réessayez'])
			param = listen()
		
	speak([u' Quel mot ou phrase doit provoquer cette réponse?'])
	ans = listen()
	satis = False
	while(not satis):
		speak([u' Est-ce que ' + ans + u' est la valeur que vous souhaitiez'])
		message = listen()
		
		if message == u'oui' or message == u'affirmatif':
			satis = True
		else:
			speak([u'Réessayez'])
			ans = listen()
		
	words = re.findall(r"[\w]+", ans, re.UNICODE)
	key = ""
	if len(words) > 1:
		with open(files(1), mode = 'r') as f:
			composed_trigger_ht = pickle.load(f)
			f.close()
			
		key = ans
		update_ht(1, composed_trigger_ht, key, dial_exe)
		
	else:
		with open(files(0), mode = 'r') as f:
			trigger_ht = pickle.load(f)
			f.close()
		
		stemmer = FrenchStemmer()	
		key = stemmer.stem(words[0])
		update_ht(0, trigger_ht, key, dial_exe)
	
	#add to custom answer storage structure
	with open(files(3), mode = 'r') as f:
		interac_ht = pickle.load(f)
		f.close()
		
	update_ht(3, interac_ht, key, param)

#update_ht(1, htc, u'test', test)	
def update_ht(file_number, ht, k, v):
	ht[k] = v
	with open(files(file_number), mode = 'w') as f:
		pickle.dump(ht, f)
		f.close()

def count(file_path):
	i = 0
	with open(file_path, 'U') as macro_model:
		for line in macro_model:
			if 'P\x00A\x00R\x00A\x00M' in line:
				i+=1
	return i

def custom_macro(file_path, param_list):
	i = 0
	with open(file_path, 'U') as macro_model, open('Macros\customedMacro.mrf','wb') as customed_macro:
		for line in macro_model:
			if 'P\x00A\x00R\x00A\x00M' in line:
				customed_macro.write(custom(line, param_list[i]))
				i+=1
			else:
				customed_macro.write(line)

def custom(line, replacement):
	res = ''
	for char in replacement:
		res+=char.upper()
		res+='\x00'
	line = re.sub(r'P\x00A\x00R\x00A\x00M\x00', res, line)
	return line