# -*- coding: utf-8 -*-


# Personal Assistant Reliable Intelligent System
# By Tanguy De Bels


from Brains.social import *
from Brains.utils import *
from Brains.net import *
from Brains.custom import *
import Utilities.vars
import Utilities.tools
import Senses

import os
import re
import pickle
from nltk.stem.snowball import FrenchStemmer


stemmer = FrenchStemmer()


#loading env from vars
with open(files(0), mode = 'r') as f:
	trigger_ht = pickle.load(f)
	f.close()
	
with open(files(1), mode = 'r') as f:
	composed_trigger_ht = pickle.load(f)
	f.close()
	
with open(files(2), mode = 'r') as f:
	macro_paths_ht = pickle.load(f)
	f.close()
	
with open(files(3), mode = 'r') as f:
	custom_interactions_ht = pickle.load(f)
	f.close()


#main loop
while vars.boucling == True:
	msg = listen()
	if msg is not None:
		
		words = re.findall(r"[\w]+", msg, re.UNICODE)
		last_index = 0
		
		for idx in range(len(words)):
			w = stemmer.stem(words[idx])
			
			if w in trigger_ht.keys():
				for k in composed_trigger_ht.keys():
					if k in u" ".join(w for w in words[last_index+1:idx]):
						if composed_trigger_ht[k] == macro_exe:
							macro_exe(macro_paths_ht, k)
						elif composed_trigger_ht[k] == dial_exe:
							dial_exe(custom_interactions_ht, k)
						else:
							composed_trigger_ht[k](msg)
				last_index = idx
				
				if trigger_ht[w] == macro_exe:
					macro_exe(macro_paths_ht, w)
				elif trigger_ht[w] == dial_exe:
					dial_exe(custom_interactions_ht, w)				
				else:
					trigger_ht[w](msg)

		for k in composed_trigger_ht.keys():
			if k in u" ".join(w  for w in words[last_index+1:]):
				if composed_trigger_ht[k] == macro_exe:
					macro_exe(macro_paths_ht, k)
				elif composed_trigger_ht[k] == dial_exe:
					dial_exe(custom_interactions_ht, k)
				else:
					composed_trigger_ht[k](msg)
