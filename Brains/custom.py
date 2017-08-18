# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


import re
import pickle
from Senses.mouth import speak
from Senses.ears import listen

def macro(file, param_titles):
	params = []
	for title in param_titles:
		satis = False
		speak([u'Quelle valeur voulez vous donnez au paramètre: ' + title])
		param = listen()
		while(not satis):
			speak([u' Est-ce que ' + param + u' est la valeur que vous souhaitiez'])
			message = listen()
			
			if message == u'oui' or message == u'affirmatif':
				satis = True
			else:
				speak([u'Réessayez pour: ' + title])
				param = listen()
			
		params.append(param)
		
	custom_macro(file, params)
	#call

#update_ht(1, htc, u'test', test)	
def update_ht(file_number, ht, k, v):
	ht[k] = v
	with open(files(file_number), mode = 'w') as f:
		pickle.dump(ht, f)
		f.close()
		
def custom_macro(file_path, param_list):
	i = 0
	with open(file_path, 'U') as macro_model, open('Macros\customedMacro.mrf','U') as customed_macro:
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